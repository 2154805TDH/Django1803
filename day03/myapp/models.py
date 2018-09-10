from django.db import models

# Create your models here.
class Cla(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='班级'
    )
    class Meta:
        db_table = 'clazz'
    def __str__(self):
        return self.name

class Stu(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='名字'
    )
    age = models.IntegerField(default=1)
    cla = models.ForeignKey(
        Cla,
        verbose_name='所在班级'
    )
    class Meta:
        db_table = 'stu'
    def __str__(self):
        return self.name


class tea(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='名字'
    )
    clas = models.ManyToManyField(
        Cla,
        verbose_name='负责班级'
    )
    class Meta:
        db_table = 'tea'
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='球队名字',
        # 索引
        db_index=True
    )
    country = models.CharField(
        max_length=30,
        verbose_name='所属国家'
    )
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='名字'
    )
    age = models.IntegerField(
        verbose_name='年龄'
    )
    count = models.IntegerField(
        verbose_name='火力输出'
    )
    team = models.ForeignKey(
        Team,
        verbose_name='所属球队',
        null=True
    )
    def __str__(self):
        return self.name