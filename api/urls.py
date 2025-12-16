from django.urls import path
from . import views
from . import authentication

urlpatterns = [
    path('test/', views.test_api, name='test'),
    path('hello/', views.hello, name='hello'),
    path('test1/', authentication.testapi_2, name='test1'),
]