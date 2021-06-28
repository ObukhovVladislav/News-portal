from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from mainapp.forms import ArticleForm, TechForm, SportForm
from mainapp.models import Article, Tech, Sport


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:10]
    pagination = Paginator(latest_articles_list, 4)
    page_number = request.GET.get('page', 1)
    page = pagination.get_page(page_number)
    is_pagination = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page{}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page{}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'latest_articles_list': latest_articles_list,
        'title': 'Политика',
        'page': page,
        'is_pagination': is_pagination,
        'next_url': next_url,
        'prev_url': prev_url,
    }
    return render(request, 'mainapp/article.html', context)


def article_page(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Новость не найдена!")
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    context = {
        'title': 'Страница новости',
        'article': a,
        'latest_comments_list': latest_comments_list,
    }

    return render(request, 'mainapp/article_page.html', context)


@login_required
def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Новость не найдена!")
    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('mainapp:article_page', args=(a.id,)))


def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = ArticleForm(instance=article)
    context = {
        'title': 'Изменить новость',
        'form': form,
    }
    return render(request, 'mainapp/add_article.html', context)


def delete_article(request, article_id):
    remove_article = Article.objects.get(id=article_id)
    remove_article.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def tech(request):
    latest_tech_list = Tech.objects.order_by('-tech_pub_date')[:10]
    pagination = Paginator(latest_tech_list, 4)
    page_number = request.GET.get('page', 1)
    page = pagination.get_page(page_number)
    is_pagination = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page{}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page{}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'latest_tech_list': latest_tech_list,
        'title': 'Технология',
        'page': page,
        'is_pagination': is_pagination,
        'next_url': next_url,
        'prev_url': prev_url,
    }
    return render(request, 'mainapp/tech.html', context)


def tech_page(request, tech_id):
    try:
        a = Tech.objects.get(id=tech_id)
    except:
        raise Http404("Новость не найдена!")
    latest_tech_comments_list = a.tech_comments.order_by('-id')[:10]
    context = {
        'title': 'Страница новости',
        'tech': a,
        'latest_tech_comments_list': latest_tech_comments_list,
    }

    return render(request, 'mainapp/tech_page.html', context)


@login_required
def tech_leave_comment(request, tech_id):
    try:
        a = Tech.objects.get(id=tech_id)
    except:
        raise Http404("Новость не найдена!")
    a.tech_comments.create(tech_author_name=request.POST['name'], tech_comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('mainapp:tech_page', args=(a.id,)))


def edit_tech(request, tech_id):
    tech = Tech.objects.get(id=tech_id)
    if request.method == 'POST':
        form = TechForm(request.POST, instance=tech)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:tech'))
    else:
        form = TechForm(instance=tech)
    context = {
        'title': 'Изменить новость',
        'form': form,
    }
    return render(request, 'mainapp/add_tech.html', context)


def delete_tech(request, tech_id):
    remove_tech = Tech.objects.get(id=tech_id)
    remove_tech.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def sport(request):
    latest_sport_list = Sport.objects.order_by('-sport_pub_date')[:10]
    pagination = Paginator(latest_sport_list, 4)
    page_number = request.GET.get('page', 1)
    page = pagination.get_page(page_number)
    is_pagination = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page{}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page{}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'latest_sport_list': latest_sport_list,
        'title': 'Cпорт',
        'page': page,
        'is_pagination': is_pagination,
        'next_url': next_url,
        'prev_url': prev_url,
    }
    return render(request, 'mainapp/sport.html', context)


def sport_page(request, sport_id):
    try:
        a = Sport.objects.get(id=sport_id)
    except:
        raise Http404("Новость не найдена!")
    latest_sport_comments_list = a.sport_comments.order_by('-id')[:10]
    context = {
        'title': 'Страница новости',
        'sport': a,
        'latest_sport_comments_list': latest_sport_comments_list,
    }

    return render(request, 'mainapp/sport_page.html', context)


@login_required
def sport_leave_comment(request, sport_id):
    try:
        a = Sport.objects.get(id=sport_id)
    except:
        raise Http404("Новость не найдена!")
    a.sport_comments.create(sport_author_name=request.POST['name'], sport_comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('mainapp:sport_page', args=(a.id,)))


def edit_sport(request, sport_id):
    sport = Sport.objects.get(id=sport_id)
    if request.method == 'POST':
        form = SportForm(request.POST, instance=sport)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:sport'))
    else:
        form = SportForm(instance=sport)
    context = {
        'title': 'Изменить новость',
        'form': form,
    }
    return render(request, 'mainapp/add_sport.html', context)


def delete_sport(request, sport_id):
    remove_sport = Sport.objects.get(id=sport_id)
    remove_sport.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
