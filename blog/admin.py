from django.contrib import admin

from .models import Post, Comment, Profile

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "body", "created", "updated"]


admin.site.register(Post)
admin.site.register(Profile)