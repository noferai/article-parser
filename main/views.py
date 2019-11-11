from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import FormView, CreateView, DetailView, DeleteView
from django_tables2 import SingleTableView
from django.urls import reverse, reverse_lazy
from .forms import UrlForm, ArticleForm
from .models import Article
from .tables import ArticleTable


class GetUrlView(FormView):
    template_name = 'main/get_url.html'
    form_class = UrlForm

    def form_valid(self, form):
        return HttpResponseRedirect(reverse('main:create', kwargs={'url': form.cleaned_data['url']}))


class ArticleCreateView(CreateView):
    template_name = 'main/article_create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('main:list')

    def get_form_kwargs(self):
        kwargs = super(ArticleCreateView, self).get_form_kwargs()
        kwargs.update(self.kwargs)  # update kwargs for the form init method
        return kwargs

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return super().form_invalid(form)

    def form_valid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.cleaned_data)
        else:
            form.instance.url = self.kwargs['url']
            # override object with same url
            Article.objects.update_or_create(defaults=form.cleaned_data, url=self.kwargs['url'])
            return HttpResponseRedirect(self.success_url)


class ArticleListView(SingleTableView):
    model = Article
    table_class = ArticleTable


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('main:list')

    # to avoid confirmation
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
