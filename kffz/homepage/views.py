#coding=UTF-8
from django.shortcuts import render, redirect, HttpResponse
import datetime
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.generic import ListView, DetailView
from homepage.forms import SignupForm
from django.contrib.auth import get_user_model
from . import models
from comment.forms import CommentForm
import markdown
from django.db.models import Q
from django.http import JsonResponse
import json

# Create your views here.


class IndexView(ListView):
    model = models.Blog
    template_name = 'index.html'
    context_object_name = 'blog_list'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range
        if page_number == 1:
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last
        }
        return data


class Article_list(IndexView):
    template_name = 'articles-list.html'

class Faq_list(IndexView):
    template_name = 'faq.html'

class Contact_list(IndexView):
    template_name = 'contact.html'

class diy(IndexView):
    template_name = 'diy.html'

class child(IndexView):
    template_name = 'child1.html'

class more(IndexView):
    template_name = 'more1.html'


def signup(request):
    path = request.get_full_path()
    if request.method == 'POST':
        form = SignupForm(data=request.POST, auto_id="%s")
        if form.is_valid():
            UserModel = get_user_model()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = UserModel.objects.create_user(username=username, email=email, password=password)
            user.save()
            auth_user = authenticate(username=username, password=password)
            auth_login(request, auth_user)
            return redirect('/')
    else:
        form = SignupForm(auto_id='%s')
    return render(request, 'signup.html', locals())


def logout_view(request):
    logout(request)
    return redirect('/')


class BlogDetailView(DetailView):
    model = models.Blog
    template_name = 'single.html'
    context_object_name = 'blog'

    def get(self, request, *args, **kwargs):
        response = super(BlogDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        blog = super(BlogDetailView, self).get_object(queryset=None)
        blog.detail = markdown.markdown(blog.detail,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc'
                                        ])
        return blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        form = CommentForm
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'base.html', {'error_msg': error_msg})
    search_blog_list = models.Blog.objects.filter(Q(detail__contains=q) | Q(title__contains=q))
    return render(request, 'base.html', {'error_msg': error_msg, 'search_blog_list': search_blog_list})
