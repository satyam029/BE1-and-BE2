from django.urls import path
from .views import ArticleAPIView, ArticleDetailView, GenericAPIView

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetailView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]

