# Generated by Django 3.2.9 on 2021-11-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='participant',
            fields=[
                ('Pre', models.TextField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=300)),
                ('Email', models.CharField(max_length=300)),
            ],
        ),
    ]
