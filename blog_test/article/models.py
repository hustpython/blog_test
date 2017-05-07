from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客分类 可为空
    #tag = models.ManyToManyField(Tag, blank=True)  # 博客标签 可为空
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

    class Meta:
        ordering = ['-date_time']
