from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ourstory.models import Article,Category
from datetime import datetime
from django.http import Http404
# Create your views here.
 
def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'ourstory/home.html', {'post_list': post_list})
 
def Test(request):
    return render(request,'ourstory/test.html',)
 
def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'ourstory/post.html',{'post':post})


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'ourstory/home.html', context={'post_list': post_list})