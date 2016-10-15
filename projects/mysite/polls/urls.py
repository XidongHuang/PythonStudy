"""*************************************************************************
    > File Name: polls/urls.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Thu 13 Oct 20:19:14 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

from django.conf.urls import url

from . import views

urlpatterns = [
				url(r'^$', views.index, name="index"),
			  ]
