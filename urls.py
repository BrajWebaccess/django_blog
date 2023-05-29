from django.urls import include, path
from .views import Home, Article, ArticleDetails


urlpatterns = [
    path('', Home.as_view()),
    path('articles', Article.as_view()),
    path('articles/<int:id>', ArticleDetails.as_view())
]

# blog/ will match an url http:// localhost:8000/blog/
# articles/ will match http:// localhost:800/articles/