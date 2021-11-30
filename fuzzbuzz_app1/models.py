from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.base import Model
from django.db.models.expressions import Value

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("이메일을 반드시 입력해주세요.")
        if not username:
            raise ValueError("사용자명을 반드시 입력해주세요.")

        user = self.model(
            email=self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User_Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name="email", max_length=30, unique=True)
    username        = models.CharField(max_length=30, unique=True)
    date_signup     = models.DateTimeField(verbose_name="date signup", auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = AccountManager()

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name_plural = '유저 정보'


# class Userinfo(models.Model):
#     name        = models.CharField(max_length=10)
#     phone       = models.CharField(max_length=15)
#     address     = models.TextField()
#     create_date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['create_date']
#         verbose_name_plural = '테스트 테이블(userinfo)'


# 혼잡도 테이블
class Congestion_points_HJ(models.Model):
    input_time = models.DateTimeField()
    value      = models.FloatField(max_length=5)
    people     = models.IntegerField(default=0)
    class Meta:
        ordering = ['input_time']                  # 정렬 기준
        verbose_name_plural = '혼잡도 테이블 / HJ'   # admin 페이지 표기명
    def __str__(self):
        return f'{self.input_time} :: {self.value}'

class Congestion_points_SH(models.Model):
    input_time = models.DateTimeField()
    value      = models.FloatField(max_length=5)
    people     = models.IntegerField(default=0)

    class Meta:
        ordering = ['input_time']
        verbose_name_plural = '혼잡도 테이블 / SH'   # admin 페이지 표기명
    def __str__(self):
        return f'{self.input_time} :: {self.value}'


# 순환 주기 메모리
class turnover_temp_HJ(models.Model):
    input_time = models.DateTimeField()
    table_id   = models.SmallIntegerField()
    table_pnum = models.SmallIntegerField()
    class Meta:
        ordering = ['input_time']

class turnover_points_HJ(models.Model):
    input_time = models.DateTimeField()
    table_id   = models.SmallIntegerField()
    table_pnum = models.SmallIntegerField()
    class Meta:
        ordering = ['input_time']
        verbose_name_plural = '순환율 테이블 / HJ'
    def __str__(self):
        return f'{self.input_time} // {self.table_id}번 테이블 - {self.table_pnum}명'


class turnover_points_SH(models.Model):
    input_time = models.DateTimeField()
    total_turn = models.IntegerField()

    class Meta:
        ordering = ['input_time']
        verbose_name_plural = '순환율 테이블 / SH'
    def __str__(self):
        return f'{self.input_time} // {self.total_turn}회'


# FAQ 테이블
class Questions(models.Model):
    Q_text = models.TextField(null=False)
    A_text = models.TextField(null=False)
    time   = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'FAQ 목록'