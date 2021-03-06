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

app_name = 'polls'
urlpatterns = [
				# ex: /polls/
				url(r'^$', views.IndexView.as_view(), name="index"),
				# ex: /polls/5
				url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
				# ex: /polls/5/results/
				url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name="results"),
				# ex: /polls/5/vote/
				url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
			  ]
