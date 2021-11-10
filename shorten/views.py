from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, redirect, render
from .forms import SubmitUrl
from .models import Url
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.crypto import get_random_string

from .models import Url
# Create your views here.

def home(req):
    if req.method == 'POST':
        #print(request.POST)
        form = SubmitUrl(req.POST)
        context = {
            "title": "Submit URL",
            "form": form
        }
        print(context)
        if form.is_valid():
            current_url=form.cleaned_data.get('url')
            shortened = Url.shortened(url=current_url)
            redirect = Url.redirect(url=current_url)
            context={
                'title':'URL Shortened!',
                'redirect':redirect,
                'shortened':shortened
            }

            return render(req, 'home.html',context)
    else:
        form=SubmitUrl()
        context={
            "title":"Submit URL",
            "form": form
        }
        return render(req, 'shorten/home.html',context)







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

    return JsonResponse({"status": "method not allowed"})


def get_full_url(request, path):
    if request.method == "GET":

        try:
            
            full_url = Url.objects.get(shortened=path)
            print(full_url)
            return JsonResponse({"url": full_url.redirect})
        except Url.DoesNotExist:
            return JsonResponse({"status": "not found"})

    return JsonResponse({"status": "method not allowed"})