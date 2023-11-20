from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),                # 默认登录页面
    path('sign_up', views.sign_up, name='sign_up'),  # 注册
    path('log_in', views.log_in, name='log_in'),           # 登录
    path('index', views.index, name='index'),           # 主页
    path('log_out', views.log_out, name='log_out'),        # 登出
    
]