from django.shortcuts import render
from django.http import HttpResponse
from .models import UserModel, PostModel
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from .forms import SignInForm, PostForm
import feedparser
from django.db.models import Q


import socket




def index(request):



    if request.user.is_authenticated:
        print(request.user)

        appUser = UserModel.objects.get(username=request.user)
        print(appUser)
        # filters through the users entries
        allEntries = PostModel.objects.filter(foreignkeyToUserModel=appUser)
    else:

        allEntries = ''
        url = 'http://www.nba.com/rss/nba_rss.xml'

    feed = feedparser.parse(url)
    print(allEntries)
    context = {"allEntries": allEntries,
            'feed': feed}


    return render(request, 'sportsapp/index.html', context)

def createPost(request):
    form = PostForm(request.POST or None)

    authUser = UserModel.objects.get(username=request.user)
    context = {'PostForm': form}

    if request.method == 'POST':
        print(request.method)

        if form.is_valid():
            print("WORKED")
            print(form)
            # form.save()

            # if theres a valid file to upload it creates and saves it the database
            theImage = ''
            # if request.FILES:
            #     theImage = request.FILES["imageUpload"]

            PostModel.objects.create(title=request.POST["title"], textField=request.POST["textField"],
                                     dateCreated=request.POST["dateCreated"],
                                     foreignkeyToUserModel=authUser)



            return redirect('index')

        else:
            print(form.errors)
            context = {
                'errors': form.errors,
                'Postform': form
            }

    return render(request, 'sportsapp/createpost.html', context)


def viewPost(request, post_id):
    postModel = get_object_or_404(PostModel, pk=post_id)
    print(PostModel)
    relatedItems = PostModel.objects.filter(foreignkeyToWiki= postModel)
    print(post_id)
    context = {'post_list': postModel,
               }
    print(relatedItems)

    return render(request, 'sportsapp/viewPost.html', context)


def postList():
    return HttpResponse("post list")


def createUser(request):
    form = SignInForm(request.POST or None)
    context = {'SignInForm': form}

    if request.method == 'POST':
        print(request.method)

        if form.is_valid():
            print("working")

            User.objects.create_user(request.POST["username"], "", request.POST["password1"])
            form.save()
            return redirect('index')

        else:
            context = {
                'errors': form.errors,
                'SignInForm': form
            }

    return render(request, 'sportsapp/createUser.html', context)

def postDetails(request):
    return HttpResponse(" Details")


def editPost(request):
    return HttpResponse("edit Post")


def deletePost(request, post_id):
    deletePost = get_object_or_404(PostModel, pk=post_id)
    deletePost.delete()
    return redirect('index')

def postList(request):
    query = request.GET.get("q", None)
    qs = PostModel.objects.all()
    if query is not None:
        qs = qs.filter(Q(title__icontains= query))

    context = {

        'post_list': qs

    }

    return render(request, 'sportsapp/postList.html', context)







# def index(request):
#     url = 'http://www.nba.com/rss/nba_rss.xml'
#
#     feed = feedparser.parse(url)
#
#
#     return render(request, 'sportsapp/reader.html', {
#         'feed': feed
#     })
