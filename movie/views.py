from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.utils import timezone

from .models import Movie, About, Schedule
from .forms import CommentForm, BuyTicketForm
from .utils import ObjectDetailMixin

# Create your views here.

class MovieDetail(ObjectDetailMixin, View):
    model = Movie
    template = 'movie/movie_detail.html'
    form = CommentForm

class BuyTicket(View):
    def get(self, request, id, id_db):
        form = BuyTicketForm()
        sc = Schedule.objects.get(id=id)
        place = sc.place_set.get(place_num=id_db)
        return render(request, 'movie/buyticket.html', context={'form':form, 'sc':sc, 'place':place})

    def post(self, request, id, id_db):

        sc = Schedule.objects.get(id=id)
        place = sc.place_set.get(place_num=id_db)
        r = request.POST.copy()
        r['is_bought'] = place.is_bought

        bound_form = BuyTicketForm(r)

        if bound_form.is_valid():
            place.is_bought = True
            place.save()
            return redirect(sc)
        return render(request, 'movie/buyticket.html', context={'form':bound_form, 'sc':sc, 'place':place})

def add_comment(request, slug):
    bound_form = CommentForm(request.POST)
    if request.method == "POST" and ('pause' not in request.session):
        movie = Movie.objects.get(slug__iexact=slug)
        if bound_form.is_valid():
            comment = bound_form.save(commit=False)
            comment.comment_film = movie
            comment.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
            return redirect(Movie.objects.get(slug__iexact=slug))
        return render(request, 'movie/movie_detail.html', context={'movie':Movie.objects.get(slug__iexact=slug), 'form':bound_form})
    return render(request, 'movie/movie_detail.html', context={'movie':Movie.objects.get(slug__iexact=slug), 'form':bound_form})

def get_movies_list(request):
    movies_list = Movie.objects.filter(soon=False)
    soon_list = Movie.objects.filter(soon=True)
    page = "m_list"
    return render(request, 'movie/index.html', context={'movies':movies_list, 'soon':soon_list, 'page':page})

def get_schedule(request):
    movies_list = Movie.objects.filter(soon=False)
    page = "sc"
    time_now = timezone.now()
    return render(request, 'movie/schedule.html', context={'movies':movies_list, 'page':page, 'time':time_now})

def get_info(request):
    info = About.objects.get(id=1)
    page = "about"
    return render(request, 'movie/about.html', context={'info':info, 'page':page})

def get_places_list(request, id):
    info = About.objects.get(id=1)
    n_rows = int(info.hall_rows_count)
    sc = Schedule.objects.get(id=id)

    d = {}

    for i in range(1, n_rows + 1):
        d[str(i)] = sc.place_set.filter(hall_row=str(i))

    return render(request, 'movie/places_list.html', context={'sc':sc, 'hall':d})
