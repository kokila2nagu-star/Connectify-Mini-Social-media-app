from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Post, Like, Comment, Follow
from .forms import PostForm

def landing(request):

    return render(
        request,
        "landing.html"
    )


@login_required
def home(request):

    posts = Post.objects.all().order_by('-created_at')


    if request.method == "POST":

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect("home")

    else:
        form = PostForm()



    # Suggested users

    suggested_users = User.objects.exclude(
        id=request.user.id
    )



    following_ids = Follow.objects.filter(
        follower=request.user
    ).values_list(
        "following_id",
        flat=True
    )



    for post in posts:

        post.is_following = Follow.objects.filter(
            follower=request.user,
            following=post.user
        ).exists()



    context = {

        "posts": posts,

        "form": form,

        "suggested_users": suggested_users,

        "following_ids": list(following_ids)

    }



    return render(
        request,
        "home.html",
        context
    )





@login_required
def like_post(request,id):

    post = get_object_or_404(
        Post,
        id=id
    )


    liked = Like.objects.filter(
        user=request.user,
        post=post
    ).exists()


    if liked:

        Like.objects.filter(
            user=request.user,
            post=post
        ).delete()

    else:

        Like.objects.create(
            user=request.user,
            post=post
        )


    return redirect("home")





@login_required
def add_comment(request,id):

    post = get_object_or_404(
        Post,
        id=id
    )


    if request.method == "POST":

        text = request.POST.get("comment")


        Comment.objects.create(
            user=request.user,
            post=post,
            text=text
        )


    return redirect("home")





@login_required
def follow_user(request,username):

    user_to_follow = get_object_or_404(
        User,
        username=username
    )


    existing = Follow.objects.filter(
        follower=request.user,
        following=user_to_follow
    )



    if existing.exists():

        existing.delete()

    else:

        Follow.objects.create(
            follower=request.user,
            following=user_to_follow
        )



    return redirect(
        "profile",
        username=username
    )





@login_required
def profile(request,username):

    user_profile = get_object_or_404(
        User,
        username=username
    )


    posts = Post.objects.filter(
        user=user_profile
    ).order_by(
        "-created_at"
    )


    followers_count = Follow.objects.filter(
        following=user_profile
    ).count()



    following_count = Follow.objects.filter(
        follower=user_profile
    ).count()



    is_following = Follow.objects.filter(
        follower=request.user,
        following=user_profile
    ).exists()



    context = {

        "profile_user": user_profile,

        "posts": posts,

        "followers_count": followers_count,

        "following_count": following_count,

        "is_following": is_following

    }



    return render(
        request,
        "profile.html",
        context
    )
@login_required
def messages_page(request):
    return render(request, "messages.html")


@login_required
def groups_page(request):
    return render(request, "groups.html")


@login_required
def notifications_page(request):
    return render(request, "notifications.html")


@login_required
def settings_page(request):
    return render(request, "settings.html")