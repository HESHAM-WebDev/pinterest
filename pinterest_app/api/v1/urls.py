from django.urls import path
from pinterest_app.api.v1 import views

app_name = 'pinterest'
urlpatterns = [
    # path('boards', views.board_list, name='board_list'),
    # path('board/<int:id>', views.board_detail, name='board_detail'),
    # path('board/create', views.board_create, name='board_create'),
    # path('delete/<int:id>', views.board_delete, name='board_delete'),
    # path('<int:id>/update', views.board_update, name='board-update'),
    path('users', views.users_list, name='users_list'),
    path('user/<int:id>', views.user_detail, name='user_detail'),
    path('pins', views.pin_list, name='pin_list'),
    path('pin/<int:id>', views.pin_detail, name='pin_detail'),
    path('pin/create', views.pin_create, name='pin_create'),
    path('delete/<int:id>', views.pin_delete, name='pin_delete'),
    path('pin/<int:id>/update', views.pin_update, name='pin-update'),
]