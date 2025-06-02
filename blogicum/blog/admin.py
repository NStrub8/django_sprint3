from django.contrib import admin

from .models import Post, Category, Location


admin.site.site_title = 'Администрирование Блогикума'
admin.site.site_header = 'Блог'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'pub_date', 'is_published',
        'author', 'category', 'location'
    )
    list_filter = ('is_published', 'category', 'location')
    search_fields = ('title', 'text')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
