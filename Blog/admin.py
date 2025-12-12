from django.contrib import admin
from .models import Post
# Import the Comment model
from .models import Comment
# Register your models here.

class CommentInline(admin.TabularInline):
	model = Comment
	fields = ['visitor_name', 'visitor_email', 'content', 'created_at', 'is_approved']
	readonly_fields = ['created_at']
	extra = 0

class PostAdmin(admin.ModelAdmin):
	inlines = [CommentInline]
	list_display = ['title', 'author', 'data_posted']
	list_filter = ['author', 'data_posted']
	search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
