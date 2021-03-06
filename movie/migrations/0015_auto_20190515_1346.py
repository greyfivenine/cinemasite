# Generated by Django 2.2 on 2019-05-15 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0014_auto_20190512_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie', verbose_name='Фильм'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(max_length=200, verbose_name='Актерский состав'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='age',
            field=models.CharField(max_length=20, verbose_name='Возрастное ограничение'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=40, verbose_name='Режиссер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=20, verbose_name='Длительность'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=50, verbose_name='Жанр'),
        ),
    ]
