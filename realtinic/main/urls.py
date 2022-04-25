from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('listing', views.listing, name='listing'),
    path('add-listing', views.addlisting, name='Add listing'),
    path('find-agent', views.findagents, name='Find Agents'),
    path('find-agency', views.findagency, name='Find Agency'),
    path('help', views.help, name='Help'),
    path('blog', views.blog, name='Blog'),
    path('privacy-policy', views.privacy_policy, name='Privacy Policy'),
    path('about', views.about, name='About'),
    path('download', views.download, name='Download'),
    path('terms-of-use', views.terms, name='Terms of Use'),
]