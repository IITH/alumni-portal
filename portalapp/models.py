from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=255)
    # TODO(rushiagr): password not secret. Make it
    password = models.CharField(max_length=255)
