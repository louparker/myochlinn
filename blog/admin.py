from django.contrib import admin
from .models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'preview',
        'text_content',
        'image',
        'source_link',
    )


admin.site.register(Post, BlogAdmin)
