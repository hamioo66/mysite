from django.template import loader,Context
from django.http import HttpResponse
from models import BlogPost

# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('../templates/index.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))