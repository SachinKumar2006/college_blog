
# Register your models here.

from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # Columns shown in admin list page
    list_display = ['title', 'author', 'status', 'publish', 'created']

    # Filters on right sidebar
    list_filter = ['status', 'author', 'publish', 'created']

    # Search box in admin
    search_fields = ['title', 'body']

    # Automatically create slug from title
    prepopulated_fields = {'slug': ('title',)}

    # Faster author selection for large user tables
    raw_id_fields = ['author']

    # Navigation by date
    date_hierarchy = 'publish'

    # Default ordering
    ordering = ['status', '-publish']

    # Posts per page
    list_per_page = 10

    # Show filter facets
    show_facets = admin.ShowFacets.ALWAYS