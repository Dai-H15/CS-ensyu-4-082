# Generated by Django 4.2.7 on 2023-12-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0003_rename_customdata_customusermodel_customdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitymodel',
            name='community_Key',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='custom_user_key',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]