from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Login
    path('login',views.CustomLoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(next_page = 'login'),name="logout"),

    # Server
    path('',views.ServerList.as_view(),name="server_list"),
    path('ServerCreate',views.ServerCreate.as_view(),name="server_create"),
    path('ServerUpdate/<int:pk>',views.ServerUpdate.as_view(),name="server_update"),
    # path('<int:pk>',views.ServerSearch.as_view(),name="server_search"),

    # Problem
    path('Problems/<int:pkk>', views.ProblemList.as_view(),name = "problem_list"),
    path('ProblemCreate', views.ProblemCreate.as_view(),name = "problem_create"),
    path('ProblemUpdate/<int:pk>', views.ProblemUpdate.as_view(),name = "problem_update"),
    
]