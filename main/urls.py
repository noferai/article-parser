from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', GetUrlView.as_view(), name='geturl'),
    path('create/<path:url>', ArticleCreateView.as_view(), name='create'),
    path('list/', ArticleListView.as_view(), name='list'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name="detail"),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name="remove"),
]
