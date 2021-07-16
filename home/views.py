from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# Home page 
def home(request):
    allPosts = Paginator(Post.objects.all().order_by('-view')[0:4], 2)
    page = request.GET.get('page')
    try:
        Posts = allPosts.page(page)
    except PageNotAnInteger:
        Posts = allPosts.page(1)
    except EmptyPage:
        Posts = allPosts.page(allPosts.num_pages)
    
    context = {'allPosts' : Posts}
    return render(request, 'home.html', context)

# View Posts
def homepost(request, slug):
    post = Post.objects.filter(slug = slug).first()
    post.view = post.view + 1
    post.save()
    context = { 'post' : post }
    return render(request, 'blogpost.html', context)

# About page
def about(request):
    return render(request, 'about.html')

# Contact page
def contact(request):
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['emailcontact']
        phone = request.POST['phone']
        content =request.POST['content']
    
        if len(name) < 2 or len(email) < 5 or len(phone) < 10 or len(content) < 8 :
            messages.warning(request, 'Please fill the form correctly !')
       
        else:
            contact = Contact(name = name, email = email, phone = phone, content = content)
            contact.save()
            messages.success(request, 'Your message has been sent successfully')
    return render(request, 'contact.html')


# Handle signup 
def handleSignUp(request):
    if request.method == 'POST':
        # get the post perameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']  
        email = request.POST['email']  
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checks for errorneous input
        # passwords should match
        if pass1 == pass2:
            # if User.objects.filter(username = username).first():
                # passwords should be greater then 5 charcters
                if len(pass1) > 5 and len(pass1) < 12:
                    # username should be alpha numeric
                    if username.isalnum():
                        # username should be greater then 5 chacters
                        if len(username) > 5 and len(username) < 12:
                        # create the user
                            try:
                                myuser = User.objects.create_user(username, email, pass1)
                                myuser.first_name = fname
                                myuser.last_name = lname
                                myuser.save()
                                messages.success(request, 'User has been created successfully ')
                                return redirect('home')
                            except:
                                messages.error(request, 'Username already exists')
                                return redirect('home')
                        else:
                            messages.error(request, 'Username should be greater then 5 charcters and less then 12 charecters')
                            return redirect('home')
                    else:
                        messages.error(request, 'Username only can contain alphabets and numerics')
                        return redirect('home')
            
                else:
                    messages.error(request, 'Password should be greater then 5 charcters')
                    return redirect('home')
            # else:
            #     messages.error(request, 'username already exist')
            #     return redirect('home')
        else:
            messages.error(request, "Password doesn't match" )
            return redirect('home')
    else:
        return HttpResponse("Not Allowed !")

# handle logout
def handleLogIn(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username = loginusername, password = loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials, Please try again')
            return redirect('home')
    
    else:
        return HttpResponse('Invalid credentials, Please fill the login for for login')

# handle logout
def handleLogOut(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home') 

