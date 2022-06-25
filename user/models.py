from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


""""""
# Create your models here.
# custom user model 사용 시 UserManager 클래스와 create_user, create_superuser 함수가 정의되어 있어야 함
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, username, password, email=None):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        if email is not None:
            user.email = email # 메일 저장
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField("사용자 계정", max_length=20, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    profile_image = models.ImageField("프로필 사진", upload_to="user/profile/", max_length=None,
                                      default="user/profile/default_profile_image.jpg")
    name = models.CharField("이름", max_length=20)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    gender = models.BooleanField("성별")
    date_of_birth = models.DateField("생년월일")
    mobile_number = models.CharField("휴대전화", max_length=20)
    introduce = models.CharField("소개", max_length=200)
    join_date = models.DateTimeField("가입일", auto_now_add=True)
    is_seller = models.BooleanField("판매자")
    is_terms_of_service = models.BooleanField("서비스이용약관동의")
    is_privacy_policy = models.BooleanField("개인정보처리방침동의")
    is_receive_marketing_info = models.BooleanField("마케팅정보수신동의")
    is_secession = models.BooleanField("탈퇴", default=False)


    # is_active가 False일 경우 계정이 비활성화됨
    is_active = models.BooleanField("활성화 상태", default=True)

    # is_staff에서 해당 값 사용
    is_admin = models.BooleanField("관리자", default=False)

    # id로 사용 할 필드 지정.
    # 로그인 시 USERNAME_FIELD에 설정 된 필드와 password가 사용된다.
    USERNAME_FIELD = 'userid'

    # user를 생성할 때 입력받을 필드 지정
    REQUIRED_FIELDS = ["email",]

    objects = CustomUserManager()  # custom user 생성 시 필요

    def __str__(self):
        return self.userid

    # 로그인 사용자의 특정 테이블의 crud 권한을 설정, perm table의 crud 권한이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_perm(self, perm, obj=None):
        return True

    # 로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_module_perms(self, app_label):
        return True

    # admin 권한 설정
    @property
    def is_staff(self):
        return self.is_admin


class UserAddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(to=User, verbose_name="회원", on_delete=models.CASCADE)
    address = models.CharField("주소", max_length=100)
    zip_code = models.CharField("우편번호", max_length=10)
    address_tag = models.CharField("배송지명", max_length=20)
    name = models.CharField("받는분 성함", max_length=20)

    def __str__(self):
        return f"{self.user.name}님의 배송지 : {self.address_tag}"