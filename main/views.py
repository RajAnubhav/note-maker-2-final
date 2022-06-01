from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from main import models 

# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id')) # post_id becoz our button is named as post_id in the article_details.html
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'mysite/index.html'
    ordering = ['-post_date']


def CodeView(request):
    return render(request, 'mysite/code_editor.html')

def DashboardView(request):
    user_notes=Post.objects.filter()
    return render(request, 'mysite/dashboard.html', {'user_notes':user_notes})

def CategoryView(request, cats):
    category_posts=Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'category_posts':category_posts, 'cats':cats})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'mysite/article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True 
        

        context ['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context 

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'mysite/add_post.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'mysite/category_post.html'
    fields= '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'mysite/edit_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'mysite/delete_post.html'
    success_url = reverse_lazy('home')
