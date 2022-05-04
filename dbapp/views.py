from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination


from travello.models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name= 'Bali'
    
    return render(request, 'index.html', {'dest1':dest1.name})

