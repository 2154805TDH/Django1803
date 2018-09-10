from django.db import models

# Create your models here.
class BankCard(models.Model):
    num = models.IntegerField(
        verbose_name='卡号'
    )
    bankName = models.CharField(
        max_length=30,
        verbose_name='银行名字'
    )
    def __str__(self):
        return self.num
class Person(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='人名'
    )
    age = models.IntegerField()
    bankcard = models.OneToOneField(
        BankCard,
        verbose_name='银行卡',
        on_delete=models.PROTECT
    )
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(
        verbose_name='语言名字',
        max_length=30,
    )
    desc = models.CharField(
        max_length=255,
        verbose_name='描述',
    )

class Engineer(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='名字',
    )
    life = models.IntegerField(
        verbose_name='职业生涯',
    )
    language = models.ForeignKey(
        Language,
        verbose_name='掌握的语言',
    )
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='人名'
    )
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        max_length=30
    )
    authors = models.ManyToManyField(
        Author,
        verbose_name='作者'
    )
    def __str__(self):
        return self.title