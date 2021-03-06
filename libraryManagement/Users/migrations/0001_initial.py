# Generated by Django 3.2.5 on 2021-08-25 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], max_length=1, null=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('BirthDate', models.DateField(null=True)),
                ('Phone', models.CharField(blank=True, max_length=10, null=True)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('CreatedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='UserCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('UpdatedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='UserUpdatedBy', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
