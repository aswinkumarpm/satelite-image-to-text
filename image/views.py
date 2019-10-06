# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import StringIO

from PIL import Image
from PIL import ImageFile
import pytesseract
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from forms import UploadForm
from image.models import FileUpload, ImageUser
from serializers import PhotoSerializer

ImageFile.LOAD_TRUNCATED_IMAGES = True


def mapview(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
    context = {
        "data": "title",
        "latitude" : "10.639436",
        "longitude" : "76.015007",
    }

    return render(request, 'maps.html', context)


def upload(request):
    if request.method == 'POST':
        print request.POST
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        cd = form.cleaned_data
        image_field = cd.get('photo')
        img = str(image_field)
        img_name, img_extension = img.split(".")

        image_file = StringIO.StringIO(image_field.read())
        image = Image.open(image_file)
        h = pytesseract.image_to_string(image)
        t = str(unicode(h).encode('utf8'))
        f = open("guru99.txt", "w+")
        f.write(t)
        photodetails = FileUpload()
        photodetails.text = t
        photodetails.photo = image_field
        photodetails.save()
        response = HttpResponse(t, content_type='text/plain')
        f.close()
        response['Content-Disposition'] = 'attachment;filename="' + img_name + '-converted.txt' '"'
        # return response and HttpResponseRedirect('map_view')
        return response

    query = FileUpload.objects.order_by('-id')[:1].values_list('latitude', flat=True)
    # lat = query.values_list('latitude', flat=True)
    p = []
    for item in query:
        p.append(item)

    context = {
        "form": form,
        "latitude" : p,
    }
    return render(request, 'image-to-text.html', context)


def file_list(request):
    queryset_list = FileUpload.objects.all()
    context = {
        "objects_list": queryset_list,
    }
    return render(request, 'list.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (ImageUser.objects.filter(username=username).exists() or ImageUser.objects.filter(email=email).exists()):
                ImageUser.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

        else:
            return HttpResponse("Correct Your forms")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@csrf_exempt
def photo_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        photos = FileUpload.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def photo_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        photos = FileUpload.objects.get(pk=pk)
    except FileUpload.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PhotoSerializer(photos)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PhotoSerializer(photos, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        photos.delete()
        return HttpResponse(status=204)