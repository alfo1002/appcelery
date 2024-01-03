from django.urls import path
from .views import slowResponseView

urlpatterns = [
    path('correr', slowResponseView, name='correr')
]
