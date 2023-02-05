from django.urls import path
from . import views
urlpatterns = [
    path('', views.VideoList.as_view(),name='index'),
    path('search/', views.SearchResultView.as_view(),name='search')
]
