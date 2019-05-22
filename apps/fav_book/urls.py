from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^books$',views.books),
    url(r'^books/(?P<book_id>\d+)$',views.book),
    url(r'^add_book$',views.add_book),
    url(r'^books/(?P<book_id>\d+)/add_to_fav$',views.add_to_fav),
    url(r'^books/(?P<book_id>\d+)/delete$',views.delete),
    url(r'^logout$',views.logout),
]