# Generated by Django 2.2 on 2019-05-06 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_comment_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.CharField(db_index=True, max_length=10, verbose_name='Имя автора'),
        ),
    ]
