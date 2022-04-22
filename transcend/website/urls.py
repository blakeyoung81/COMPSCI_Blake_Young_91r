
from xml.dom.minidom import Document
from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Home.html', views.home, name='home'),
    path('Contact.html', views.contact, name ='contact'),
    path('About.html', views.about, name = 'about'),
    path('Preferences.html', views.preferences, name = 'preferences'),
    path('Register.html', views.register, name = 'register'),
    path('Login.html', views.login, name = 'login'),
    path('My-DNA.html', views.myDNA, name = 'myDNA'),
    path('Offspring-DNA.html', views.offspringDNA, name = 'offspringDNA'),
    path('Upload.html', views.upload, name = 'upload'),
    path('Mate-DNA.html', views.mateDNA, name = 'mateDNA'),
    path('', include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)