from django.db import models

# Create your models here.

# 資料表建議使用單數名稱
class book(models.Model):
    bookname  = models.CharField(max_length=20, null=False, verbose_name='書名')
    author    = models.CharField(max_length=20, null=False, verbose_name='作者')
    publisher = models.CharField(max_length=20, verbose_name='出版社')
    pubdate   = models.DateField(verbose_name='出版日期')
    price     = models.IntegerField(verbose_name='定價')
    content   = models.TextField(verbose_name='詳細內容')
    def __str__(self):
        return self.bookname +'  '+ self.author