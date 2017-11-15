from django.conf import settings

import json

from .models import DownloadRequest

from youtube_dl import YoutubeDL


def download(dl_request):
    if dl_request.status != DownloadRequest.PENDING:
        return

    def progress_hook(d):
        print d
        if d['status'] == 'finished':
            dl_request.status = DownloadRequest.SUCCESS
            dl_request.downloaded_file = d['filename']
        elif d['status'] == 'downloading':
            dl_request.status = DownloadRequest.IN_PROGRESS
        else:
            dl_request.status = DownloadRequest.FAIL
        dl_request.remarks = json.dumps(d)
        dl_request.save()

    ydl_opts = {
        'progress_hooks': [progress_hook],
        'outtmpl': '{}videos/%(id)s.%(ext)s'.format(settings.MEDIA_ROOT)
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([dl_request.youtube_url])
