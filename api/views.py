from django.shortcuts import render
from django.http import JsonResponse
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/testapi")
def test(request):
    return JsonResponse({"message": "im fine!"})


# -----------------------------------------------------------------------

# add apis for fetching university name, college name, course name,

# -----------------------------------------------------------------------


# -----------------------------------------------------------------------

# add apis for fetching notes and question papers

# -----------------------------------------------------------------------


# -----------------------------------------------------------------------

# add api for pdf uploads

# -----------------------------------------------------------------------
