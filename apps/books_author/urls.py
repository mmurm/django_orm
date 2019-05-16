from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$',views.index),
    url(r'^authors$',views.authors),
    url(r'^books/(?P<book_id>\d+)$',views.book),
    url(r'^authors/(?P<author_id>\d+)$',views.author),
    url(r'^process_book$',views.process_book),
    url(r'^process_author$',views.process_author),
    url(r'^update_book/(?P<b_id>\d+)$',views.update_book),
    url(r'^update_author/(?P<a_id>\d+)$',views.update_author),
]