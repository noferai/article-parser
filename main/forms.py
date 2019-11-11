from django import forms
from .models import Article
from .parser import fetch_page, parse


class UrlForm(forms.Form):
    url = forms.URLField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url'].widget.attrs.update(size='40')

    def clean_url(self):
        try:
            req = fetch_page(self.cleaned_data['url'])
            return req.url
        except Exception as e:
            raise forms.ValidationError(e)


class ArticleForm(forms.ModelForm):
    def __init__(self, url=None, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.url = url
        for field_name in self.fields.keys():
            self.fields[field_name] = forms.CharField(label=field_name.capitalize() + ' css selector')

    def clean(self):
        try:
            data = parse(self.url, **self.cleaned_data)
        except Exception as e:
            raise forms.ValidationError("Error: %s!" % e.__class__.__name__)
        return data

    class Meta:
        model = Article
        fields = '__all__'
