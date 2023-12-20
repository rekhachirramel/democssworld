from django.urls import path
from .views import home,project,contact
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name='home1'),
    path('project/',project,name='project'),
    path('contact/',contact,name='contact'),
]
