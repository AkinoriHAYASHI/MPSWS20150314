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

from contrib.api_executor.api_executor import ApiExecutor

class GoogleOAuth2V2UserinfoApiExecutor(ApiExecutor):
    def __init__(self, access_token):
        base_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
        params = {'access_token': access_token}
        super(GoogleOAuth2V2UserinfoApiExecutor, self).__init__(base_url, params)
