"""fuzzbuzz_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static

from fuzzbuzz_app1 import views as appviews
from fuzzbuzz_django import views as projviews


urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', projviews.index),

    # path('userinfo/', appviews.Userinfo_list),      # django rest api 연습페이지
    
    path('app1/', include('fuzzbuzz_app1.urls')),   # django webpage 기능

    path('dl-con-hj/', appviews.dl_con_hj),               # DL 혼잡도 데이터 송수신
    path('dl-cir-hj/', appviews.dl_cir_hj),               # DL 순환 데이터 송수신

    path('dl-con-sh/', appviews.dl_con_sh),               # DL 혼잡도 데이터 송수신
    path('dl-cir-sh/', appviews.dl_cir_sh),               # DL 순환 데이터 송수신


    path('app-faq/', appviews.app_FAQ),             # Android app FAQ 데이터 송수신
    path('app-login/', appviews.app_login),         # Android app 로그인
    path('app-signup/', appviews.app_signup),       # Android app 회원가입
    path('app-con/', appviews.app_con),             # Android app 혼잡도 통신

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
