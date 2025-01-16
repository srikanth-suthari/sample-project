# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("run-script/", views.web_automation, name="web_automation"),
]
