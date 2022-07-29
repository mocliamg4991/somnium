from ast import Sub
from operator import mod
from turtle import position
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from organization.models import Position, Subdivision
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    patronymic = models.CharField(max_length=100, verbose_name="Отчество",blank=True, null=True)
    code = models.PositiveIntegerField(verbose_name="Код",blank=True, null=True)
    position = models.ManyToManyField(Position)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, blank=True, null=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images',verbose_name="Аватар",blank=True, null=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Ставка",blank=True, null=True)
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()


def getFullName(self):
    return '{0} {1} {2}'.format(self.user.first_name, self.user.last_name, self.patronymic)

def getParentSubdivision(self):
    return Profile.objects.select_related('subdivision').get(self.user.id).subdivision.parent

def getAllUsersPosition(self):
    q = Profile.objects.prefetch_related('position')
    pos_data = []
    for profile  in q:
        positions = [position.name for position in profile.objects.all()]
        pos_data.append({'id': profile.user.id, 'name': profile.user.first_name, 'books': positions})
    return pos_data

