from django.urls import path
from . import views

# /listing/23

urlpatterns = [
    path('', views.index, name='listings'), # '' means '/listings' 
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]