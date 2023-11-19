from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),                # 默认登录页面
    path('register', views.register, name='register'),  # 注册
    path('login', views.login, name='login'),           # 登录
    path('index', views.index, name='index'),           # 主页
    path('logout', views.logout, name='logout'),        # 登出
]