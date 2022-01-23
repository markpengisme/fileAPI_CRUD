from django.urls import path
from . import views

urlpatterns = [
    path('<path:localSystemFilePath>', views.restfulAPI, name='file'),
    path('', views.restfulAPI)
]
