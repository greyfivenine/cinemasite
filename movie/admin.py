from django.contrib import admin

from .models import Movie, About, Comment, Schedule, Place
from .forms import AdminScheduleForm
# Register your models here.

class CommentFilter(admin.SimpleListFilter):
    title = 'Фильм'
    parameter_name = 'movie_slug'

    def lookups(self, request, model_admin):
        movies = set([movie for movie in Movie.objects.filter(soon=False)])
        return [(m.slug, m.title) for m in movies]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(comment_film__slug__iexact=self.value())

class PlaceFilter(admin.SimpleListFilter):
    title = 'Фильм'
    parameter_name = 'movie_slug'

    def lookups(self, request, model_admin):
        movies = set([movie for movie in Movie.objects.filter(soon=False)])
        return [(m.slug, m.title) for m in movies]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(schedule__movie_name__slug__iexact=self.value())

class ScheduleInline(admin.TabularInline):
    model = Schedule

class PlaceInline(admin.TabularInline):
    model = Place

class MovieAdmin(admin.ModelAdmin):
    class Meta:
        model = Movie

    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'country', 'genre', 'duration', 'soon']
    inlines = [
        ScheduleInline,
    ]

class CommentAdmin(admin.ModelAdmin):
    class Meta:
        model = Comment

    list_display = ['comment_author', 'comment_film', 'comment_date']
    list_filter = (CommentFilter, 'comment_author',)

class ScheduleAdmin(admin.ModelAdmin):
    class Meta:
        model = Schedule

    form = AdminScheduleForm
    list_display = ['movie_name', 'movie_date', 'movie_price', 'movie_format']
    inlines = [
        PlaceInline,
    ]

class PlaceAdmin(admin.ModelAdmin):
    class Meta:
        model = Place

    # list_filter = ['schedule__movie_name__title', 'hall_row', 'hall_place']
    list_filter = (PlaceFilter, 'hall_row', 'hall_place',)
    search_fields = ['schedule__movie_name__title', '=hall_row', '=hall_place']
    list_display = ['get_movie_name', 'get_movie_date', 'hall_row', 'hall_place', 'is_bought']

    def get_movie_name(self, obj):
        return obj.schedule.movie_name.title

    def get_movie_date(self, obj):
        return obj.schedule.movie_date

admin.site.register(Movie, MovieAdmin)
admin.site.register(About)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Place, PlaceAdmin)
