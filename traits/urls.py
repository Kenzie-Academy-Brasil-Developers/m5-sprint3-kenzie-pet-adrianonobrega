from django.urls import path
from . import views

urlpatterns = [
    path("/traits/",views.TraitView.as_view()),
]