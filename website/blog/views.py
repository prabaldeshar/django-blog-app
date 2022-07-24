from typing import List
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
from utils import web_scrape
# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/blogs.html", {"blogs": blogs, "page_obj": page_obj})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    # return render(request, "meetings/detail.html", {"meeting": meeting})
    return render(request, "blog/detail.html", {"blog": blog})

def add_blogs_to_db(request):
    blogs = retrive_blogs_from_website()
    for blog in blogs:
        # breakpoint()
        if Blog.objects.filter(title=blog["title"]).exists() != True:
            if blog["reading_time"] != "" and blog["reading_time"] != int:
                reading_time = int(blog["reading_time"].split()[0])
            else:
                reading_time = 0
            b = Blog(title=blog["title"], blog_image_url=blog["blog_image_url"], description=blog["description"], author_name=blog["author_name"], author_designation=blog["author_designation"], author_image_url=blog["author_image_url"], reading_time=reading_time)
            b.save()
        else:
            print("The Blog with the same title already exists in the database")

    return redirect("blogs")

def retrive_blogs_from_website():
    print("Retrive all blogs function called")
    all_blogs = web_scrape.main()
    return all_blogs



