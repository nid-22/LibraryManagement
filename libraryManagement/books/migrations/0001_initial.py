# Generated by Django 3.2.5 on 2021-08-25 08:00

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
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('CoverPage', models.ImageField(upload_to='Covers/')),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('CreatedOn', models.DateTimeField(auto_now_add=True)),
                ('UpdatedOn', models.DateTimeField(auto_now=True, null=True)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
                ('CreatedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BookCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('UpdatedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BookUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]