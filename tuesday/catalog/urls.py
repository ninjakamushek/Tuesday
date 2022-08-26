from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('', views.index, name='index'),
    path('boards/', views.BoardListView.as_view(), name='boards'),
    path('board/<int:pk>', views.BoardDetailView.as_view(), name='board-detail'),
    path('profile/', profile, name='profile'),
    path('change_task/', views.change_task, name='change_task')
]
