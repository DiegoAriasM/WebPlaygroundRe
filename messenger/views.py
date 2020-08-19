from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread
from django.http import Http404
<<<<<<< HEAD
=======

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
>>>>>>> ce65623273b556746ccc40492f20886a80804799

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
<<<<<<< HEAD
@method_decorator(login_required, name="dispatch")
=======
@method_decorator(login_required, name="disparch")
>>>>>>> ce65623273b556746ccc40492f20886a80804799
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
<<<<<<< HEAD
            raise Http404()
        return obj
=======
            raise Http404
        return obj
>>>>>>> ce65623273b556746ccc40492f20886a80804799
