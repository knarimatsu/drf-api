from django.contrib import admin
# Register your models here.
from .models import Task

# Taskモデルを管理画面で見れるようにする
admin.site.register(Task)