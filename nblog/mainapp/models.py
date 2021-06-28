from django.db import models
from datetime import date
import datetime
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Заголовок', max_length=200)
    img = models.ImageField('Фотография', upload_to='img/article')
    article_small_text = models.CharField('Введите короткий текст', max_length=200)
    article_text = models.TextField('Введите текст')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Политическая новость'
        verbose_name_plural = 'Политические новости'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Новость')
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author_name

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Политический комментарий'
        verbose_name_plural = 'Политические комментарии'


class Tech(models.Model):
    tech_title = models.CharField('Заголовок', max_length=200)
    tech_img = models.ImageField('Фотография', upload_to='img/tech')
    tech_small_text = models.CharField('Введите короткий текст', max_length=200)
    tech_text = models.TextField('Введите текст')
    tech_pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.tech_title

    def was_published_recently(self):
        return self.tech_pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Технологическая новость'
        verbose_name_plural = 'Технологические новости'


class TechComment(models.Model):
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE, verbose_name='Новость', related_name='tech_comments')
    tech_author_name = models.CharField('Имя автора', max_length=50)
    tech_comment_text = models.CharField('Текст комментария', max_length=200)
    tech_created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tech_author_name

    class Meta:
        ordering = ['-tech_created_on']
        verbose_name = 'Технологический комментарий'
        verbose_name_plural = 'Технологические комментарии'


class Sport(models.Model):
    sport_title = models.CharField('Заголовок', max_length=200)
    sport_img = models.ImageField('Фотография', upload_to='img/sport')
    sport_small_text = models.CharField('Введите короткий текст', max_length=200)
    sport_text = models.TextField('Введите текст')
    sport_pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.sport_title

    def was_published_recently(self):
        return self.sport_pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Спортивная новость'
        verbose_name_plural = 'Спортивные новости'


class SportComment(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, verbose_name='Новость', related_name='sport_comments')
    sport_author_name = models.CharField('Имя автора', max_length=50)
    sport_comment_text = models.CharField('Текст комментария', max_length=200)
    sport_created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sport_author_name

    class Meta:
        ordering = ['-sport_created_on']
        verbose_name = 'Спортивный комментарий'
        verbose_name_plural = 'Спортивные комментарии'
