"""UnistashFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Functions.views import index,file1 ,company,index1,logout
from django.conf.urls import include ,url
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^logout/$',logout ,   name='logout'),
    url(r'^password_reset/$', auth_views.password_reset,  name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,{'template_name': 'login.html'}, name='password_reset_complete'),

#url(r'^login/', include('django.contrib.auth.urls')),
    url(r'^(?P<string>[\w\-]+)/$',index,name='index'),
    # url(r'^login/(?P<string>[\w\-]+)/$',index,name='index'),
   
    url(r'^notes/(?P<string1>[\w\-]+)/$',file1, name='files'),
    url(r'^interview/(?P<company>[\w\-]+)/$', company ,name='company'),
    #url(r'^content/(?P<string>[\w\-]+)/(?P<stri>[\w\-]+)/$',sidebar, name='side'),
   url(r'^captcha/', include('captcha.urls')),
   url(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
]
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

