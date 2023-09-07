from django.urls import path
from . import views

urlpatterns = [
    path('',views.serverlist.as_view(),name="server_list"),
    path('problem/<int:pk>', views.serverproblem.as_view(),name = "server_problem")
]