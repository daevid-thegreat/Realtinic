from django.urls import path
from . import views

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('listing', views.listing, name='listing'),
    path('add-listing/', views.addlisting, name='Add listing'),
    path('edit-listing/<str:id>', views.editlisting, name='Edit listing'),
    path('find-agent', views.findagents, name='Find Agents'),
    path('agents', views.agents, name='Agents'),
    path('agents/<str:id>', views.user_single, name='Agents Profile'),
    path('find-agency', views.findagency, name='Find Agency'),
    path('help', views.help, name='Help'),
    path('blog', views.blog, name='Blog'),
    path('listing/<str:id>', views.single_listing, name= 'single listing'),
    path('privacy-policy', views.privacy_policy, name='Privacy Policy'),
    path('about', views.about, name='About'),
    path('download', views.download, name='Download'),
    path('terms-of-use', views.terms, name='Terms of Use'),
    path('signin', views.signin, name='Sign In'),
    path('my-dashboard', views.dashboard, name='Agent Dashboard'),
    path('my-messages', views.message, name='Messages'),
    path('my-listings', views.my_listings, name='My Listings'),
    path('compare', views.compare, name='Compare'),
    path('terms', views.terms, name='Terms and Condition'),
    path('privacy_policy', views.privacy_policy, name='Privacy Policy'),
    path('my-profile', views.user_profile, name='my-profile'),
    path('register-agent', views.register_agents, name='register agent'),
    path('my-reviews', views.reviews, name='My Reviews'),
    path('my-bookings', views.bookings, name='My Bookings'),
    path('logout', views.logout, name='Log Out'),
    path('my-messages/<str:room_name>', views.chat, name='chat'),
    path('saved-homes', views.saved_homes, name='Saved Homes'),
    # path('agent-signin', views.agent_signin, name='Sign In Agent'),
]

