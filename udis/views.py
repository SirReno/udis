from django.shortcuts import render
import requests
from django.core import serializers
from django.http import JsonResponse


def home(request):
    return render(request, '../templates/home.html')

def udis(request):
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')

    url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257/datos/' + startDate + '/'+endDate
    headers = {'content-type': 'application/json',
               'Bmx-Token': 'ea5d1a78b04c3fe4066ada107796ac81500d9551f81935a3a18d8482eb317928'}
    payload = {}
    r = requests.get(url, payload, headers=headers)

    data = r.json()

    dates = []
    values = []

    max = 0
    min = 999999999
    average = 0

    for days in data['bmx']['series'][0]['datos']:
        dates.append(days['fecha'])
        values.append(days['dato'])
        average += float(days['dato'])

        if (float(days['dato']) > max): max = float(days['dato'])

        if (float(days['dato']) < min): min = float(days['dato'])

    average = average / len(data['bmx']['series'][0]['datos'])


    return JsonResponse(data={
        'labels': dates,
        'data': values,
        'max': max,
        'min': min,
        'average': average
    })


def dollars(request):
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')

    url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF63528/datos/' + startDate + '/'+endDate
    headers = {'content-type': 'application/json',
               'Bmx-Token': 'ea5d1a78b04c3fe4066ada107796ac81500d9551f81935a3a18d8482eb317928'}
    payload = {}
    r = requests.get(url, payload, headers=headers)

    data = r.json()

    dates = []
    values = []

    max = 0
    min = 999999999
    average = 0

    for days in data['bmx']['series'][0]['datos']:
        dates.append(days['fecha'])
        values.append(days['dato'])
        average += float(days['dato'])

        if(float(days['dato']) > max): max = float(days['dato'])

        if(float(days['dato']) < min): min = float(days['dato'])

    average = average/len(data['bmx']['series'][0]['datos'])

    return JsonResponse(data={
        'labels': dates,
        'data': values,
        'max': max,
        'min': min,
        'average': average
    })
