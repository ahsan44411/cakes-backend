from django.urls import path

from api.views import *

app_name = 'api'

urlpatterns = [
    path('cake/', CakeList.as_view()),
    path('cake/<int:pk>/', CakeDetail.as_view())
]
