from django.contrib import admin
from ourstory.models import Article,Category,Tag
from django_summernote.admin import SummernoteModelAdmin# 给content字段添加富文本
# Register your models here.
 
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)  # 给content字段添加富文本
 
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)