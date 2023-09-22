from django.shortcuts import render
from django.http import HttpResponse

def vistagbnlv(request):
    html="""
    <h1 style="color:blue">Hola mundo</h1>
    """
    return HttpResponse(html)