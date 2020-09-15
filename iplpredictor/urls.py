from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name = 'home'),
    path("predicted_score", views.score, name = 'score'),
]