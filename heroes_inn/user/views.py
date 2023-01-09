from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView, TemplateView, CreateView
from .forms import LoginForm


# Create your views here.

class LoginView(View):

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect(to='home-page')

        form = LoginForm()
        context = {'form': form}
        return render(request, 'user/login.html', context=context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(self.request, 'Такой пользователь не существует')

            user = authenticate(self.request, username=username, password=password)

            if user is not None:
                login(self.request, user)
                return redirect(to='heroes:heroes_list')
            else:
                messages.error(self.request, 'Неверный логин или пароль')


class LogoutView(TemplateView):
    template_name = 'user/login.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('user:login')


class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('heroes:heroes_list')

    def form_valid(self, form):

        self.object = form.save()

        print(self.object)

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())




# class HeroesInnLoginView(LoginView):
#     # authentication_form = LoginForm
#     template_name = 'user/login.html'
#     success_url = reverse_lazy('home-page')
#     redirect_authenticated_user = True
