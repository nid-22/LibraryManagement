# Generated by Django 3.2.5 on 2021-08-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_books_coverpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='CoverPage',
            field=models.ImageField(blank=True, null=True, upload_to='Covers/'),
        ),
    ]
