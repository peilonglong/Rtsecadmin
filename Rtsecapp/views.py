# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views import View

class Base(View):
    def get(self,request):
        return render(request,'base.html')


class Arp(View):
    def get(self,request):
        return render(request,'arp.html')

class Dos(View):
    def get(self,request):
        return render(request,'Dos.html')

#指令注入
class Command(View):
    def get(self,request):

        return render(request,'command.html')
#数据篡改
class Change(View):
    def get(self,request):
        return render(request,'change.html')

#非法操作
class Lawless(View):
    def get(self,request):
        return render(request,'lawless.html')

class Login(View):
    def get(self,request):
        return render(request,'login.html')

