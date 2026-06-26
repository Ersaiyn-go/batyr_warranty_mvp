import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create or update admin user from environment variables'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not username or not password:
            self.stdout.write(
                self.style.WARNING(
                    'Admin was not created: DJANGO_SUPERUSER_USERNAME or DJANGO_SUPERUSER_PASSWORD is missing.'
                )
            )
            return

        User = get_user_model()

        user, created = User.objects.get_or_create(username=username)
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f'Admin user "{username}" created.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Admin user "{username}" updated.'))