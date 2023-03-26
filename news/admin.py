from django.contrib import admin

from news.models import News, NewsImage


class NewsImageAdmin(admin.StackedInline):
    model = NewsImage


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageAdmin]


admin.site.register(News, NewsAdmin)