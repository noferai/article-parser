import django_tables2 as tables
from .models import Article


class ArticleTable(tables.Table):
    title = tables.TemplateColumn('<a href="{{record.url}}" target="_blank">{{record.title|truncatewords:5}}</a>')
    content = tables.TemplateColumn('{{record.content|truncatewords:40}}')
    actions = tables.TemplateColumn(template_name="main/actionbuttons.html", extra_context={
        'view_link': 'main:detail',
        'remove_link': 'main:remove'
    }, orderable=False, exclude_from_export=True)

    class Meta:
        model = Article
        template_name = "django_tables2/bootstrap4.html"
        fields = ['title', 'content', 'date']
        attrs = {
            'class': 'table table-striped table-hover text-center',
            'thead': {
                'class': 'thead-dark'
        }}
