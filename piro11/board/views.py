from django.http import HttpResponse
from django.shortcuts import render


# function view
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, TemplateView, ListView, DetailView

from board.forms import ArticleForm
from board.models import Article


def create_article(request):
    form = ArticleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse('작성되었습니다.')
    else:
        context = {'form': form}
        return render(request, 'board/create_article.html', context)


class ArticleCreateView(View):
    def get(self, request):
        form = ArticleForm()
        context = {'form': form}
        return render(request, 'board/create_article.html', context)

    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('작성되었습니다.')
        else:
            context = {'form': form}
            return render(request, 'board/create_article.html', context)


class ArticleFormView(FormView):
    form_class = ArticleForm
    template_name = 'board/create_article.html'
    initial = {'title': '제목'}

    def form_valid(self, form):
        form.save()
        return HttpResponse('작성되었습니다.')


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class ArticleListView(ListView):
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
