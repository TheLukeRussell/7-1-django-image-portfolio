from django.views.generic import TemplateView
from .models import Image

class Images(TemplateView):
    template_name = 'images.html'

    def get_context_data(self, **kwargs):
        images = Image.objects.all()

        context = {
            'images': images
        }

        return context