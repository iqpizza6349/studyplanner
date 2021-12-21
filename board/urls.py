from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list),
    path('write/', views.board_write),
    path('detail/<int:pk>', views.board_detail),
    path('detail/<int:pk>/remove', views.board_remove),
]
