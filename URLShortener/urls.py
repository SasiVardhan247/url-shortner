from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('shorten/', shorten_url),
    path('redirect/<slug:custom_name>', redirect_url),
    path('all-analytics',all_analytics),
]