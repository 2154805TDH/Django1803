from django.core.cache import cache
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from django.views.decorators.cache import cache_page

from .models import Player
from .my_util import get_random_color
import io
import random
import time
# Create your views here.
def get_verify_img(request):
    # 画布背景颜色
    bg_color = (120, 120, 0)
    img_size = (150,70)
    # 实例化一个画布
    image = Image.new('RGB',img_size , bg_color)
    # 实例化画笔
    draw = ImageDraw.Draw(image, "RGB")
    # 设置文字颜色
    # text_color = (255,0,0)
    # 创建字体
    font_path = '/home/tan/gz1803/day07/static/fonts/ADOBEARABIC-BOLD.OTF'
    font = ImageFont.truetype(font_path, 30)
    source = 'abcdefGsjfjfljflwjJLJLJLJFJJFIJFUIURWRUUQWETIOA'
    # 保存随机的字符
    code_str = ''
    for i in range(4):
        tmp_num = random.randrange(len(source))
        random_str = source[tmp_num]
        code_str += random_str
        text_color = get_random_color()

        draw.text((10+i*30, 20), random_str, text_color, font)
    # 记录给哪个请求发了什么验证码
    request.session['code'] = code_str
    # 使用画笔将文字画到画布
    # draw.text((10, 20), "2", text_color, font)
    # draw.text((40, 20), "3", text_color, font)
    # draw.text((70, 20), "2", text_color, font)
    # 获得一个缓存区

    buf =io.BytesIO()
    # 将图片保存到缓存区
    image.save(buf, 'png')
    # 将缓存区的内容返回到前端
    return HttpResponse(buf.getvalue(), 'image/png')

def mylogin(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        params = request.POST
        # 用户输入的
        code = params.get('verify_code')
        server_code = request.session.get('code')
        print(server_code)
        if server_code.lower() == code.lower():
            print('1')
            return HttpResponse('ok')
        else:
            print('2')
            return HttpResponse('..')

@cache_page(60)
def get_data(request):
    # 假装在拼命的查数据库
    time.sleep(5)
    return HttpResponse('睡醒了')

def get_players(request):
    # 在缓存尝试拿数据
    data = cache.get('players')
    if data:
        # 如果拿到数据 直接返回
        return HttpResponse(data)
    else:
        # 没拿到 假装拿很久
        time.sleep(5)
        # 拿数据
        players = Player.objects.all()
        # 设置缓存
        cache.set('players', players, 30)
        # 把数据返回给前端
        return HttpResponse(players)


