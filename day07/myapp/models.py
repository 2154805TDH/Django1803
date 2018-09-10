from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='游戏名字'
    )
    desc = models.CharField(
        max_length=251,
        verbose_name='简介'
    )
    rate = models.FloatField(
        verbose_name='评分'
    )
    def __str__(self):
        return self.name


class Humen(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='角色名字'
    )
    player = models.ForeignKey(
        'Player',
        verbose_name='所属游戏'
    )
    def __str__(self):
        return self.name