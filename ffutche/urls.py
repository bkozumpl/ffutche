
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from backend.resources import ScholarshipResource
from users import views as user_views
from backend import views as backend_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

scholarship_resource = ScholarshipResource()

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('backend.urls')),
path('register/', user_views.register, name='register'),
path('index/', user_views.index, name='index'),
url(r'^backend/', include(scholarship_resource.urls)),
 url(r'^backend/', include('backend.urls')),
]


urlpatterns += staticfiles_urlpatterns()
