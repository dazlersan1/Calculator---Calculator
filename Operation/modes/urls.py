from . import views
from django.urls import path,include

urlpatterns = [
    
    path('inverse',views.inv,name='inv'),
   
    ]
    
from django.conf import settings
from django.conf.urls.static import static

if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
