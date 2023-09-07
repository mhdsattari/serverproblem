from django.urls import path
from . import views

urlpatterns = [
    path('',views.serverlist.as_view(),name="server_list"),
]