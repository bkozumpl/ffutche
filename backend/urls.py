
from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('backend', views.BackendView)
router.register('school', views.SchoolView )
router.register('scholarship', views.ScholarshipView )
router.register('tuition_fees', views.Tuition_FeesView )



urlpatterns = [
    path('', include(router.urls)),


]


