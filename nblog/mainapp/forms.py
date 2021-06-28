from django import forms

from mainapp.models import Article, Tech, Sport


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'article_title',
            'img',
            'article_small_text',
            'article_text',
            'pub_date',
        )


class DeleteArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'article_title',
            'img',
            'article_small_text',
            'article_text',
            'pub_date',
        )


class TechForm(forms.ModelForm):
    class Meta:
        model = Tech
        fields = (
            'tech_title',
            'tech_img',
            'tech_small_text',
            'tech_text',
            'tech_pub_date',
        )


class DeleteTech(forms.ModelForm):
    class Meta:
        model = Tech
        fields = (
            'tech_title',
            'tech_img',
            'tech_small_text',
            'tech_text',
            'tech_pub_date',
        )


class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = (
            'sport_title',
            'sport_img',
            'sport_small_text',
            'sport_text',
            'sport_pub_date',
        )


class DeleteSport(forms.ModelForm):
    class Meta:
        model = Sport
        fields = (
            'sport_title',
            'sport_img',
            'sport_small_text',
            'sport_text',
            'sport_pub_date',
        )
