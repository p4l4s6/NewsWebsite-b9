from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from news import forms
from news.models import Category, FlashNews, Article


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Category.objects.filter(is_menu=True, is_active=True)
        context['flash_news'] = FlashNews.objects.last()
        context['categories'] = Category.objects.filter(is_active=True)
        context['articles'] = Article.objects.filter(is_draft=False)
        return context


class ArticleDetailView(View):

    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        context = {
            'article': article
        }
        return render(request, 'article-details.html', context=context)


class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            password = form.data['password']
            user = form.save()
            user.set_password(password)
            user.save()
        context = {'form': form}
        return render(request, 'register.html', context=context)


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    login(request, user)
                    messages.success(request, "Logged in successfully")
                    return redirect('/')
                messages.error(request, "Password didnt match")
            except ObjectDoesNotExist:
                messages.error(request, "User not found")
        else:
            messages.error(request, "Invalid data")
        context = {'form': form}
        return render(request, 'login.html', context=context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/auth/login/')
