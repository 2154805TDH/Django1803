from django.shortcuts import render
from .models import *
# Create your views here.
ZH_sort = '0'
PRICE_sort = '1'
SALE_sort = '2'
def home(request):
    # 拿轮播数据
    # swipers = MyWheel.objects.all()
    swipers = MyWheel.objects.raw('SELECT * FROM axf_wheel')
    # 拿导航数据
    navs = MyNav.objects.all()
    # 拿必购数据
    mustbuy = MustBuy.objects.all()
    # 拿商店数据
    shops = MyShop.objects.all()
    shop_img = shops[0]
    shop_imgs = shops[1:3]
    goods = MainShow.objects.all()
    data = {
        'title': '首页',
        'swipers':swipers,
        'navs': navs,
        'mustbuy':mustbuy,
        'shop_img':shop_img,
        'shop_imgs':shop_imgs,
        'shop_more':shops[3:7],
        'shop_last':shops[7:],
        'goods':goods,
    }
    return render(request, 'home/home.html', data)

def market(request, type_id, sub_type_id, sort_type):
    # 拿全部的分类数据
    all_types = GoodsType.objects.all()
    # 拿商品
    goods = Goods.objects.filter(categoryid = type_id)
    # 如果二级分类的id不等于0，那就需要在原有数据集goods的基础上找
    if int(sub_type_id) != 0:
        goods = goods.filter(childcid=sub_type_id)

    # 一定先拿数据，再排序
    if sort_type == ZH_sort:
        pass
    elif sort_type == PRICE_sort:
        goods = goods.order_by('price')
    else:
        goods = goods.order_by('-productnum')
    # 通过查询出来的数据集找到选中的那个分类数据
    select_type = all_types.get(typeid = type_id)
    all_sub_type = select_type.childtypenames
    type_name_id_list = all_sub_type.split("#")
    sub_types = [i.split(':') for i in type_name_id_list]
    print(sub_types)
    data = {
        'title': '闪购',
        'all_types':all_types,
        'goods':goods,
        'select_id':type_id,
        'sub_types':sub_types,
        'selected_sub_type_id': sub_type_id,
        'sort_type':sort_type,
    }
    return render(request, 'market/market.html', data)

def cart(request):
    data = {
        'title': '购物车',
    }
    return render(request, 'cart/cart.html', data)

def mine(request):
    data = {
        'title': '我的',
    }
    return render(request, 'mine/mine.html', data)

def register_view(request):
    return render(request, 'user/register.html')

def my_login(request):
    return render(request, 'mine/mine.html')