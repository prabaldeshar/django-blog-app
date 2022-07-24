from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('webscrape/', views.add_blogs_to_db, name="web_scrape"),
]
