import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('<int:article_id>/', mainapp.article_page, name='article_page'),
    path('<int:article_id>/leave_comment', mainapp.leave_comment, name='leave_comment'),

    path('edit/<int:article_id>/', mainapp.edit_article, name='edit_article'),
    path('remove/<int:article_id>/', mainapp.delete_article, name='delete_article'),

    path('tech/', mainapp.tech, name='tech'),
    path('tech/<int:tech_id>/', mainapp.tech_page, name='tech_page'),
    path('tech/<int:tech_id>/tech_leave_comment', mainapp.tech_leave_comment, name='tech_leave_comment'),

    path('tech/edit/<int:tech_id>/', mainapp.edit_tech, name='edit_tech'),
    path('tech/remove/<int:tech_id>/', mainapp.delete_tech, name='delete_tech'),

    path('sport/', mainapp.sport, name='sport'),
    path('sport/<int:sport_id>/', mainapp.sport_page, name='sport_page'),
    path('sport/<int:sport_id>/sport_leave_comment', mainapp.sport_leave_comment, name='sport_leave_comment'),

    path('sport/edit/<int:sport_id>/', mainapp.edit_sport, name='edit_sport'),
    path('sport/remove/<int:sport_id>/', mainapp.delete_sport, name='delete_sport'),
    
]
