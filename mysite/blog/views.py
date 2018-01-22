# -*-coding:UTF-8 -*-
# from django.template import loader,Context
# from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Blog,Comment
from django.http import Http404
from mysite.blog.forms import CommentForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    # posts = Blog.objects.all()
    # t = loader.get_template('../templates/index.html')
    # c = Context({'posts': posts})
    # return HttpResponse(t.render(c))
    # 分页

    blogs = Blog.objects.all().order_by(('-publish_time'))
    p = Paginator(blogs, 4)
    print('页码数量', p.num_pages)
    page = request.GET.get('page', 1)
    loaded = p.page(page)
    return render_to_response("index.html", {"blogs": blogs}, {"item_info": loaded})


def get_details(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            clean_data['blog'] = blog
            Comment.objects.create(**clean_data)
    return render_to_response("blog_show.html", {"blog": blog})