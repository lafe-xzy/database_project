## 安装依赖
```
pip install -r requirements.txt
```

## 运行方法

1. 虚拟机运行 opengauss 数据库
2. 运行
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
    ```
2. 同一局域网下访问：主机 IP + 端口，如 172.26.xx.xx:8000




## Notice!
1. Django 版本不可以太高，由于 OpenGauss 内置的 Postgres 版本较低（9.2.4），较高版本的 Django 不支持。
