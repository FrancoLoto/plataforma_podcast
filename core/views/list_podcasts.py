from django.shortcuts import render

from core.models import Podcast


def list_podcasts(request):
    podcasts = Podcast.objects.all()
    return render(request, "list_podcasts.html",
                  context={"podcasts": podcasts})
