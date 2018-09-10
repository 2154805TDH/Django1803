from django.contrib import admin
from .models import Player, Humen


# Register your models here.

class HumenInfo(admin.TabularInline):
    # 指定model
    model = Humen
    # 指定条数
    extra = 2


class PlayerAdmin(admin.ModelAdmin):
    def get_rate_level(self):
        if self.rate >= 9:
            return '好游戏'
        else:
            return '垃圾游戏'

    get_rate_level.short_description = '评价'
    # 显示字段
    list_display = ['name', 'rate', get_rate_level]
    # 过滤器
    list_filter = ['rate', 'desc']
    # 搜索的字段
    search_fields = ['name', 'rate']
    # 分页
    list_per_page = 1
    # 分组显示
    fieldsets = [
        ('基本信息', {'fields': ('name', 'desc',)}),
        ('附加信息', {'fields': ('rate',)})
    ]
    inlines = [HumenInfo]


# 注册你的model
admin.site.register(Player, PlayerAdmin)
admin.site.register(Humen)


class MyAdmin(admin.AdminSite):
    site_header = '达达学堂'
    site_title = '免费教学'
    site_url = 'http://baidu.com'


site = MyAdmin()
site.register(Player, PlayerAdmin)
