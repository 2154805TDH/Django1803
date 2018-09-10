from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Teacher

# Create your views here.
def get_teachers(req):
    result = Teacher.objects.all()
    return render(req, 'teachers.html',context={'teachers': result})

def get_teachers_v1(req):
    # 加载模板
    template = loader.get_template('teachers.html')
    print(template)
    print(dir(template))
    # 拿数据
    result = Teacher.objects.all()
    res = template.render({'teachers': result})
    return HttpResponse(res)

def get_teacher(req, i):
    teacher = Teacher.objects.filter(pk=i)
    return render(req, 'teacher.html', {'teacher':teacher})

def index(req):
    return render(req, 'index.html')
def indexplus(req):
    return render(req, 'indexplus.html')
def school_index(req):
    return render(req, 'school.html')