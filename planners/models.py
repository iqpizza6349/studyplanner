from django.db import models


# Create your models here.
class Board(models.Model):
    username = models.ForeignKey('member.BoardMember', on_delete=models.CASCADE, null=True)

    subject = models.CharField(max_length=100, null=True)
    goal = models.TextField(null=True)
    passs = models.CharField(max_length=100, null=True)
    time = models.CharField(max_length=100, null=True)

