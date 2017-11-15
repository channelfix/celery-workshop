# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


DL_STATUS = (
    (0, 'PENDING'),
    (1, 'IN_PROGRESS'),
    (2, 'SUCCESS'),
    (3, 'FAIL')
)


class DownloadRequest(models.Model):
    youtube_url = models.URLField()
    downloaded_file = models.FileField(
        null=True, blank=True, upload_to='videos/')
    status = models.PositiveIntegerField(choices=DL_STATUS, default=0)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    remarks = models.TextField(blank=True)

    # some constants
    PENDING = 0
    IN_PROGRESS = 1
    SUCCESS = 2
    FAIL = 3

    def __str__(self):
        return self.youtube_url
