from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .bigboytimer import *
from twitterhandler.settings import QUERY_INTERVAL, TOGGLE_TOKEN

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

timer = BigBoyTimer(QUERY_INTERVAL)

timer_dict = {
    True: "started",
    False: "stopped"
}


@login_required(login_url='/admin/')
def index(request):
    context = {}
    print(timer.is_running)
    return render(request, "index.html", context)


@api_view(["POST"])
def toggle(request):
    context = {}
    if request.method == "POST":
        if "token" in request.data and request.data["token"] == TOGGLE_TOKEN:
            print(request.path_info)
        else:
            context["state"] = "FUCK YOU"
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        timer.toggle()
        context["state"] = timer_dict[timer.is_running]
        print(context["state"])
        return Response(context, status=status.HTTP_200_OK)
