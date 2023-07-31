from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = [
        'post_no',
        'title',
        'username',
        'created_time',
        'updated_time',
    ]

    sortable_by = [
        'post_no',
        'title',
        'created_time',
        'updated_time',
    ]

    list_filter = [
        'username',
    ]