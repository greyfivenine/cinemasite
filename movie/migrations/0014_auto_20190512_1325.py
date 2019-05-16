# Generated by Django 2.2 on 2019-05-12 08:25

from django.db import migrations, models
import movie.models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_auto_20190511_1104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AddField(
            model_name='movie',
            name='optional_desc',
            field=models.CharField(blank=True, max_length=50, verbose_name='Доп. информация для слайдера'),
        ),
        migrations.AddField(
            model_name='movie',
            name='slider_image',
            field=models.ImageField(blank=True, upload_to=movie.models.generate_slider_filename, verbose_name='Превью для слайдера'),
        ),
        migrations.AddField(
            model_name='movie',
            name='soon',
            field=models.BooleanField(default=False, verbose_name='Премьера'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='is_bought',
            field=models.BooleanField(default=True),
        ),
    ]
