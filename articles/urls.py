from django.urls import URLPattern, path
from .views import ArticleListView,ArticleUpdateView,ArticleDeleteView,ArticleDetailView,ArticleCreateView
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('',ArticleListView.as_view(), name = 'article_list'),
    path('<int:pk>/edit/',ArticleUpdateView.as_view(), name = 'article_edit'),
    path('<int:pk>/',ArticleDetailView.as_view(), name = 'article_detail'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name = 'article_delete'),
    path('article_new/',ArticleCreateView.as_view(), name = 'article_new'),

]
