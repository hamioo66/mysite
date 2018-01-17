# from django.template import loader,Context
# from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Blog
from django.http import Http404


# Create your views here.
def index(request):
    # posts = Blog.objects.all()
    # t = loader.get_template('../templates/index.html')
    # c = Context({'posts': posts})
    # return HttpResponse(t.render(c))
    blogs = Blog.objects.all()
    return render_to_response("index.html", {"blogs": blogs})


def blog_show(request, id=''):
    try:
        blogs = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html", {"blogs": blogs})
