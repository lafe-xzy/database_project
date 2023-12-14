## 安装依赖
```
pip install -r requirements.txt
```

## 运行方法

1. 虚拟机运行 opengauss 数据库，记录 IP 和端口
2. 修改 database_project/settings.py 中的 `HOST` 和 `PORT` 为对应 IP 和端口
    ```python
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': BASE_DIR / 'db.sqlite3',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'project',
            'USER': 'lafe',
            'PASSWORD': 'lafe@123',
            'HOST': '192.168.232.147',
            'PORT': '7654',
        }
    }
    ```
2. 运行
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
    ```
2. 同一局域网下访问：主机 IP + 端口，如 172.26.xx.xx:8000




## Notice!
1. Django 版本不可以太高，由于 OpenGauss 内置的 Postgres 版本较低（9.2.4），较高版本的 Django 不支持。
2. 管理员：lafe(123)
3. 测试用户：21307169(xzy12345), 21307177(kjx12345), 21307275(xjw12345)
