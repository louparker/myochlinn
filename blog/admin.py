from django.contrib import admin
from .models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'preview',
        'section_one',
        'section_two',
        'section_three',
        'image',
        'source_link',
    )


admin.site.register(Post, BlogAdmin)
