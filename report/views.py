from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Server
# Create your views here.

class serverlist(ListView):
    model = Server
    paginate_by = 50
    context_object_name = "servers"
    template_name = "report/index.html"