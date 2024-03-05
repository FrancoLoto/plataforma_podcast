from django.shortcuts import render

from core.models import Podcast


def home(request):
    podcasts = Podcast.objects.all()[:3]
    return render(request, "index.html", context={"podcasts": podcasts})
