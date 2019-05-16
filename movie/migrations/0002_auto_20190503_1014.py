# Generated by Django 2.2 on 2019-05-03 05:14

from django.db import migrations, models
import movie.models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to=movie.models.generate_filename),
        ),
    ]
