# Generated by Django 4.2.7 on 2024-01-10 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0001_initial'),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customUser.communitymodel'),
        ),
    ]
