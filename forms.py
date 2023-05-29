from django.forms import ModelForm  # django provide a feautre for creating a form 
# by defining a class inside forms.py file like below

from .models import ArticleModel

class ArticleForm(ModelForm):
    class Meta:
        model = ArticleModel
        fields = ["title", "category", "author", "content"]