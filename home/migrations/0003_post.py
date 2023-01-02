# Generated by Django 3.2.5 on 2023-01-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('date', models.DateField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='')),
                ('text', models.TextField()),
            ],
        ),
    ]