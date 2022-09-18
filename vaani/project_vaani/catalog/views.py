from django.shortcuts import render
from django.core.files.base import File
from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404

from .forms import *

from .models import *
#using class based view
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
#using classbased views
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class IntroPageView(TemplateView):
    template_name = 'vaani_intro.html'

class RecordPageView(TemplateView):
    template_name = 'vaani_record.html'

class UploadPageView(TemplateView):
    template_name = 'vaani_upload.html'

class TestPageView(TemplateView):
    template_name = 'vaani_test.html'

class ResultsPageView(TemplateView):
    template_name = 'vaani_final.html'

def intro_view(request):
    context = {
    "songs": ["Enna Sona", "Raabta", "Sooraj Dooba Hai", "Gulaabi Ankhein"],
    }
    return render(request, "vaani_intro.html", context)

def toggle_button_view(request):
    if request.POST.get('action') == 'toggle_button':
        token = request.POST.get('csrfmiddlewaretoken')
        id = request.POST.get("id")
        #print (token)
        print (id)
    return render(request, "vaani_intro.html")

def Audio_store(request):
    if request.method == 'POST': 
        form = AudioForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            form.save() 
            return HttpResponse('successfully uploaded')
    else: 
        form = AudioForm() 
    return render(request, 'vaani_upload.html', {'upload' : form}) 



