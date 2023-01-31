from django.urls import path
from crudapp.views import article_func

urlpatterns = [
    path('', article_func, name='article_func'),
]