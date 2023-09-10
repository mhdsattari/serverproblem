from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Server,Problem

class serverlist(ListView):
    model = Server
    paginate_by = 50
    context_object_name = "servers"
    template_name = "report/index.html"
    

class serverproblem(ListView):
    model = Problem
    context_object_name = "problems"
    template_name = "report/problem.html"
    def get_queryset(self):
        return Problem.objects.filter(server=self.request.resolver_match.kwargs['pkk'])
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        myserver = Server.objects.get(id=self.request.resolver_match.kwargs['pkk'])
        context["server"] = f"{myserver.user} | {myserver.title} | {myserver.description} \
        | {myserver.get_server_type_display()} | {myserver.createdate} | {myserver.updatedate}"
        return context
    