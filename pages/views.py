from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] # [:3] --> we only want 3 listings

    context = {
        'listings': listing
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    

    # set it to dict
    context = {
        'realtors' : realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)