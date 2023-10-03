from typing import Annotated, Any
from urllib import request
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# from django.contrib.auth.decorators import permission_required
from django.db.models import Count
from .models import Server,Problem
from django.contrib.auth.views import LoginView

# Login 
class CustomLoginView(LoginView):
    template_name="report/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

# Servers List
class ServerList(LoginRequiredMixin,ListView):
    model = Server
    # permission_required = 'sd'
    paginate_by = 50
    context_object_name = "Servers"
    template_name = "report/Servers.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Servers'] = Server.objects.filter(user = self.request.user).annotate(problemcount=Count('problem')).order_by('-problemcount')
        filter_value = self.request.GET.get('server') or ''
        context['filter_value'] = filter_value
        if filter_value:
            context['Servers'] = context['Servers'].filter(title__startswith=filter_value)
        return context

# Server Create
class ServerCreate(LoginRequiredMixin,CreateView):
    model = Server
    fields = ["title","description","server_type"]
    template_name = "report/ServerCreate.html"
    success_url = reverse_lazy("server_list")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Server Update
class ServerUpdate(LoginRequiredMixin,UpdateView):
    model = Server
    fields = ["title","description","server_type"]
    template_name = "report/ServerUpdate.html"
    success_url = reverse_lazy("server_list")
    def form_valid(self, form):
        if form.instance.user==self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse("does not equal!!!")
        
# Server Search
# class ServerSearch(DetailView):
#     model = Server
#     context_object_name = 'server'
#     template_name = "report/server.html"
#     def get_queryset(self):
#         return super().get_queryset().filter(user = self.request.user)
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['problemcount'] = Problem.objects.filter(user = self.request.user,server = self.request.resolver_match.kwargs['pk']).count()
#         return context

# Problem
class ProblemList(LoginRequiredMixin,ListView):
    model = Problem
    paginate_by=50
    context_object_name = "Problems"
    template_name = "report/Problems.html" 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Problems'] = Problem.objects.filter(server=self.request.resolver_match.kwargs['pkk'])
        filter_value = self.request.GET.get('problem') or ''  
        if filter_value:
            context['Problems'] = context['Problems'].filter(title__startswith=filter_value)
        print(context['Problems'])
        context['filter_value'] = filter_value
        myserver = Server.objects.get(id=self.request.resolver_match.kwargs['pkk'])
        context["server"] = f"{myserver.user} | {myserver.title} | {myserver.description} \
        | {myserver.get_server_type_display()} | {myserver.createdate} | {myserver.updatedate}"
        return context

# Problem Create
class ProblemCreate(LoginRequiredMixin,CreateView):
    model = Problem
    fields = ["server","title","description","problem_type"]
    template_name = "report/ProblemCreate.html"
    # print(request.GET.get('next'))
    # nextt = request.GET.get('next')
    success_url = reverse_lazy("server_list")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Server Update
class ProblemUpdate(LoginRequiredMixin,UpdateView):
    model = Problem
    fields = ["title","description","problem_type"]
    template_name = "report/ProblemUpdate.html"
    success_url = reverse_lazy("server_list")
    def form_valid(self, form):
        if form.instance.user==self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse("does not equal!!!")
 
