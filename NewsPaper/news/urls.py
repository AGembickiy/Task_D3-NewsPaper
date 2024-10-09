from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('news/', new, name = 'news'),
    path('news/<int:postid>/', newid, name = 'new'),

]