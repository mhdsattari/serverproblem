from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.serverlist.as_view(),name="server_list"),
    path('login',views.CustomLoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(next_page = 'login'),name="logout"),
    path('problem/<int:pkk>', views.problem.as_view(),name = "server_problem"),
    path('ServerCreate',views.ServerCreate.as_view(),name="server_create"),
    path('ServerUpdate/<int:pk>',views.ServerUpdate.as_view(),name="server_update"),
    path('<int:pk>',views.serversearch.as_view(),name="server_search")
]