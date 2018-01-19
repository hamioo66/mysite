# -*-coding:UTF-8 -*-
# from django.template import loader,Context
# from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Blog,Tag
from django.http import Http404
from django.utils import timezone
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    # posts = Blog.objects.all()
    # t = loader.get_template('../templates/index.html')
    # c = Context({'posts': posts})
    # return HttpResponse(t.render(c))
    # 分页

    blogs = Blog.objects.all()
    p = Paginator(blogs, 4)
    print('页码数量', p.num_pages)
    page = request.GET.get('page', 1)
    loaded = p.page(page)
    return render_to_response("index.html", {"blogs": blogs}, {"item_info": loaded})


def blog_show(request, id=''):
    try:
        blogs = Blog.objects.get(id=id)
        # # 获取当前时间
        # time = timezone.localtime(timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html", {"blogs": blogs})