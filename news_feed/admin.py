from django.contrib import admin
from news_feed.models import (
    Category,
    NewsData,
    NewsSource
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category model fields list display"""

    list_display = (
        "id",
        "name",
        "created_on",
        "updated_on",
    )
    search_fields = (
        "id",
        "name",
        "created_on",
        "updated_on",
    )


@admin.register(NewsData)
class NewsDataAdmin(admin.ModelAdmin):
    """NewsData model fields list display"""

    list_display = (
        "id",
        "url",
        "created_on",
        "updated_on",
    )
    search_fields = (
        "id",
        "url",
        "created_on",
        "updated_on",
    )


@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    """NewsSource model fields list display"""

    list_display = (
        "id",
        "url",
        "created_on",
        "updated_on",
    )
    search_fields = (
        "id",
        "url",
        "created_on",
        "updated_on",
    )
