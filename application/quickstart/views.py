# -*- coding: utf-8 -*-
'''

from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from application.quickstart.serializers import UserSerializer, GroupSerializer


# Create your views here.

class UserViweSet(viewsets.ModelViewSet):

	queryset = User.objects.all().order_by('-date_joined')
	serializers_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):

	queryset = Group.objects.all()
	serializers_class = GroupSerializer

'''

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer
from bs4 import BeautifulSoup
import urllib2


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ParseBs4ViewSet(viewsets.ModelViewSet):

	def sewp(request):
		r = requests.get("http://www.vladtv.com/")

		soup = BeautifulSoup(r.content, 'html.parser')

		content = soup.find_all("a")

		for link in soup.find_all("a"):
		    link = link.get("href")

		ella = "ella"
		context = {
		    "link": link,
		    "ella": ella,
		}
		print r
		return render(request, "posts/display_soup.html", context)