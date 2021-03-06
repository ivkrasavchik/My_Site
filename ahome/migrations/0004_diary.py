# Generated by Django 2.1.5 on 2019-01-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahome', '0003_chapter_numer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.TextField(blank=True, default=None, max_length=256, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
            },
        ),
    ]
