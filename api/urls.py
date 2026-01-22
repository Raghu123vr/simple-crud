from django.urls import path,include
from .views import Employee
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employee',Employee)
urlpatterns=[
    path('', include(router.urls))

]