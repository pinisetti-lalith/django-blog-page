from django.contrib import admin
from .models import Posts

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']

    class Meta:
        model = Posts


admin.site.register(Posts, PostAdmin)
