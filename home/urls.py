from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('couple/', views.couple, name='about'),
    path('gallery/', views.gallery, name='about'),
    path('contact/', views.contact, name='about'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)