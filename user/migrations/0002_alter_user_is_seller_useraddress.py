# Generated by Django 4.0.5 on 2022-06-26 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_seller',
            field=models.BooleanField(default=False, verbose_name='판매자'),
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100, verbose_name='주소')),
                ('zip_code', models.CharField(max_length=10, verbose_name='우편번호')),
                ('address_tag', models.CharField(max_length=20, verbose_name='배송지명')),
                ('name', models.CharField(max_length=20, verbose_name='받는분 성함')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='회원')),
            ],
        ),
    ]
