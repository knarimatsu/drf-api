from django.db import models

# Create your models here.

# Taskモデルを作成(データベースでTaskテーブルを作成)
class Task(models.Model):
    # titleカラムを作成最大文字数は50
    title = models.CharField(max_length=50)
    # 作成された時間を自動で入力
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新された時間を自動で入力
    updated_at = models.DateTimeField(auto_now=True)

    # タイトルを返す。管理画面でタスクを見やすくするため
    def __str__(self):
        return self.title