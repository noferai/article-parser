from django.urls import path, include

urlpatterns = [path('', include('main.urls', namespace="main"))]
