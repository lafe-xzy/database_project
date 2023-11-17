## 安装依赖
```
pip install -r requirements.txt
```

## 运行方法

1. 运行
    ```
    python manage.py runserver 0.0.0.0:8000
    ```
2. 同一局域网下访问：主机 IP + 端口，如 172.26.xx.xx:8000

运行成功可以看到 Hello World!


## Notice!
1. Django 版本不可以太高，由于 OpenGauss 内置的 Postgres 版本较低（9.2.4），较高版本的 Django 不支持。
2. Bug: 创建超级用户时没有提示输入 firstname 和 lastname 但是 auth_user 表中这二者不能为 Null，导致创建失败。通过 Data Studio 登录数据库后手动修改二者可以为 Null，成功创建用户。(superusername: lafe password: 123)