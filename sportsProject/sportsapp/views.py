from django.shortcuts import render
from django.http import HttpResponse
from .models import UserModel, PostModel
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from .forms import SignInForm, PostForm



def index(request):
    # if request.user.is_authenticated:
    #     print(request.user)
    #
    #     authUser = UserModel.objects.get(username=request.user)
    #
    #     allEntries = PostModel.objects.filter(foreignkeyToUserModel=authUser)
    # else:
    #
    #     allEntries =''
    #     context = {'allEnttries': allEntries}
    #
    #
    return render(request,'sportsapp/index.html')
    # return HttpResponse("Index")

def createPost(request):
    form = PostForm(request.POST or None)

    appUser = UserModel.objects.get(username=request.user)
    context = {'PostForm': form}

    if request.emthod == 'POST':
        if form.is_valid():
            PostModel.objects.create(title=request.POST['title'], textField=request.POST['textField'],dateCreated = request.POST['dateCreated'], foreignkeyToUserModel=appUser)

    return redirect("index")


def viewPost(request):
    return HttpResponse("view Post")


def postList():
    return HttpResponse("post list")


def createUser(request):
    return HttpResponse("Create user")

def postDetails(request):
    return HttpResponse(" Details")


def editPost(request):
    return HttpResponse("edit Post")


def deletePost(request):
    return HttpResponse("delete Post")

