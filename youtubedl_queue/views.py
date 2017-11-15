# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from .tasks import queue_download

from youtubedl_queue.models import DownloadRequest


class HomeView(ListView):
    template_name = 'youtubedl_queue/home.html'
    model = DownloadRequest
    ordering = '-pk'

    def post(self, request):
        youtube_url = request.POST.get('youtube_url')
        if youtube_url:
            dl_request = DownloadRequest.objects.create(
                youtube_url=youtube_url)
            queue_download.delay(dl_request.pk)
        return redirect('/')
