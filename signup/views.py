from django.shortcuts import render
from django.views import generic


from .models import User

class IndexView(generic.ListView):
  model = User
  template_name = 'signup/index.html'

class ResultsView(generic.ListView):
  model = User
  template_name = 'signup/result.html'

def append(request):
  new_user = User(name=request.get['name'])
  new_user.save()