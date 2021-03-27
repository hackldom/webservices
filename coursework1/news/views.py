from django.shortcuts import render
from rest_framework import viewsets
from .models import NewsStory, Author
from .serializers import NewsStorySerializer, AuthorSerializer
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import json


def LoginRedirect(request):
    return HttpResponse('You need to log in to access this page', status=403)

@csrf_exempt
def HandleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # if request.user.is_authenticated:
                login(request, user)
                print('successful login')
                return HttpResponse('You have been logged in, welcome to the server', status=200)
            # print('User is not authenticated')
            # return HttpResponse('You are already logged in', status=400)
        else:
            return HttpResponse('Invalid Login')
    else:
        return HttpResponse('Invalid Request Type', status=400)

@csrf_exempt
def HandleLogout(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
            return HttpResponse('You have been successfully logged out', status=200)
        return HttpResponse('You cannot logout if you aren\'t logged in', status=400)
    return HttpResponse('You cannot logout with a GET request', status=400)

@csrf_exempt
@login_required(login_url='/notloggedin')
def PostStory(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewsStorySerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=503)
    return HttpResponse('Invalid Request Type', status=400)


def GetAuthor(request):
    if request.method == 'GET':
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'error message'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    
@csrf_exempt
@login_required(login_url='/notloggedin')
def DeleteStory(request):
    if request.method == 'POST':
        story_key = json.loads(request.body)
        key_to_delete = story_key['story_key']
        if NewsStory.objects.filter(id=key_to_delete).delete():
            return HttpResponse("news story with id " + key_to_delete + " has been deleted", status=200)
        return HttpResponse("news id does not exist", status=503)   


class NewsStoryView(viewsets.ModelViewSet):

    queryset = NewsStory.objects.all()
    serializer_class = NewsStorySerializer

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


