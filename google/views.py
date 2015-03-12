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

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from urllib.parse import urlencode
from urllib.request import urlopen, Request
from google.google_oauth2 import GoogleOAuth2
from google.api_executor import GoogleOAuth2V2UserinfoApiExecutor as UserinfoApiExecutor

# Create your views here.
CLIENT_ID = 'Your Client ID'
CLIENT_SECRET = 'Your Client Secret'
REDIRECT_URI = 'Your Redirect URI'

class WelcomeView(View):
    def get(self, request):
        # 図中の (A) に該当するコードを書く。
        # つまり、情報を含んだ URL を作成する。
        url = ''
        return HttpResponse('<a href="%s">Google のユーザー情報へのアクセスを承認。</a>' % (url))
    
class CallbackView(View):
    def get(self, request):
        if request.GET.get('code'):
            # code には承認コードが格納される。
            code = request.GET['code']

            # ここに図中 (D) と (E) に該当するコードを書く。
            # つまり、必要な情報を承認サーバーに送信し、その結果としてアクセストークンを含む情報を得る。
            token = dict()

            # ここに図中の (F) と (G) に該当するコードを書く。
            # つまり上で得た token から access_token を取り出し、リソースサーバーの
            # ユーザー情報を管理するエンドポイントに送信し、結果としてユーザー情報を得る。
            user_info = dict()
            
            txt = ''
            for key, value in userinfo.items():
                txt = '%s<p>%s: %s</p>' % (txt, key, value)
            
            return HttpResponse(txt)
        else:
            return HttpResponse('承認求む。。。')
