from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
#     serving html view
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
