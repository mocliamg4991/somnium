from django.urls import  path
from api import views

urlpatterns = [
    path(r'profile/', views.ProfileList.as_view()),
    path(r'profile/<int:pk>/', views.ProfileDetail.as_view()),
    path(r'positions/', views.PositionList.as_view()),
    path(r'subdivisions/', views.SubdivisionList.as_view()),
]
