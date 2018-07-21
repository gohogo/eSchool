from django.db import models
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    interest = models.TextField(blank=True, null=True)

    VISITOR = 0
    STUDENT = 1
    PARENT = 2
    TEACHER = 3
    ROLES = (
        (VISITOR, 'vistor'),
        (STUDENT,
         'student'),
        (PARENT,
         'parent'),
        (TEACHER, 'teacher'),
    )
    role = models.IntegerField(
        choices=ROLES,
        default=VISITOR)
    nickname = models.CharField(max_length=255,verbose_name='昵称',blank=True, null=True)
    Phone = models.BooleanField(default=False,verbose_name='联系方式')
    gender = models.CharField(max_length=6, choices=(('male','男'),('female','女')),
    						default='female',verbose_name='性别')
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)