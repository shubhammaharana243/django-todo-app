import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a Django superuser from environment variables"

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not all([username, email, password]):
            self.stdout.write("Superuser variables not configured.")
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write("Superuser already exists.")
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write(self.style.SUCCESS("Superuser created."))