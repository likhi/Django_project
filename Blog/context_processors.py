from django.contrib.auth.models import User
from Blog.models import Post, Comment
from Blog.forms import CommentForm

def all_authors(request):
    """
    Context processor to pass all authors (users with posts) to templates
    """
    # Get all users who have at least one post
    authors = User.objects.filter(post__isnull=False).distinct().order_by('username')
    
    return {
        'all_authors': authors
    }

def comments_and_form(request):
    """
    Context processor to make comments and form available globally
    """
    # Get all approved comments
    comments = Comment.objects.filter(is_approved=True).order_by('-created_at')[:5]
    
    # Initialize form with prefilled data for authenticated users
    if request.user.is_authenticated:
        display_name = request.user.get_full_name() or request.user.username
        form = CommentForm(initial={
            'visitor_name': display_name,
            'visitor_email': request.user.email,
        })
    else:
        form = CommentForm()
    
    return {
        'comments': comments,
        'form': form
    }