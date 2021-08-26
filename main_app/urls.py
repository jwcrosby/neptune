from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dives/', views.dives_index, name='dives_index'),
  path('dives/<int:dive_id>/', views.dives_detail, name='dives_detail'),
  path('dives/create/', views.DiveCreate.as_view(), name='dives_create'),
  path('dives/<int:dive_id>/add_note/', views.add_note, name='add_note'),
]
