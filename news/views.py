from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.db import IntegrityError
from django.contrib.auth.models import User

from .models import *


def sign_up(request):
    '''
    用户注册
    - url: /sign_up
    - method: POST
    - 传入参数: username, password
    - 返回值: 0-未操作, 1-成功，2-用户名已存在
    '''
    return_code = 0
    if request.method == 'POST':
        # 从 POST 请求中获取用户名、密码参数
        username = request.POST.get('username') 
        passward = request.POST.get('password')
        
        try:
            # 创建用户
            user = User.objects.create_user(username=username, password=passward)
            user.save()
            if user:    # 如果注册成功，跳转到登录页面
                return_code = 1
                return render(request, 'log_in.html', {'return_code':return_code})
        except IntegrityError:
            return_code = 2          # 用户名已存在
            return render(request, 'sign_up.html', {'return_code':return_code})
            
    return render(request, 'sign_up.html', {'return_code':return_code})


def log_in(request):   
    '''
    用户登录
    - url: /log_in
    - method: POST
    - 传入参数: username, passward
    - 返回值: 0-未操作, 1-成功，2-用户名不存在或密码错误，3-取回评论
    '''
    return_code = 0
    if request.method == 'POST':    
        # 从 POST 请求中获取用户名、密码参数   
        username = request.POST.get('username')        
        password = request.POST.get('password')        
          
        try:   
            # 验证用户名、密码是否正确
            user = auth.authenticate(username=username, password=password)   
            if user:            
                auth.login(request, user)   # 正确则登录   
                # 如果是超级用户，跳转到后台管理页面
                if user.is_superuser:
                    return redirect('/admin') 
                all_dish = Comments.objects.select_related('dish_id').all()
                all_dish = all_dish.order_by('?')[:8]
                return_code = 1
                return render(request, 'index.html', {'comment_data': all_dish,'return_code':return_code})
            else:
                raise auth.PermissionDenied
        except auth.PermissionDenied:       # 用户名不存在或密码错误
            return_code = 2
            return render(request, 'log_in.html', {'return_code':return_code})
    return render(request, "log_in.html", {'return_code':return_code})


def index(request):  
    '''
    主页
    - url: /index
    '''  
    # 主页评论展示
    return get_some_dish(request)

def get_some_dish(request):
    '''
    主页评论展示
    - url: /index
    - 返回值: 3-取回评论
    '''
    all_dish = Comments.objects.select_related('dish_id').all()
    # 随机取8条评论
    all_dish = all_dish.order_by('?')[:8]
    
    if request.user.is_authenticated:
        return render(request, 'index.html', {'comment_data': all_dish,'return_code':1})
    return render(request, 'index.html', {'comment_data': all_dish, 'return_code': 3})
    
def search(request):
    '''
    搜索界面
    - url: /search
    - method: GET
    - 传入参数: q, campus, cafeteria, served_time
    - 返回值: search_result, context
    '''
    # 获取所有校区、食堂、用餐时间，用于搜索界面的筛选
    campus_list = Campus.objects.all()
    cafeteria_list = Cafeteria.objects.all()
    served_time_list = ServedTime.objects.all()
    search_result = None
    if request.method == 'GET':
        query = request.GET.get('q', '')                        # 获取搜索的菜名
        campus = request.GET.getlist('campus', [])              # 获取筛选条件的校区
        cafeteria = request.GET.getlist('cafeteria', [])        # 获取筛选条件的食堂
        served_time = request.GET.getlist('served_time', [])    # 获取筛选条件的用餐时间

        # 构建查询条件
        filters = {}
        if query:   # 基于菜名的模糊查询
            filters['dish_name__icontains'] = query
        # if campus:
            # filters['campus_id'] = campus
            # cafeteria_list = Cafeteria.objects.filter(campus_id=campus)
        if len(cafeteria) > 0:      # 基于食堂的查询
            filters['cafeteria_id__in'] = cafeteria
            # served_time_list = ServedTime.objects.filter(cafeteria_id=cafeteria)
        if len(served_time) > 0:    # 基于用餐时间的查询
            filters['served_time_id__in'] = served_time

        # 执行查询
        search_result = Dish.objects.filter(**filters)
        
    context = {
        'campuses': campus_list,
        'cafeterias': cafeteria_list,
        'served_times': served_time_list,
    }
    
    return render(request, 'search.html', {'search_result': search_result, 'context': context})

def get_comments_by_dish_id(dish_id):
    '''菜品详情页-获取评论'''
    comments = Comments.objects.filter(dish_id=dish_id)
    return comments

def detail(request, dish_id):
    '''
    菜品详情页
    - url: /detail/<dish_id>
    - method: GET, POST
    - 传入参数: dish_id
    - 返回值: dish_info, dish_comments, return_code(0-GET方法, 1-评论成功，2-未登录，评论失败)
    '''
    return_code = 0
    # 获取菜品信息
    dish = Dish.objects.get(dish_id=dish_id)  
    dish_name = dish.dish_name
    dish_price = dish.dish_price
    dish_cafe = dish.cafeteria_id.cafeteria_name
    dish_served_time = dish.served_time_id.served_time_period
    dish_info = {'dish_id': '/static/images/Dish/'+str(int(float(dish_id)))+'.png','dish_name': dish_name, 'dish_price': dish_price, 'dish_cafe': dish_cafe, 'dish_served_time': dish_served_time}
    
    # 获取菜品评论
    dish_comments = get_comments_by_dish_id(dish_id)
    
    # 添加评论
    if request.method == 'POST':
        return_code = add_comment(request, dish_id)
        
    return render(request, 'detail.html', 
                  {'dish_info': dish_info, 'dish_comments': dish_comments, 'return_code': return_code})

def add_comment(request, dish_id):
    '''
    添加评论
    - url: /detail/<dish_id>
    - method: POST
    - 传入参数: dish_id
    - 返回值: 0-GET方法, 1-成功，2-未登录
    '''
    # 判断用户是否登录
    user = request.user
    if not user.is_authenticated:
        return 2
    username = user.username
    
    # 获取评论内容    
    score = request.POST.get('score')
    content = request.POST.get('content')
    dish = Dish.objects.get(dish_id=dish_id)
    
    # 获取当前最大的评论id（因为数据库的 comments_id 是 unique 的，且存储为 varchar）
    max_id = Comments.objects.all().aggregate(models.Max('comments_id'))['comments_id__max']
    next_id = int(float(max_id)) + 1
    # 创建评论
    comment = Comments.objects.create(comments_id=next_id, score=score, content=content, dish_id=dish, username_id=username)
    comment.save()
    return 1
    
def about_us(request):
    return render(request, 'about_us.html')

def get_comments_by_username(username):
    '''用户评论'''
    comments = Comments.objects.filter(username_id=username)
    return comments
    
def log_out(request): 
    '''登出
    '''   
    auth.logout(request)    
    all_dish = Comments.objects.select_related('dish_id').all()
    all_dish = all_dish.order_by('?')[:8]
    return render(request, 'index.html', {'comment_data': all_dish,'return_code':3})

def user_info(request):
    '''
    用户信息
    - url: /user_info
    - method: GET and POST
    '''
    username = request.user.username
    comments = get_comments_by_username(username)
    user_info = {'username': username, 'comments': comments}
    
    if request.method == 'POST':
        # 修改密码
        auth.logout(request)    
        all_dish = Comments.objects.select_related('dish_id').all()
        all_dish = all_dish.order_by('?')[:8]
        return redirect('log_in')
    else:
        return render(request, 'user_info.html', {'user_info': user_info})

    


                       
        
