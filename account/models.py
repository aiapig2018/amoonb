from django.db import models
from django.conf import settings

#扩展用户信息模型
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField("生日",blank=True, null=True)
    headshot = models.ImageField(upload_to='avatar/%Y/%m/%d/',default='default.jpg', verbose_name='头像')
    city = models.CharField("居住地", max_length = 30, blank = True) 
    
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

