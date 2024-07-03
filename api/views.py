from django.shortcuts import render
from django.http import JsonResponse
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/testapi")
def test(request):
    return JsonResponse({"message": "im fine!"})
