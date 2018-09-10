from django.forms import model_to_dict
from django.shortcuts import render, HttpResponse
from django.db.models import Sum, F, Q
from .models import Cla, Stu, tea, Player, Team
import json
# Create your views here.
def get_stu(req):
    c_id = req.GET.get('c_id')
    cla = Cla.objects.get(pk=int(c_id))
    res = cla.stu_set.all()
    return HttpResponse(res)

# def get_cla(req):
#     s_id = req.GET.get('s_id')
#     stu = Stu.objects.get(pk=int(s_id))
#     res = stu.cla
#     return HttpResponse(res)
def get_cla(req):
    s_name = req.GET.get('s_name')
    stu = Stu.objects.get(name=s_name)
    s = Stu.objects.get(pk=int(stu.pk))
    res = s.cla
    return HttpResponse(res)

def get_tea_by_cla(req):
    c_id = req.GET.get('c_id')
    cla = Cla.objects.get(pk=int(c_id))
    tea = cla.tea_set.all()
    return HttpResponse(tea)

def get_cla_by_tea(req):
    t_id = req.GET.get('t_id')
    teas = tea.objects.get(pk=int(t_id))
    cla = teas.clas.all()
    return HttpResponse(cla)

def get_count(req):
    # 拿到全部数据
    players = Player.objects.all()
    # 求和
    res = players.aggregate(Sum('count'))
    print(res)
    # return HttpResponse(res['count__sum'])
    return HttpResponse(res.get('count__sum'))

def get_player(req):
    # 需求：年纪大于火力输出的数据
    player = Player.objects.filter(age__gt=F('count'))
    # 将查询出来的对象裙摆转换成数字套字典的格式
    res = [model_to_dict(i)for i in player]
    print(res,type(res))
    re =json.dumps(res)
    # print(re[1])
    return HttpResponse(re)

def get_player_by_Q(req):
    # 需求：查询年纪大于30 或者火力输出大于100
    res = Player.objects.filter(Q(age__gt=30) | Q(count__gt=100))
    ress = json.dumps([model_to_dict(i)for i in res])
    return HttpResponse(json.loads(ress)[0]['name'])