# Generated by Django 4.0.5 on 2022-06-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='사용자 계정')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('profile_image', models.ImageField(default='user/profile/default_profile_image.jpg', upload_to='user/profile/', verbose_name='프로필 사진')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='이메일 주소')),
                ('gender', models.BooleanField(verbose_name='성별')),
                ('date_of_birth', models.DateField(verbose_name='생년월일')),
                ('mobile_number', models.CharField(max_length=20, verbose_name='휴대전화')),
                ('introduce', models.CharField(max_length=200, verbose_name='소개')),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('is_seller', models.BooleanField(verbose_name='판매자')),
                ('is_terms_of_service', models.BooleanField(verbose_name='서비스이용약관동의')),
                ('is_privacy_policy', models.BooleanField(verbose_name='개인정보처리방침동의')),
                ('is_receive_marketing_info', models.BooleanField(verbose_name='마케팅정보수신동의')),
                ('is_secession', models.BooleanField(default=False, verbose_name='탈퇴')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 상태')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
