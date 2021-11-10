from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.crypto import get_random_string

from .models import Url
# Create your views here.


def generate_random_id():
    return get_random_string(length=6)


@csrf_exempt
def short(request):
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        url = body['url']

        random_id = generate_random_id()

        while True:
            try:
                Url.objects.get(shortened=random_id)
                random_id = generate_random_id()
            except Url.DoesNotExist:
                break

        print(random_id)

        url_to_save = Url(redirect=url, shortened=random_id)
        url_to_save.save()

        response = {
            "status": "success",
            "path": random_id
        }

        return JsonResponse(response)

    return JsonResponse({"satuts": "FAILED"})
