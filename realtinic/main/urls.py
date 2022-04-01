from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('listing', views.listing, name='listing'),
    path('add-listing', views.addlisting, name='Add listing'),
    path('find-agent', views.findagents, name='Find Agents'),
    path('help', views.help, name='Help'),
    path('blog', views.blog, name='Blog'),
]