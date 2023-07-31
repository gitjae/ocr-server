from django.urls import path
#from .views import get_board_all
from .views import *

urlpatterns = [
    #path('', get_board_all)
    path('', Boards.as_view()),
    path('board/<int:post_no>', BoardDetail.as_view())
]