# Generated by Django 4.1.1 on 2022-10-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('upload', models.ImageField(upload_to=None)),
                ('surname', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('year_of_birth', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('postcode', models.IntegerField()),
                ('town', models.CharField(max_length=50)),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]