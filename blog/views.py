from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


#  all Blogs page function
def blog(request):
    allPosts = Paginator(Post.objects.all().order_by('-datetime'), 2)
    page = request.GET.get('page')
    try:
        Posts = allPosts.page(page)
    except PageNotAnInteger:
        Posts = allPosts.page(1)
    except EmptyPage:
        Posts = allPosts.page(allPosts.num_pages)
    
    context = {'allPosts' : Posts}
    return render(request, 'blog.html', context)
 
# Blogpost page function
def blogpost(request, slug):
    post = Post.objects.filter(slug = slug).first()
    post.view = post.view + 1
    post.save()
    context = { 'post' : post }
    return render(request, 'blogpost.html', context)

