from django.shortcuts import render,redirect
from homepage.models import Blog
from .models import Comment
from .forms import CommentForm

# Create your views here.
def blog_comment(request,blog_pk):
    blog = Blog.objects.filter(pk=blog_pk)[0]
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect(blog)
        else:
            comment_list = blog.comment_set.all()
            context = {
                'blog':blog,
                'form':form,
                'comment_list':comment_list
                 }
            return render(request,'homepage/templates/single.html',context=context)
    else:
        return redirect(blog)
