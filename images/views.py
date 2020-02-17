from django.views.generic import ListView
from .models import Image

class HomePageView(ListView):
    model = Image
    template_name = 'home.html'