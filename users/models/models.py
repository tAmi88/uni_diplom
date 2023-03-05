from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

#from .managers import StudentManager, TeacherManager
from django.dispatch import receiver

class UserAccountManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username or len(username)<=0:
            raise ValueError("Email field is required !")
        if not password:
            raise ValueError("Password is must !")
        user=self.model(username = username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, username, password):
        if not username or len(username)<=0:
            raise ValueError("Email field is required !")
        if not password:
            raise ValueError("Password is must !")
        user=self.model(username = username)
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
        
class UserAccount(AbstractBaseUser):
      class Meta:
            app_label="users"
      
      class Types(models.TextChoices):
            STUDEN="STUDENT", "student"
            TEACHER="TEACHER", "teacher"
            ADMIN="ADMIN", "admin"

      type = models.CharField(max_length = 8 , choices = Types.choices)
      username = models.CharField(max_length = 200 , unique = True)
      is_active = models.BooleanField(default = True)
      is_admin = models.BooleanField(default = False)
      
      is_staff = models.BooleanField(default = False)
      is_superuser = models.BooleanField(default = False)
      is_student = models.BooleanField(default = False)
      is_teacher = models.BooleanField(default = False)

      USERNAME_FIELD = "username"

      objects = UserAccountManager()

      def __str__(self):
           return str(self.username)
	
      def has_perm(self ,perm,obj=None):
           return self.is_admin
      
      def has_module_perms(self, app_label):
           return True
      
      def save(self, *args,**kwargs):
            
            if not self.type or self.type==None:
                  self.type=UserAccount.Types.ADMIN
            return super().save(*args , **kwargs)
      

              
      
        
class StudentProfile(models.Model):
      user = models.OneToOneField('users.UserAccount', on_delete=models.CASCADE)

      def __str__(self) -> str:
            return self.user.username
      
      class Meta:
            app_label="users"

class TeacherType(models.Model):
      user = models.OneToOneField('users.UserAccount', on_delete=models.CASCADE)
      def __str__(self) -> str:
            return self.user.username
      class Meta:
            app_label="users"
      

class StudentManager(BaseUserManager):
      
      def create_user(self, username, password=None):
            if not username or len(username)<=0:
                  raise ValueError("Email field is required !")
            if not password:
                  raise ValueError("Password is must !")
            user=self.model(username=username)
            user.set_password(password)
            user.save(using=self._db)
            return user
      
      def get_queryset(self, *args, **kwargs) :
            return super().get_queryset(*args, **kwargs).filter(type=UserAccount.Types.STUDEN)

class Student(UserAccount):
      class Meta:
            proxy=True

      objects=StudentManager()
      def save(self, *args, **kwargs):
            self.type=UserAccount.Types.STUDEN
            self.is_student=True
            return super().save(*args, **kwargs)

class TeacherManager(BaseUserManager):
      def create_user(self, username, password=None):
            if not username or len(username)<=0:
                  raise ValueError("Email field is required !")
            if not password:
                  raise ValueError("Password is must !")
            user=self.model(username=username)
            user.set_password(password)
            user.save(using=self._db)
            return user

      def get_queryset(self, *args, **kwargs) :
            return super().get_queryset(*args, **kwargs).filter(type=UserAccount.Types.TEACHER)
      
class Teacher(UserAccount):
      class Meta:
            proxy=True

      objects=TeacherManager()
      def save(self, *args, **kwargs):
            self.type=UserAccount.Types.TEACHER
            self.is_teacher=True
            return super().save(*args, **kwargs)


# class Subject(models.Model):
#       pass