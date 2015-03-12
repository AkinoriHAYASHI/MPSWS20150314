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

from django.conf.urls import patterns, include, url
from django.contrib import admin

from google.views import WelcomeView, CallbackView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oauth_sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^callback', CallbackView.as_view(), name='callback'),
    url(r'^', WelcomeView.as_view(), name='welcome'),
)
