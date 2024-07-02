from django.shortcuts import render
from django.http import JsonResponse
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/test1")
def test(request):
    return JsonResponse({"message": "im fine!"})
