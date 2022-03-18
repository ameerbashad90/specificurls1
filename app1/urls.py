from app1.views import kurnool
from django.urls import path
app_name='app1'
urlpatterns=[
    path('kurnool/',kurnool,name='kurnool'),
]
