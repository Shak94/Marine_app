from django.urls import path
from . import views
from .models import Coral
from .models import CoralTraits

urlpatterns =[
    path('', views.Home.as_view(), name='home'),
    path('coral/about/', views.About.as_view(), name='about'),
    path('coral/', views.CoralList.as_view(), name="coral_list"),
    path('coral/new/', views.CoralCreate.as_view(), name ="coral_create"),
    path('coral/<int:pk>', views.CoralDetail.as_view(), name ="coral_detail"),
    path('coral/<int:pk>/update/',views.CoralUpdate.as_view(), name ="coral_update"),
    path('coral/<int:pk>/delete/',views.CoralDelete.as_view(), name ="coral_delete"),
    path('coral/<int:pk>/trait/new/', views.CoralTraitsCreate.as_view(), name="trait_create")

]
