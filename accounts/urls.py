from django.urls import path

from accounts.views import PodcastLoginView, RegisterView, logout_view

urlpatterns = [
    path('ingresar/', PodcastLoginView.as_view(), name="ingresar"),
    path('salir/', logout_view, name="salir"),
    path('registrar/', RegisterView.as_view(), name="registrar")
]
