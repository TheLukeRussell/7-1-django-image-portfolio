from django.http import HttpResponse

def home_page(request):
    return HttpResponse('You made it to the home page!')