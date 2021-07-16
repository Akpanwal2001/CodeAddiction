from django.db.models import query
from django.shortcuts import redirect, render
from django.contrib import messages
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def search(request):
    if request.method == 'POST':
        query = request.POST['query']

        if len(query) > 70:
            allPosts = Post.objects.none()
            messages.warning(request, 'Please search somthing else !')

        elif len(query) == 0:
            allPosts = Post.objects.none()
            messages.warning(request, 'Please fill somthing in search box !')
            
        else:   
            allPoststitle = Post.objects.filter(title__icontains = query)
            allPostscontent = Post.objects.filter(content__icontains = query)
            allPosts = allPoststitle.union(allPostscontent)
                  
            if allPosts.count() == 0:
                messages.warning(request, 'No search results found !')

        context = {'allPosts' : allPosts , 'query':query}
        return render(request, 'search.html', context)

    else:
        messages.error(request, 'Somthing went wrong, Please Try to search from search box !')
        return redirect('home')   

# View Posts
def searchpost(request, slug):
    post = Post.objects.filter(slug = slug).first()
    post.view = post.view + 1
    post.save()
    context = { 'post' : post }
    return render(request, 'blogpost.html', context)