# Generated by Django 2.2 on 2021-06-13 13:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('img', models.ImageField(upload_to='img/article', verbose_name='Фотография')),
                ('article_small_text', models.CharField(max_length=200, verbose_name='Введите короткий текст')),
                ('article_text', models.TextField(verbose_name='Введите текст')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Политическая новость',
                'verbose_name_plural': 'Политические новости',
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('sport_img', models.ImageField(upload_to='img/sport', verbose_name='Фотография')),
                ('sport_small_text', models.CharField(max_length=200, verbose_name='Введите короткий текст')),
                ('sport_text', models.TextField(verbose_name='Введите текст')),
                ('sport_pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Спортивная новость',
                'verbose_name_plural': 'Спортивные новости',
            },
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('tech_img', models.ImageField(upload_to='img/tech', verbose_name='Фотография')),
                ('tech_small_text', models.CharField(max_length=200, verbose_name='Введите короткий текст')),
                ('tech_text', models.TextField(verbose_name='Введите текст')),
                ('tech_pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Технологическая новость',
                'verbose_name_plural': 'Технологические новости',
            },
        ),
        migrations.CreateModel(
            name='TechComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_author_name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('tech_comment_text', models.CharField(max_length=200, verbose_name='Текст комментария')),
                ('tech_created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tech_comments', to='mainapp.Tech', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Технологический комментарий',
                'verbose_name_plural': 'Технологические комментарии',
                'ordering': ['-tech_created_on'],
            },
        ),
        migrations.CreateModel(
            name='SportComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_author_name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('sport_comment_text', models.CharField(max_length=200, verbose_name='Текст комментария')),
                ('sport_created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sport_comments', to='mainapp.Sport', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Спортивный комментарий',
                'verbose_name_plural': 'Спортивные комментарии',
                'ordering': ['-sport_created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Текст комментария')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Article', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Политический комментарий',
                'verbose_name_plural': 'Политические комментарии',
                'ordering': ['-created_on'],
            },
        ),
    ]
