# Generated by Django 4.2.7 on 2023-12-14 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityModel',
            fields=[
                ('community_name', models.CharField(max_length=30)),
                ('community_Key', models.CharField(max_length=33, primary_key=True, serialize=False)),
                ('introduce', models.CharField(max_length=300)),
                ('is_RegistByEmail', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('custom_user_Name', models.CharField(max_length=50)),
                ('custom_user_key', models.CharField(max_length=33, primary_key=True, serialize=False)),
                ('Community', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customUser.communitymodel')),
                ('PersonalData', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.personaldata')),
            ],
        ),
    ]
