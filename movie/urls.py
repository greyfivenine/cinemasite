from django.urls import path

from .views import *

urlpatterns = [
    path('about/', get_info, name='get_info_url'),
    path('', get_movies_list, name='movies_list_url'),
    path('movie/schedule/', get_schedule, name='schedule_list_url'),
    path('movie/<str:slug>/addcomment', add_comment, name='add_comment_url'),
    path('movie/<str:slug>/', MovieDetail.as_view(), name='movie_details_url'),
    path('movie/schedule/<id>/buyticket/<id_db>', BuyTicket.as_view(), name='buy_ticket_url'),
    path('movie/schedule/<id>/', get_places_list, name='schedule_details_url'),
]
