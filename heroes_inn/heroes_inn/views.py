from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.method == 'GET' and request.user.is_authenticated:
            print('----------------------')
            print('authenticated')
            print('----------------------')
            return redirect('heroes:heroes_list')
        else:
            return render(self.request, 'home.html')

