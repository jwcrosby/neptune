from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('dives/', views.dives_index, name='dives_index'),
    path('dives/<int:dive_id>/', views.dives_detail, name='dives_detail'),
    path('dives/create/', views.DiveCreate.as_view(), name='dives_create'),
    path('dives/<int:pk>/update/', views.DiveUpdate.as_view(), name='dives_update'),
    path('dives/<int:pk>/delete/', views.DiveDelete.as_view(), name='dives_delete'),
    path('dives/<int:dive_id>/add_photo/', views.add_photo, name='add_photo'),
    path('dives/<int:dive_id>/add_note/', views.add_note, name='add_note'),
    path('dives/<int:dive_id>/assoc_buddy/<int:buddy_id>/', views.associate_buddy_with_dive, name='associate_buddy_with_dive'),
    path('buddies/create/', views.BuddyCreate.as_view(), name='buddies_create'),
    path('buddies/<int:pk>/', views.BuddyDetail.as_view(), name='buddies_detail'),
    path('buddies/', views.BuddyList.as_view(), name='buddies_index'),
    path('buddies/<int:pk>/update/', views.BuddyUpdate.as_view(), name='buddies_update'),
    path('buddies/<int:pk>/delete/', views.BuddyDelete.as_view(), name='buddies_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
