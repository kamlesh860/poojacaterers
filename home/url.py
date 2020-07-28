
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
     # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('gallary/',views.gallary,name='gallary'),
    path('menu/',views.menu,name='menu'),
    path('contactus/',views.contactus,name='contactus'),
    path('menu/',views.menu,name='menu'),
    path('contact_us_form/',views.contact_us_form,name='contact_us_form'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)