from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib import messages
from .forms import ArticleForm
from django.views import View
from .models import Article


class ListArticlesView(View):
    def get(self, request):
        articles = Article.objects.all().order_by('-created_at')
        return render(request, 'list_articles_page.html', {'articles': articles})


class CreateArticleView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = ('articles.add_article')

    def get(self, request):
        form = ArticleForm()
        return render(request, 'create_article_page.html', {'form': form})

    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            Article.objects.create(
                title=title,
                content=content,
                author=request.user
            )
            messages.success(request, 'Article created successfully.')
            return redirect('list_articles_page')
        else:
            messages.error(request, 'Failed to create article due to a problem.')
            return redirect('create_article_page')


class RetrieveArticleView(View):
    def get(self, request, pk):
        article = get_object_or_404(Article, id=pk)
        return render(request, 'retrieve_article_page.html', {'article': article})


class UpdateArticleView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = ('articles.change_article')

    def get(self, request, pk):
        ...

    def post(self, request, pk):
        ...


class DeleteArticleView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = ('articles.delete_article')

    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        if request.user == article.author or request.user.is_superuser:
            article.delete()
            messages.success(request, 'Article deleted successfully.')
            return redirect('list_articles_page')
        else:
            messages.error(request, 'You do not have permission to delete this article.')
            return redirect('list_articles_page')