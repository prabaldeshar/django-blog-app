from django.shortcuts import get_object_or_404, render
from .models import Blog
# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blog/blogs.html", {"blogs": blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    # return render(request, "meetings/detail.html", {"meeting": meeting})
    return render(request, "blog/detail.html", {"blog": blog})

def add_blogs_to_db(request):
    pass

