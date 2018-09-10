from django.core.serializers import json
from django.forms import model_to_dict
from django.shortcuts import render, HttpResponse
from .models import Category, Goods, Author, Book


# Create your views here.
def cates(req):
    resul = Category.objects.all().order_by('-id')
    return render(req, 'cates.html', {'res':resul, 'title':'分类列表'})

def catel(req):
    print(req)
    c_desc = req.GET.get('c_desc')
    res = Category.objects.get(desc=c_desc)
    print(dir(req))
    print(res)
    return HttpResponse(res)

def cate_filter(req):
    # 拿参数
    key_word = req.GET.get('kw')
    # 查数据库 __contains 类似于SQL里面的like
    res = Category.objects.filter(name__contains=key_word)
    print(res)
    return HttpResponse(res)

def cates_filter_in(req):
    # pk是主键的缩写
    res = Category.objects.filter(pk__in=[0,2])
    return HttpResponse(res)

def get_goods_by_datetime(req):
    my_time = req.GET.get('time')
    # 通过年份去查询
    res = Goods.objects.filter(in_datetime__year=my_time)
    # res = Goods.objects.filter(in_datetime__day=my_time)
    print(res)
    return HttpResponse(res)

def get_book_by_author(req):
    a_id = req.GET.get('a_id')
    author = Author.objects.get(pk=int(a_id))
    res = author.book_set.all()
    return HttpResponse(res)

def get_author_by_book(req):
    b_id = req.GET.get('b_id')
    books = Book.objects.get(pk=int(b_id))
    res = books.authors.all()
    return HttpResponse(res)