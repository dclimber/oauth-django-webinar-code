# Generated by Django 3.1.7 on 2021-03-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Фамилия')),
                ('bio', models.TextField(blank=True, default='', verbose_name='Биография')),
                ('photo_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на фото')),
            ],
            options={
                'verbose_name': 'Поэт(эсса)',
                'ordering': ('first_name',),
            },
        ),
    ]