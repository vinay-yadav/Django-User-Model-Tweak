# Django-User-Model-Tweak

# Adding Custom Fields to Django-Default-User-Model

1. Create a new app
2. In models.py of new app, create a new User model and extend the 'AbstrctUser' class from 'from django.contrib.auth.models import AbstractUser'
3. Changing User model on admin page, register 'User' model with 'UserAdmin' from 'from django.contrib.auth.admin import UserAdmin'
4. Add "AUTH_USER_MODEL = 'users.User'" in settings.py


install iPython => 'pip install ipython' to get conda interactive shell.
