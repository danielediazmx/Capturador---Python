from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.dashboard.forms import UserinfoForm
from apps.userinfo.models import Userinfo


class UsersList(ListView):
    model = Userinfo
    template_name = 'admin/index.html'
    context_object_name = 'users'
    paginate_by = 10
    queryset = Userinfo.objects.all()


class UsersCreate(CreateView):
    model = Userinfo
    form_class = UserinfoForm
    template_name = 'admin/form.html'
    success_url = reverse_lazy('userinfo-index')


class UsersUpdate(UpdateView):
    model = Userinfo
    form_class = UserinfoForm
    template_name = 'admin/form.html'
    success_url = reverse_lazy('userinfo-index')


class UsersDelete(DeleteView):
    model = Userinfo
    template_name = 'admin/delete.html'
    success_url = reverse_lazy('userinfo-index')


def redirector(request):
    return redirect('userinfo-index')
