from django.contrib import admin

from mainapp.models import Article, Comment, Tech, TechComment, Sport, SportComment

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tech)
admin.site.register(TechComment)
admin.site.register(Sport)
admin.site.register(SportComment)
