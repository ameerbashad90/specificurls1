from app2.views import anantapur
from django.urls import path
app_name='app2'
urlpatterns=[
    path('anantapur/',anantapur,name='anantapur'),
]