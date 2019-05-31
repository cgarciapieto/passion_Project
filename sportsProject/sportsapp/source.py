import datetime
from django.db import models


class Source(models.Model):
    id = models.Column(models.IntegerField, primary_key=True)
    title = models.Column(models.Text, nullable=False)
    subtitle = models.Column(models.Text, nullable=False)
    link = models.Column(models.Text, nullable=False)
