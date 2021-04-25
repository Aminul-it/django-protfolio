
from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact/',views.contact.as_view(),name='contact'),
    path('success',views.success,name='success'),
    path('serv/',include('serv.urls')),
    path('edu/',include('edu.urls')),
]
