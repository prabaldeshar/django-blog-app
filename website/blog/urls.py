from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('webscrape/', views.add_blogs_to_db, name="web_scrape"),
    path('search_blogs/', views.search_blogs, name="search-blogs"),
    path('update/<int:blog_id>/', views.update_blog, name="update-blog"),
    path('delete_all/', views.delete_all_blog, name="delete-all"),
]
