from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from .models import *
from .forms import *


class HomeView(View):
    def get(self, request):
        return render(request, 'home_page.html', {'user': request.user})


class ListNewsView(View):
    def get(self, request):
        news = News.objects.all().order_by('-created_at')
        return render(request, 'list_news_page.html', {'news': news, 'page_title': 'News'})


class MyNewsView(LoginRequiredMixin, View):
    login_url = 'login_page'

    def get(self, request):
        news = News.objects.filter(author=request.user).order_by('-created_at')
        return render(request, 'my_news_page.html', {'news': news, 'page_title': 'My News'})


class CreateNewsView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = ('news.add_news')

    def get(self, request):
        form = NewsForm()
        return render(request, 'create_news_page.html', {'form': form})
    
    def post(self, request):
        form = NewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            News.objects.create(
                title=title,
                content=content,
                author=request.user
            )
            messages.success(request, 'News created successfully.')
            return redirect('list_news_page')
        messages.error(request, 'Failed to create news due to a problem.')
        return render(request, 'create_news_page.html', {'form': form})


class RetrieveNewsView(View):
    def get(self, request, pk):
        news = get_object_or_404(News, id=pk)
        return render(request, 'retrieve_news_page.html', {'news': news})


class UpdateNewsView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = ('news.change_news')

    def get(self, request, pk):
        news = get_object_or_404(News, id=pk)
        form = NewsForm(initial={
            'title': news.title,
            'content': news.content,
        })
        return render(request, 'update_news_page.html', {'form': form, 'pk': pk})

    def post(self, request, pk):
        news = get_object_or_404(News, id=pk)
        form = NewsForm(request.POST)
        if form.is_valid():
            news.title = form.cleaned_data['title']
            news.content = form.cleaned_data['content']
            news.save()
            messages.success(request, 'News updated successfully.')
            return redirect('list_news_page')
        messages.error(request, 'Failed to update news due to a problem.')
        return render(request, 'update_news_page.html', {'form': form, 'pk': pk})

class DeleteNewsView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = ('news.delete_news')

    def post(self, request, pk):
        news = get_object_or_404(News, id=pk)
        if request.user == news.author or request.user.is_superuser:
            news.delete()
            messages.success(request, 'News deleted successfully.')
            return redirect('list_news_page')
        messages.error(request, 'You do not have permission to delete this news.')
        return redirect('list_news_page')
    