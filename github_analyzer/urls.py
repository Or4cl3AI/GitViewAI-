from django.urls import path
from analyzer.views import analyze_repository

urlpatterns = [
    path('', analyze_repository, name='analyze_repository'),
]