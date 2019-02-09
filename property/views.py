from django.shortcuts import render
from .models import Property

# Create your views here.
def property_view(request):
    properties =Property.objects.all()
    print(properties)
    context = {
    	'properties': properties

    }
    return render(request, 'main/property.html', context)