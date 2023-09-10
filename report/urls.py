from django.urls import path
from . import views

urlpatterns = [
    path('',views.serverlist.as_view(),name="server_list"),
    path('problem/<int:pkk>', views.serverproblem.as_view(),name = "server_problem"),
    path('ServerCreate',views.ServerCreate.as_view(),name="server_create")    ,
    path('ServerUpdate/<int:pk>',views.ServerUpdate.as_view(),name="server_update")    
]