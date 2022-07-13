from django.urls import path
from . import views, models

urlpatterns=[
    path('',views.home,name='hm'),
]
