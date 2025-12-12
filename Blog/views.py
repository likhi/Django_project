from django.shortcuts import render , get_list_or_404 , get_object_or_404, redirect
from django.http import HttpResponse
from Blog.models import Post
from Blog.models import Post, Comment
from Blog.forms import CommentForm
from django.contrib.auth.models import User
from django.views.generic import(CreateView,ListView,DetailView,DeleteView,UpdateView,)
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
# Create your views here.
# there are 2 types of views we can write one is functions and another one is class views

def landing(request):
    """
    Render the landing page with video background
    """
    return render(request, 'Blog/landing.html')

def submit_comment(request):
    """
    Handle comment submission from sidebar form
    """
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        # Redirect back to the referring page or home
        return redirect(request.POST.get('next', 'Blog-home'))
    return redirect('Blog-home')

'''Post = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
'''
#function view
def home(request):
    posts = Post.objects.all()
    context ={
       'posts': posts
    }
    return render(request, 'Blog/home.html', context)

#for example of generic class views
# class view
class PostListView(ListView):
    model=Post
    template_name='Blog/home.html'
    context_object_name='posts'
    ordering=['data_posted']
    paginate_by=5

class UserPostListView(ListView):
    model=Post
    template_name='Blog/user_posts.html'
    context_object_name='posts'
    ordering=['-data_posted']
    paginate_by=5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-data_posted')


class PostDetailView(DetailView):
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(is_approved=True)
        # If user is authenticated, prefill name/email in the form
        if self.request.user.is_authenticated:
            display_name = self.request.user.get_full_name() or self.request.user.username
            context['form'] = CommentForm(initial={
                'visitor_name': display_name,
                'visitor_email': self.request.user.email,
            })
        else:
            context['form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return self.get(request, *args, **kwargs)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content','youtube_url']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
   
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):  #user passes testmixin is used to authentic even in url
    model=Post
    fields=['title','content','youtube_url']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        Post=self.get_object()
        if self.request.user==Post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):  
    model=Post
    success_url='http://127.0.0.1:8000/home/'

    
    def test_func(self):
        Post=self.get_object()
        if self.request.user==Post.author:
            return True
        return False




def get_queryset(self):
    user = get_object_or_404(user, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')



def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})





