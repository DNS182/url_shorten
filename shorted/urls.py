from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='home'),
    path('shorted_urls/', views.shorted , name='shorted_urls'),
    path('<slug:key>/' , views.redirector , name='redirect')
]
