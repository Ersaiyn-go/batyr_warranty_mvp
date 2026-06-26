#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py shell <<'PY'
import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = (os.environ.get("DJANGO_SUPERUSER_USERNAME") or "admin").strip()
email = (os.environ.get("DJANGO_SUPERUSER_EMAIL") or "").strip()
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

print("DJANGO_SUPERUSER_USERNAME =", repr(username))
print("DJANGO_SUPERUSER_EMAIL =", repr(email))

if username and password:
    user, created = User.objects.get_or_create(username=username)

    user.email = email
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.set_password(password)
    user.save()

    print("Superuser created or updated")
    print("Username in database:", repr(user.username))
    print("Is staff:", user.is_staff)
    print("Is superuser:", user.is_superuser)
    print("Is active:", user.is_active)
else:
    print("Superuser environment variables are not set")
PY