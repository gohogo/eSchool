from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # age = models.PositiveIntegerField(default=10)
    nickname = models.CharField(max_length=22,default='nickname')
    realname = models.CharField(max_length=22,default='realname')
    birth = models.DateField(null=True,blank=True)
    interest = models.TextField(null=True,blank=True)

    VISITOR = 0
    STUDENT = 1
    TEACHER = 2
    PARENT = 3
    ROLES = (
        (VISITOR, 'Visitor'),
        (STUDENT,
         'Student'),
        (TEACHER,
         'Teacher'),
        (PARENT, 'Parent'),
    )
    userroles = models.IntegerField(
        choices=ROLES,
        default=VISITOR)


