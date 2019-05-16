from django.db import models
from django.shortcuts import reverse

# Create your models here.

def generate_filename(instance, filename):
    return '{0}/{1}'.format(instance.slug, filename)

def generate_slider_filename(instance, filename):
    return '{0}/{1}'.format(instance.slug, 'slider_' + filename)

class About(models.Model):
    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информация"

    description = models.TextField(db_index=True, verbose_name="Описание")
    email_field = models.CharField(max_length=50, db_index=True, verbose_name="E-mail")
    address = models.CharField(max_length=50, db_index=True, verbose_name="Адрес")
    hall_rows_count = models.DecimalField(max_digits=2, decimal_places=0, verbose_name="Число рядов")
    hall_places_count = models.DecimalField(max_digits=2, decimal_places=0, verbose_name="Число мест в ряду")

class Movie(models.Model):
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    title = models.CharField(max_length=50, db_index=True, verbose_name="Название фильма")
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to=generate_filename, verbose_name="Превью")
    slider_image = models.ImageField(upload_to=generate_slider_filename, blank=True, verbose_name="Превью для слайдера")
    country = models.CharField(max_length=30, db_index=True, verbose_name="Страна производства")
    genre = models.CharField(max_length=50, verbose_name="Жанр")
    actors = models.CharField(max_length=200, verbose_name="Актерский состав")
    duration = models.CharField(max_length=20, verbose_name="Длительность")
    director = models.CharField(max_length=40, verbose_name="Режиссер")
    age = models.CharField(max_length=20, verbose_name="Возрастное ограничение")
    description = models.TextField(verbose_name="Описание")
    soon = models.BooleanField(default=False, verbose_name="Премьера")
    optional_desc = models.CharField(max_length=50, blank=True, verbose_name="Доп. информация для слайдера")

    def get_absolute_url(self):
        return reverse('movie_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class Comment(models.Model):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-comment_date"]

    comment_author = models.CharField(max_length=10, db_index=True, verbose_name="Имя автора")
    comment_text = models.TextField(db_index=True, verbose_name="Текст комментария")
    comment_film = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")
    comment_date = models.DateTimeField(auto_now_add=True)
    author_email = models.EmailField(max_length=75, verbose_name="Адрес электронной почты")

    def __str__(self):
        return '{0}/{1}'.format(self.comment_film.title, self.comment_author)


class Schedule(models.Model):
    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

    MOVIE_FORMATS = [
        ('4D', '4D'),
        ('IMAX', 'IMAX 3D'),
        ('3D', '3D'),
        ('2D', '2D')
    ]

    movie_date = models.DateTimeField(verbose_name="Дата фильма")
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Название фильма")
    movie_price = models.DecimalField(max_digits=4, decimal_places=0, verbose_name="Стоимость билета")
    movie_format = models.CharField(max_length=2, db_index=True, verbose_name="Формат фильма", choices = MOVIE_FORMATS)
    def save(self, *args, **kwargs):
        super(Schedule, self).save(*args, **kwargs) # Call the "real" save() method.
        about = About.objects.get(id=1)
        rows_count = int(about.hall_rows_count)
        places_count = int(about.hall_places_count)
        n_bd = 1
        for row in range(1, rows_count+1):
            for pl in range(1, places_count+1):
                new_place = Place.objects.create(
                    schedule = Schedule.objects.get(id=self.id),
                    hall_row = str(row),
                    hall_place = str(pl),
                    place_num = n_bd,
                    is_bought = False
                )
                new_place.save()
                n_bd += 1

    def __str__(self):
        return '{0}/{1}'.format(self.movie_name.title, self.movie_date)

    def get_absolute_url(self):
        return reverse('schedule_details_url', kwargs={'id': self.id})


class Place(models.Model):
    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name="Фильм", blank=True, null=True)
    hall_row = models.CharField(max_length=2, db_index=True, verbose_name="Ряд")
    hall_place = models.CharField(max_length=2, db_index=True, verbose_name="Место")
    place_num = models.DecimalField(max_digits=4, decimal_places=0, verbose_name="МестоБД")
    is_bought = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('buy_ticket_url', kwargs={'id': self.schedule.id, 'id_db':self.place_num})

    def __str__(self):
        return '{0}/{1}'.format(self.schedule.movie_name.title, self.schedule.movie_date)
