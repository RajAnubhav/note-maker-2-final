from django.urls import path
from . import views 
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, DashboardView
# Enter your code here
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add-post"),  
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="edit-post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete-post"),
    path('add_category/', AddCategoryView.as_view(), name="add-category"),
    path('category/<str:cats>/', CategoryView, name="category-view"),
    path('code_editor/', views.CodeView, name="editor"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('dashboard/', DashboardView, name='dashboard'),
    # path('private/<int:pk>', PrivateView, name='private_post'),
]