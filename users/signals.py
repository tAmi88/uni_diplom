from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Student, Teacher, StudentProfile, TeacherType
UserAccount=get_user_model()

@receiver(post_save,sender=Student)
@receiver(post_save,sender=Teacher)
@receiver(post_save,sender=UserAccount)
def my_handler(sender, instance, created, **kwargs):
    if created:
        if sender == Student:
            StudentProfile.objects.create(user=instance)
        if sender == TeacherType:
            TeacherType.objects.create(user=instance)
        if sender == UserAccount:
            if instance.type == "STUDENT":
                StudentProfile.objects.create(user=instance)
            elif instance.type == "TEACHER":
                TeacherType.objects.create(user=instance)



    