from django.urls import path, include
from rest_framework import routers

#from Course.views import CourseViewSet
from appcapacit  import views


router= routers.DefaultRouter()
router.register(r'Course',views.CourseViewSet)
router.register(r'User',views.UserViewSet)
router.register(r'Teacher',views.UserViewSet)
#----
urlpatterns = [
     path('', include(router.urls)),
]