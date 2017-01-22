from django.http import HttpResponse

def index(request):
	return HttpResponse("The travelator")

# Create your views here.
