from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', TemplateView.as_view(template_name='LibraLoom/home.html'), name='home'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('advance-search/', views.advanced_search, name='advance_search'),
    path('anybook/', views.anybook_pdf, name='anybook'),
    path('profile/', views.profile, name='profile'),  # This view requires authentication
    path('book-details/<int:book_id>/', views.book_details, name='book_details'),
    path('reserve/<int:book_id>/', views.reserve_book, name='reserve_book'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),
    path('search-book/', views.search_book, name='search_book'),
    path('generate_summary/', views.generate_summary, name='generate_summary'),

]
