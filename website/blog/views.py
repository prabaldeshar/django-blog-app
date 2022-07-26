import re
from typing import List
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
from .forms import BlogUpdateForm
from utils import web_scrape
# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    # assert Blog.objects.all().ordered == True
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/blogs.html", {"blogs": blogs, "page_obj": page_obj})

def detail(request, blog_id: int):
    blog = get_object_or_404(Blog, pk=blog_id)
    # return render(request, "meetings/detail.html", {"meeting": meeting})
    return render(request, "blog/detail.html", {"blog": blog})

def search_blogs(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = Blog.objects.filter(title__contains=searched)
        return render(request, "blog/search_blogs.html", {"searched": searched, "blogs": blogs})
    else:
        return render(request, "blog/search_blogs.html")

def add_blogs_to_db(request):
    blogs = retrive_blogs_from_website()
    if blogs == None:
        return HttpResponse("No blogs foundx")
    for blog in blogs:
        # breakpoint()
        if Blog.objects.filter(title=blog["title"]).exists() != True:
            if blog["reading_time"] != "" and type(blog["reading_time"]) != int:
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

def update_blog(request, blog_id: int):
    if request.method == "GET":
        blog = Blog.objects.get(pk=blog_id)
        blog_form = BlogUpdateForm(initial={"description": blog.description, "title": blog.title})
    else:
        blog = Blog.objects.get(pk=blog_id)
        f = BlogUpdateForm(request.POST, instance=blog)
        f.save()
        return redirect('detail', blog_id=blog_id)
    return render(request, "blog/update_blog.html", {"blog_form": blog_form})

def delete_all_blog(request):
    Blog.objects.all().delete()
    return redirect('blogs')
