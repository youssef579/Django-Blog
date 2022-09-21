from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UpdateUser
from django.contrib import messages
from .forms import PostForm

@login_required
def home(request):
    context = {
        "home_activate": "active",
        "posts": request.user.post_set.all()
    }
    return render(request, "main/home.html", context)

@login_required
def profile(request):
    match request.method:
        case "POST":
            user_update_form = UpdateUser(request.POST, request.FILES, instance=request.user)

            if user_update_form.is_valid():
                user_update_form.save()
                messages.success(request, 'The profile has been updated')

        case _:
            user_update_form = UpdateUser(instance=request.user)

    context = {
        "profile_activate": "active",
        "form": user_update_form,
    }

    return render(request, "main/profile.html", context)

@login_required
def delete(request):
    request.user.delete()
    return render(request, "authentication/delete.html")

@login_required
def create_post(request):
    match request.method:
        case "POST":
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                request.user.post_set.create(title=request.POST["title"], content=request.POST["content"])
                messages.success(request, "A new post was added successfully")
                return redirect("home")
        case _:    
            post_form = PostForm()
            
    context = {
        "form": post_form,
        "title": "Create Post",
        "submit_value": "Post",
        "heading": "Create Post"
    }
    return render(request, "main/post.html", context)

@login_required
def update_post(request, pk):
    match request.method:
        case "POST":
            post_form = PostForm(request.POST, instance=request.user.post_set.get(id=pk))
            if post_form.is_valid():
                post_form.save()
                messages.success(request, "Post was updated successfully")
                return redirect("home")
        case _:    
            post_form = PostForm(instance=request.user.post_set.get(id=pk))
            
    context = {
        "form": post_form,
        "title": "Update Post",
        "submit_value": "Update",
        "heading": "Update Post"
    }
    return render(request, "main/post.html", context)

@login_required
def delete_post(request, pk):
    request.user.post_set.get(id=pk).delete()
    messages.success(request, "Post was deleted successfully")
    return redirect("home")