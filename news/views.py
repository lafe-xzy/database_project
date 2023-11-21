from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import auth
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

from .models import *

'''用户注册'''
def sign_up(request):
    return_code = '0'
    if request.method == 'POST':
        username = request.POST.get('username') # 要求用户名唯一
        passward = request.POST.get('password')
        
        try:
            user = User.objects.create_user(username=username, password=passward)
            user.save()
            if user:    # 注册成功后跳转至登录
                auth.login(request, user)
                return redirect('log_in', {'return_code':'1'})    
        except IntegrityError:
            return_code = '2'          # 用户名已存在
            return render(request, 'sign_up.html', {'return_code':return_code})
            
    return render(request, 'sign_up.html', {'return_code':return_code})

'''用户登录'''
def log_in(request):   
    return_code = '0'
    if request.method == 'POST':        
        username = request.POST.get('username')        
        password = request.POST.get('password')        
          
        try:   
            user = auth.authenticate(username=username, password=password)   
            if user:            
                auth.login(request, user)   # 登录    
                return redirect('index', {'return_code':'1'})    # 登录成功后跳转至主页
            else:
                raise auth.PermissionDenied
        except auth.PermissionDenied:
            return_code = '2'
            return render(request, 'log_in.html', {'return_code':return_code})
    return render(request, "log_in.html", {'return_code':return_code})

'''主页'''
def index(request):    
    # name = request.user.username    
    # password = request.user.password    
    return get_some_dish(request)

'''登出'''
def log_out(request):    
    auth.logout(request)    
    return redirect('index')

'''查看评论'''
# def get_comment_by_dish_name(request):
#     return_code = '0'
#     if request.method == 'GET':
#         dish_name = request.GET.get('dish_name')
#         if dish_name is None:
#             return_code = '1'
#             return render(request, 'index.html', {'return_code': return_code})
        
#         comment = Dish.objects.filter(dish_name=dish_name)
#         if comment is None:
#             return_code = '2'
#             return render(request, 'index.html', {'return_code': return_code})
        
#         comment_data = list(comment.values())
#         return_code = '3'   # 菜品存在且有评论
#         return render(request, 'index.html', {'return_code': return_code, 'comment_data': comment_data})
    
#     return render(request, 'index.html', {'return_code': return_code})

'''主页评论展示'''
def get_some_dish(request):
    all_dish = Comments.objects.select_related('dish_id').all()
    return render(request, 'index.html', {'comment_data': all_dish})
    
'''搜索界面'''
def search(request):
    campus_list = Campus.objects.all()
    cafeteria_list = Cafeteria.objects.all()
    served_time_list = ServedTime.objects.all()
    search_result = None
    if request.method == 'GET':
        query = request.GET.get('q', '')
        campus = request.GET.get('campus', '')
        cafeteria = request.GET.get('cafeteria', '')
        served_time = request.GET.get('served_time', '')

        # 构建查询条件
        filters = {}
        if query:
            filters['dish_name__icontains'] = query
        # if campus:
            # filters['campus_id'] = campus
            # cafeteria_list = Cafeteria.objects.filter(campus_id=campus)
        if cafeteria:
            filters['cafeteria_id'] = cafeteria
            # served_time_list = ServedTime.objects.filter(cafeteria_id=cafeteria)
        if served_time:
            filters['served_time_id'] = served_time

        # 执行查询
        search_result = Dish.objects.filter(**filters)
        
    context = {
        'campuses': campus_list,
        'cafeterias': cafeteria_list,
        'served_times': served_time_list,
        # 其他上下文数据
    }
    
    return render(request, 'search.html', {'search_result': search_result, 'context': context})

def detail(request, dish_id):
    detail = get_object_or_404(Dish, pk=dish_id)
    return render(request, 'detail.html', {'detail': detail})

    
            
        
