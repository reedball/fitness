from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *
from .forms import *


import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# print(build)

developer_key = 'AIzaSyCVuN7GOKmyHIT0xtpd2WTM4n9pEI-zwXQ'
youtube_api_service_name = 'youtube'
youtube_api_version = 'v3'


def home_page(request):
    return render(request, 'coaching_app/index.html')


def login_page(request):
    return render(request, 'coaching_app/login_reg.html')


def user_process(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="register")
        return redirect('/login_page#toregister')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST["username"]
        email = request.POST["email"]
        matched_user = User.objects.filter(username=request.POST["username"])
        if len(matched_user) > 0:
            messages.error(request, 'Username unavailable',
                           extra_tags="register")
            return redirect('/login_page#toregister')
        pw_hash = bcrypt.hashpw(
            request.POST["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = User.objects.create(
            first_name=first_name, last_name=last_name, username=username, email=email, password=pw_hash)
        request.session["new_user_id"] = new_user.id
        request.session["username"] = request.POST["username"]
    return redirect('/registration')


def registration(request):
    context = {
        "reg_user": User.objects.get(id=request.session["new_user_id"]),
    }
    return render(request, 'coaching_app/create_profile.html', context)


def login_process(request):
    matched_user = User.objects.filter(username=request.POST['username'])
    print(matched_user)
    if len(matched_user) < 1:
        messages.error(
            request, 'Email or password does not match', extra_tags="login")
        return redirect('/login_page')
    if bcrypt.checkpw(request.POST['password'].encode('utf-8'), matched_user[0].password.encode('utf-8')):
        request.session['username'] = request.POST['username']
        return redirect('/login')
    else:
        messages.error(request, 'Email or password do not match',
                       extra_tags="login")
        return redirect('/login_page')
    return redirect('/login_page')


def login(request):
    context = {
        "reg_user": User.objects.filter(username=request.session["username"])[0],
        "users_post": Post.objects.all().order_by("-created_at")
    }
    return render(request, 'coaching_app/everyone_account.html', context)


def logout(request):
    request.session.clear()
    return redirect('/login_page')


def survey(request):
    return render(request, "coaching_app/survey.html")


def survey_reply(request):
    return render(request, "coaching_app/congrats.html")


def my_account(request):
    reg_user = User.objects.filter(username=request.session["username"])[0]
    context = {
        "reg_user": User.objects.filter(username=request.session["username"])[0],
        # "new_user": User.objects.get(id=userid)
        "users_post": Post.objects.filter(posted_by=reg_user).order_by("-created_at")[1:],
        "last_post": Post.objects.filter(posted_by=reg_user).last()
    }
    return render(request, "coaching_app/my_account.html", context)


def user_account(request, user_id):
    request.session['userid'] = user_id
    selected_user = User.objects.get(id=user_id)
    context = {
        "selected_user": User.objects.get(id=user_id),
        "selected_user_posts": Post.objects.filter(posted_by=selected_user).order_by("-created_at")[1:],
        "last_post": Post.objects.filter(posted_by=selected_user).last()
    }
    return render(request, "coaching_app/user_account.html", context)

def view(request, post_id):
    request.session['postid'] = post_id
    context = {
        "selected_post": Post.objects.get(id=post_id)
    }

    return render(request, 'coaching_app/single_post.html', context)

def no_survey_reply(request):
    return render(request, "coaching_app/no_survey_reply.html")


def update(request, userid):
    errors = User.objects.edit_validator(request.POST)
    user_id = userid
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')
    matched_user = User.objects.filter(username=request.POST["username"])
    if len(matched_user) > 1:
        messages.error(request, 'Username unavailable')
        return redirect('/registration')
    else:
        updated_user = User.objects.get(id=userid)
        updated_user.first_name = request.POST['first_name']
        updated_user.last_name = request.POST['last_name']
        updated_user.bio = request.POST['bio']
        updated_user.email = request.POST['email']
        updated_user.username = request.POST['username']
        # updated_user.password = request.POST['password']
        updated_user.save()
    return redirect('/user/edit/' + user_id)


def edit_account(request, userid):
    context = {
        "reg_user": User.objects.get(id=request.session["new_user_id"]),
        "new_user": User.objects.get(id=userid)
    }
    return render(request, "coaching_app/my_account.html", context)


def sampleworkout(request):
    return render(request, "coaching_app/sample_workout.html")


def search(request):
    print('SEARCH ITEM', request.POST['search']),
    search = request.POST['search'],
    return redirect('/item')


def create_post(request):
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            post = form.save(commit=False) 
            user = User.objects.filter(username=request.session["username"])[0]     
            post.posted_by = user
            post.save()

            # print(post.post_title)

            return redirect('/my_account') 
    else: 
        form = PostForm() 
    context = {
        "reg_user": User.objects.filter(username=request.session["username"])[0],
        'form': form
    }
    
    return render(request, "coaching_app/post.html", context)

def new_post(request):
    user = User.objects.get(username=request.session["username"])
    post_created = Post.objects.create(post_title = request.POST['title'], description = request.POST['description'], posted_by=user)
    print("*************")
    print(post_created)
    print("*************")
    return redirect('/my_account')

def delete(request, post_id):
    print("delete function works")
    deleted_post = Post.objects.get(id=post_id)
    deleted_post.delete()
    print("*"*100)
    return redirect('/login')



# def post_image_view(request): 

#     if request.method == 'POST': 
#         form = PostForm(request.POST, request.FILES) 
  
#         if form.is_valid(): 
#             form.save() 
#             return redirect('success') 
#     else: 
#         form = PostForm() 
#     return render(request, 'post.html', {'form' : form}) 


# def display_post_images(request): 
  
#     if request.method == 'GET': 
  
#         # getting all the objects of hotel. 
#         Post = Post.objects.all()  
#         return render(request, 'display_post_images.html', {'post_images' : Hotels}) 

