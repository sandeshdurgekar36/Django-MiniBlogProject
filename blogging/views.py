from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, LoginForm,AddPost,UserContact
from .models import Blog, ContactForm
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout

# home
def home(request):
    blogdesc = Blog.objects.all()
    return render(request, 'blogging/home.html',{'Blog':blogdesc})

# about
def about(request):
    return render(request, 'blogging/about.html')

# dashboard
def dashboard(request):
    if request.user.is_authenticated:
        blogdesc = Blog.objects.all()
        return render(request, 'blogging/dashboard.html',{'Blog': blogdesc, 'name': request.user.first_name})
    else:
        return HttpResponseRedirect('/login/')

# contact
def contact(request):
    if request.method == 'POST':
        contactform = UserContact(request.POST)
        if contactform.is_valid():
            em = contactform.cleaned_data['email']
            ph = contactform.cleaned_data['Phone']
            contact_detail = ContactForm(email=em, Phone=ph)
            contact_detail.save()
            contactform = UserContact()
            messages.success(request, 'Message Sent Successfully!!!')
    else:
        contactform = UserContact()
    return render(request, 'blogging/contact.html', {'form': contactform})

# signup
def User_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='author')
                user.groups.add(group)
                messages.success(request, 'Register Successfully !!!')
        else:
            form = SignUpForm()
        return render(request, 'blogging/signup.html', {'form': form})
    return HttpResponseRedirect('/dashboard/')

# login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request.user, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successfully Done')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blogging/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddPost(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                Desc = form.cleaned_data['desc']
                td = Blog(title=title, desc=Desc)
                td.save()
                messages.success(request, 'Your Add Posted Successfully')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = AddPost()
        return render(request, 'blogging/addpost.html',{'form': form})
    else:
        return HttpResponseRedirect('/login/')

def editpost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':   
            pi = Blog.objects.get(pk=id)
            form = AddPost(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Add Editted Successfully')
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Blog.objects.get(pk=id)
            form = AddPost(instance=pi)
        return render(request, 'blogging/editpost.html',{'form':form, 'id':id})
    else:
        return HttpResponseRedirect('/login/')

def deletepost(request, id):
    if request.method == 'POST':
        pi = Blog.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/dashboard/')
  