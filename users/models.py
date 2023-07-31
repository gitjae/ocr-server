from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)

    # 나만의 필드
    name = models.CharField(max_length=200, default="", blank=True) # blank : form에서 인풋박스가 비어있어도 되는지
                                                        #null = True            # null : 데이터베이스에 null로 저장되어도 되는지
