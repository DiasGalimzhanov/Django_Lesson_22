from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import Book, Car
from .forms import BookForm, CarForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

class ListCar(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'

class CreateCar(SuccessMessageMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')
    success_message = 'Объявление успешно создана'

class UpdateCar(SuccessMessageMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'update.html'
    success_url = reverse_lazy('home')
    success_message = 'Объявление успешно обновлено'

class DeleteCar(DeleteView):
    model = Car
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class DetailCar(DetailView):
    model = Car
    template_name = 'detail.html'

class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')

class Logout(LogoutView):
    next_page = reverse_lazy('home')

















#def home(request):
    # response = HttpResponse("Hello, world. You're at the app index.")
    # if 'conter' in request.COOKIES:
    #     cnt = int(request.COOKIES['conter']) + 1
    # else:
    #     cnt = 1
    # response.set_cookie(key = 'conter', value = cnt, max_age=60)
    # if request.COOKIES['conter'] == '10':
    #     response.delete_cookie('conter')
    # return response
