from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.db.models import Count
from .models import Server,Problem

class serversearch(DetailView):
    model = Server
    context_object_name = 'server'
    template_name = "report/server.html"
    def get_queryset(self):
        print ('5555555555555555555555555555555')
        return Server.objects.get(id=self.request.resolver_match.kwargs['serverip'])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['server'] = Server.objects.get(id=self.request.resolver_match.kwargs['serverip'])
        return context
    
class serverlist(LoginRequiredMixin,ListView):
    model = Server
    paginate_by = 50
    context_object_name = "servers"
    template_name = "report/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servers'] = Server.objects.filter(user = self.request.user).annotate(problemcount=Count('problem')).order_by('-problemcount')
        return context
    

class problem(LoginRequiredMixin,ListView):
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

class ServerCreate(LoginRequiredMixin,CreateView):
    model = Server
    fields = "__all__"
    template_name = "report/ServerCreate.html"
    success_url = reverse_lazy("server_list")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ServerUpdate(LoginRequiredMixin,UpdateView):
    model = Server
    fields = "__all__"
    template_name = "report/ServerUpdate.html"
    success_url = reverse_lazy("server_list")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)