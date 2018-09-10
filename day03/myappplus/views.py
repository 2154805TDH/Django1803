from django.http import HttpResponse
from django.shortcuts import render
from .models import Person, BankCard, Engineer, Language, Book, Author
# Create your views here.

def get_person_by_bank(req):
    bank = BankCard.objects.all().first()
    return HttpResponse(bank.person)

def rem_bankcard(req):
    bankcard = BankCard.objects.all().first()
    bankcard.delete()
    return HttpResponse('删除成功')

def get_engineer_by_desc(req):
    # 需求; 找工程师所用语言的描述包括人生苦短
    engineer = Engineer.objects.filter(
        language__desc__contains='人生苦短'
    )
    return HttpResponse(engineer)

def get_engineer_by_des(req):
    # 需求; 找工程师所用语言的描述包括人生苦短
    lang = Language.objects.get(desc__contains='人生苦短')
    eng = lang.engineer_set.all()
    # engineer = Engineer.objects.filter(
    #     language__desc__contains='人生苦短'
    # )
    return HttpResponse(eng)

def get_engineer_by_language(req):
    my_python = Language.objects.get(id=2)
    # 获取会python的工程师
    res = my_python.engineer_set.all()
    return HttpResponse(res)

def get_author_by_book(req):
    book = Book.objects.get(pk=1)
    authors = book.authors.all()
    print(authors)
    print(dir(authors))
    return HttpResponse(authors)
def get_book_by_author(req):
    author = Author.objects.get(name='阿达')
    books = author.book_set.all()
    print(books)
    print(dir(books))
    return HttpResponse(books.all())