from django.contrib import admin
from . models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    list_display = (
        'title',
        'intro',
        'date',
        'image',
    )

    list_filter = ('date',)


admin.site.register(Post, PostAdmin)
