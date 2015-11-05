from django.shortcuts import render_to_response
from django.http import HttpResponse
from Search.models import *
import json

def index(request):
    return render_to_response("searchresults.html",{})

def search(request):
    if request.method == 'GET' and 's' in request.GET:
        quer = request.GET['s']
        if quer is not None:
            results = Results.objects.filter(content__icontains=quer)
            json_list = []
            for re in results:
                json_list.append(re.content)
            return HttpResponse(json.dumps(json_list,ensure_ascii=False))





