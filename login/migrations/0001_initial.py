# Generated by Django 4.2.7 on 2023-12-06 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('FirstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('birth', models.DateField(default='1990-01-01')),
                ('phone', models.CharField(max_length=20)),
                ('user_key', models.CharField(max_length=33)),
                ('email', models.EmailField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]