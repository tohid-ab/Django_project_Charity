from django.contrib import admin
from .models import *
# Register your models here.
admin.site.disable_action('delete_selected')
admin.site.site_header = 'پنل مدیریت'


class TagAdmin(admin.ModelAdmin):
    list_display = ('positions', 'name', 'slug', 'status')
    list_filter = ('positions',)
    search_fields = ('name',)


admin.site.register(Tag, TagAdmin)


class CommentLine(admin.StackedInline):
    model = Comment
    extra = 0


class ARticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'time', 'user',
                    'status', 'category',)
    list_filter = ('time', 'status')
    search_fields = ('title', 'body')
    ordering = ('user', 'status')
    list_editable = ('user','status')

    inlines = [
        CommentLine,
    ]

    def category(self, obj):
        return ", ".join([Tag.name for Tag in obj.daste.all()])
    category.short_descriptions = 'دسته بندی'


admin.site.register(Post, ARticleAdmin)
admin.site.register(Comment)