from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.




def get_json(request):

    return render(request,'get_json.html')


def do_json(request):

    data={
        'name':'小明',
        'age': 20,
        'sex':'男',
        'salary':10000,
        'comment':'无'

    }
    return JsonResponse(data)