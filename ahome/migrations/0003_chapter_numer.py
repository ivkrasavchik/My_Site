# Generated by Django 2.1.5 on 2019-01-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahome', '0002_book_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='numer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
