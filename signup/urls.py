from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'signup'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
]