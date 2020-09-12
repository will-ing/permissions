# Permissions

1. docker compose up
2. docker compose down
3. `docker-compose help` - see commands
4. Change Postgres in settings.py

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

1. ```t
   poetry add psycopg2-binary
   ```

2. ```t
    poetry export -f requirements.txt -o requirements.txt
    ```

3. ```t
    docker-compose up --build
    ```

4. ```t
    docker-compose exec web python manage.py migrate
    ```

5. ```t
    docker-compose exec web python manage.py createsuperuser
    ```

6. rm db.sqlite3 from dir if exists
7. touch permissions.py

8. ```py
    from rest_framework import permissions


    class IsAuthorOrReadOnly(permissions.BasePermission):

        def has_object_permission(self, request, view, obj):

            if request.method in permissions.SAFE_METHODS:
                return True

            return obj.author == request.user
    ```

9. ```py
    # in setting.py
    ALLOWED_HOSTS = ['0.0.0.0']
    ```
    