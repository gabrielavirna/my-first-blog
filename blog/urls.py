from django.conf.urls import url
from . import views

# we're importing Django's function url and all of our views from the blog application.
# add our first URL pattern; we're now assigning a view called post_list to the ^$ URL
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

