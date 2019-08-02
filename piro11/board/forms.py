from django import forms
from django.forms import ModelForm

from board.models import Article


class ArticleForm(ModelForm):
    category = forms.ChoiceField(choices=(
        ('일기', '일기'),
        ('공부', '공부'),
        ('기타', '기타'),)
    )

    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise forms.ValidationError('제목에 *을 포함할 수 없습니다.')
        return title

    def clean(self):
        title = self.cleaned_data['title']
        content = self.cleaned_data['content']
        if len(title) + len(content) < 5:
            raise forms.ValidationError('글자수가 너무 적습니다.')
        return self.cleaned_data

    class Meta:
        model = Article
        exclude = ('file', )