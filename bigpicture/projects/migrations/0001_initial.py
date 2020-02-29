# Generated by Django 3.0.3 on 2020-02-29 16:45

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(error_messages={'unique': 'Користувач з таким імейлом вже існує'}, max_length=254, unique=True, verbose_name='Імейл')),
                ('username', models.CharField(blank=True, max_length=150, verbose_name='Юзернейм')),
                ('first_name', models.CharField(max_length=30, verbose_name="Ім'я")),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Прізвище')),
                ('phone', models.CharField(blank=True, default='', max_length=30, verbose_name='Телефон')),
                ('avatar', models.ImageField(blank=True, max_length=200, upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Користувач',
                'verbose_name_plural': 'Користувачі',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва департаменту')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, max_length=200, upload_to='', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Департамент',
                'verbose_name_plural': 'Департаменти',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва системи')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('slug', models.SlugField(max_length=200)),
                ('departments', models.ManyToManyField(to='projects.Department', verbose_name='Департаменти')),
            ],
            options={
                'verbose_name': 'Система',
                'verbose_name_plural': 'Системи',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва проєкту')),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Опис проєкту')),
                ('kind', models.CharField(choices=[('it', 'IT-проект'), ('legislative', 'Підзаконні акти')], max_length=20, verbose_name='Тип проєкту')),
                ('image', models.ImageField(blank=True, max_length=200, upload_to='', verbose_name='Картинка')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='Дедлайн')),
                ('departments', models.ManyToManyField(to='projects.Department', verbose_name='Департаменти')),
                ('responsible_persons', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Відповідальні')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.System', verbose_name='Система')),
            ],
            options={
                'verbose_name': 'Проєкт',
                'verbose_name_plural': 'Проєкти',
            },
        ),
    ]
