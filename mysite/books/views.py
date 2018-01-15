from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db.models import Q
from models import Book, Publisher
from forms import ContactForm, PublisherForm
from django.core.mail import send_mail
# Create your views here.
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("../templates/search.html",{
        "results": results,
        "query": query,
    })
def contact(request):
    if request.method =='post':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic =form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender', 'noreply@example.com')
            send_mail(
                'Feedback from your site,topic' % topic,
                message,sender,
                ['aministrator@example.com']
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('../templates/contact.html',{'form':form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_publisher/thanks/')
    else:
        form = PublisherForm()
    return render_to_response('../templates/add_publisher', {'form': form})