from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^survey$', views.index),
    url(r'^results$',views.results),
    url(r'^reset$', views.reset)   # This line has changed! Notice that urlpatterns is a list, the comma is in
]