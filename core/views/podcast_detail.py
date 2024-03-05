from django.shortcuts import get_object_or_404, render

from core.models import Podcast


def podcast_detail(request, slug):
    podcast = get_object_or_404(Podcast, slug=slug)
    context = {"podcast": podcast}
    return render(request, "podcast_detail.html", context)
