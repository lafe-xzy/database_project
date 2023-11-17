from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.models import User

'''用户注册'''
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passward = request.POST.get('password')
        user = User.objects.create_user(username=username, password=passward)
        user.save()
        if user:
            auth.login(request, user)
            return redirect('login')    #注册成功后跳转至登录
    return render(request, 'register.html')

'''用户登录'''
def login(request):    
    if request.method == 'POST':        
        username = request.POST.get('username')        
        password = request.POST.get('password')        
        user = auth.authenticate(username=username, password=password)        
        if user:            
            auth.login(request, user)   # 登录    
            return redirect('index')    # 登录成功后跳转至主页
    return render(request, "login.html")

'''主页'''
def index(request):    
    name = request.user.username    
    password = request.user.password    
    return render(request, 'index.html', {'name':name})
