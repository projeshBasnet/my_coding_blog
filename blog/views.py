from django.shortcuts import redirect, render
from .forms import UserLoginForm, PostCreateForm
from django.contrib.auth import authenticate,login,logout
from .models import Post

def Home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})


# for loging th euser
def UserLogin(request):
    form = UserLoginForm()
    if request.method=="POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username = data.get('email'),password=data.get('password'))
            if user:
                login(request,user)
                return redirect('home')
    return render(request,'userlogin.html',{'form':form})


# for logout user
def UserLogout(request):
    logout(request)
    return redirect('home')



# creating post by admin
def CreatePost(request):
    form = PostCreateForm()
    if request.method=="POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'createpost.html',{'form':form})

def PostDetail(request,pk):
    post = Post.objects.get(pk=pk)
    print(post)
    return render(request,'postdetail.html',{'post':post})


