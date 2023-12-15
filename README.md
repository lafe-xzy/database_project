## 安装依赖
```
pip install -r requirements.txt
```

## 运行方法

1. 虚拟机运行 opengauss 数据库并创建连接，记录 IP 和端口
    ```shell
    su - opengauss
    gsql -d postgres -r
    ```
2. 登录 opengauss 创建管理员，以用户名为 lafe 为例
    ```shell
    create user lafe with password 'lafe@123';
    alter user lafe sysadmin;
    \c - lafe
    ```
3. 创建数据库
    ```python
    create database project;
    ```
4. 修改 database_project/settings.py 中的 `HOST` 和 `PORT` 为对应 IP 和端口
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
5. 数据库迁移
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```
6. 使用 Data Studio 导入 static/data 目录下的数据
7. 运行
    ```shell
    python manage.py runserver
    ```




## 注意
1. Django 版本不可以太高，由于 OpenGauss 内置的 Postgres 版本较低（9.2.4），较高版本的 Django 不支持。
2. 管理员：lafe(123)
3. 测试用户：21307169(xzy12345), 21307177(kjx12345), 21307275(xjw12345)
