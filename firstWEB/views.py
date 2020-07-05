from datetime import datetime
from urllib import request
import json

from django.forms import model_to_dict
from django.shortcuts import render
from django.http.response import JsonResponse
import pymysql
import pandas as pd
from firstWEB import models
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers


# Create your views here.
# 第一个网页
def index(request):
    return render(request, 'index.html')


# 计算器
def CalPage(request):
    return render(request, 'cal.html')


def Cal(request):
    value_a = request.GET['valueA']
    value_b = request.GET['valueB']
    result = int(value_a) + int(value_b)
    cal = models.cal(value_a=value_a, value_b=value_b, result=result)
    cal.save()
    data = serializers.serialize("json", models.cal.objects.all())
    return HttpResponse(data, content_type='application/json')


# 注册表单
def register(request):
    error_msg = ""  # 刚进页面的时候，用户名还为空，此时错误信息先设置成空
    if request.method == "POST":
        username = request.POST.get("name")
        pwd = request.POST.get("pwd")
        # 对注册信息做校验
        if len(username) < 6:
            # 用户长度小于6位
            error_msg = "用户名长度不能小于6位"
        else:
            # 将用户名和密码存到数据库
            return HttpResponse("注册成功")
    return render(request, "register.html", context={"cppt": error_msg})


# peili

def sqlview(request):
    cals = models.cal.objects.all()
    json_list = []
    for cal in cals:
        json_dict = {}
        json_dict["d"] = cal.value_a
        json_dict["a"] = cal.value_b
        json_dict["r"] = cal.result

        json_dict = model_to_dict(cal)
        json_list.append(json_dict)
    data = json.dumps(json_list)
    print(data)
    ss = {"": ""}
    return JsonResponse(json_dict)


# json-mysql

def jsonview(request):
    models.student.objects.all().delete()
    s = models.student(s_id="111", s_name="sss", s_birth=datetime.now())
    s.save()
    students = models.student.objects.all()
    data = serializers.serialize("json", students)
    return HttpResponse(data, content_type='application/json')


# pymysql
def testsql(request):
    db = pymysql.connect("localhost", "root", "123456", "chendan", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM student"
    r = []
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            birthday=row[2]
            sex=row[3]

            print(row[0],row[1])
            r1 = {"s_id": id, "s_name": name,"birth":birthday,"asex":sex}
            #print(r1)
            r.append(r1)

    except:
        print("Error: unable to fecth data")
    # 关闭数据库连接

    db.close()
    #print(r)
    return HttpResponse(json.dumps(r), content_type='application/json')
