# from users.models import UserAccount
# from django.contrib.auth.models import BaseUserManager

# class StudentManager(BaseUserManager):
      
#       def create_user(self, username, password=None):
#             if not username or len(username)<=0:
#                   raise ValueError("Email field is required !")
#             if not password:
#                   raise ValueError("Password is must !")
#             user=self.model(username=username)
#             user.set_password(password)
#             user.save(using=self._db)
#             return user
      
#       def get_queryset(self, *args, **kwargs) :
#             return super().get_queryset(*args, **kwargs).filter(type='users.UserAccount.Types.STUDEN')

# class Student(UserAccount):
#       class Meta:
#             proxy=True

#       objects=StudentManager()
#       def save(self, *args, **kwargs):
#             self.type='users.UserAccount.Types.STUDEN'
#             self.is_student=True
#             return super().save(*args, **kwargs)

# class TeacherManager(BaseUserManager):
#       def create_user(self, username, password=None):
#             if not username or len(username)<=0:
#                   raise ValueError("Email field is required !")
#             if not password:
#                   raise ValueError("Password is must !")
#             user=self.model(username=username)
#             user.set_password(password)
#             user.save(using=self._db)
#             return user

#       def get_queryset(self, *args, **kwargs) :
#             return super().get_queryset(*args, **kwargs).filter(type='users.UserAccount.Types.TEACHER')
      
# class Teacher(UserAccount):
#       class Meta:
#             proxy=True

#       objects=TeacherManager()
#       def save(self, *args, **kwargs):
#             self.type='users.UserAccount.Types.TEACHER'
#             self.is_teacher=True
#             return super().save(*args, **kwargs)