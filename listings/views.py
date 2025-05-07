from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    #Fetch from database
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) # display the latest listing

    # Pagination
    paginator = Paginator(listings, 3) # 3 number of listing we want per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    # send it as dict
    context = {
    'listings': paged_listings
  }
    return render(request, 'listings/listings.html', context) # pass the data

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')