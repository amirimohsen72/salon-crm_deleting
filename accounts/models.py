from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    age = models.PositiveIntegerField(null=True,blank=True,verbose_name=_('age')) #adad mosbat : sen
    mobile = models.CharField(max_length=11,blank=True,verbose_name=_('mobile')) #shomare mobile


