from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$',views.index),
    url(r'^process_dojo$',views.process_dojo),
    url(r'^process_ninja$',views.process_ninja),
]