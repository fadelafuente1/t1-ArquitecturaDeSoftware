import datetime

from django.db import models
from django.utils import timezone


class Comment(models.Model):
  comment_text = models.CharField(max_length=400)
  comment_date = models.DateTimeField('date commented')
  sender_ip = models.CharField(max_length=20)

  def __str__(self):
    return self.comment_text
  
  def was_commented_recently(self):
    return self.comment_date >= timezone.now() - datetime.timedelta(days=1)
  
  def get_client_ip(self, request):
      x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
      if x_forwarded_for:
          ip = x_forwarded_for.split(',')[0]
      else:
          ip = request.META.get('REMOTE_ADDR')
      return ip

  

