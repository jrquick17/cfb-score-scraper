from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'scraper/index.html'

def scrape(self):
    print('cool')
