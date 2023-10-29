from django.urls import path
from.import views
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
]