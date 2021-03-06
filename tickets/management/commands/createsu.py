from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
  help = 'Creates a super user'

  def handle(self, *args, **options):
    if not User.objects.filter(is_staff=True, is_superuser=True).exists():
      User.objects.create_superuser(
        'admin', 'admin@admin.com', 'adminpass', first_name='Admin'
      )
