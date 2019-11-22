from django.http import HttpResponse, JsonResponse

from .ml.ml_business_handler import MLBusinessHandler

handler = MLBusinessHandler()


def health(request):
    return JsonResponse({"Status": "Up"})


def check_spacy(request):
    return JsonResponse(handler.check_spacy(request))
