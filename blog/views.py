from django.shortcuts import render
from .models import Post
from .forms import CommentForm



def blog_index(request):
    """
        display a list of all your posts
    """
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    """
        posts viewed will only be of a specific category
        chosen by the user.
    """

    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')   # order by largest value

    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    """
        display the full post as well as comments and
        a form to allow users to create new comments.
    """

    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }
    return render(request, "blog_detail.html", context)
