from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('login', login),
    path('board/write/', board_write),
    path('join', join),
    path('user-update', user_update),
    path('mypage', mypage),
    path('boards', board_list),
    path('ocr', OCR.as_view()),
    path('board/<int:post_no>', board),
    path('board/<int:post_no>/edit', board_update),
]