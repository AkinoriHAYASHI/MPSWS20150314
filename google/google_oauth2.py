#
#    (c) 2014 Morning Project Samurai
#
#    This file is part of Lecture at Morning Project Samurai meeting 3/14, 2015.
#    This is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License.
#
#    This is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = 'Junya Kaneko'

from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json

class GoogleOAuth2:
    __auth_url = 'https://accounts.google.com/o/oauth2/auth'
    __auth_token_url = 'https://accounts.google.com/o/oauth2/token'
    __client_id = ''
    __client_secret = ''
    
    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value

    @property
    def client_secret(self):
        return self.__client_secret

    @client_secret.setter
    def client_secret(self, value):
        self.__client_secret = value

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
            
    def get_auth_url(self, redirect_uri, scope, response_type = 'code'):
        params = {
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
            'scope': scope,
            'response_type': response_type
            }
        return self.__auth_url + '?' + urlencode(params)

    def get_auth_token(self, code, redirect_uri, grant_type = 'authorization_code'):
        params = {
            'code': code,
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
            'client_secret': self.client_secret,
            'grant_type': grant_type
            }
        request = Request(url=self.__auth_token_url, data=urlencode(params).encode('utf-8'))
        response = urlopen(request)
        return json.loads(response.read().decode('utf-8'))
