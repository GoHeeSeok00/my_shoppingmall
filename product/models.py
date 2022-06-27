from django.core.validators import MinValueValidator
from django.db import models

from user.models import User as UserModel

""""""
# Create your models here.
class Category(models.Model):
    name = models.CharField("카테고리명", max_length=20)

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(to=UserModel, verbose_name="판매자", on_delete=models.CASCADE)
    title = models.CharField("상품 제목", max_length=100)
    category = models.ManyToManyField(to=Category, verbose_name="카테고리")
    thumbnail = models.ImageField("썸네일", upload_to="product/thumbnail/", max_length=None)
    description = models.TextField("상품 설명")
    view_count = models.BigIntegerField("상품 조회수", default=0)
    is_active = models.BooleanField("활성화 상태", default=True)
    is_delete = models.BooleanField("삭제 여부", default=False)
    created_at = models.DateTimeField("작성시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정시간", auto_now=True)

    def __str__(self):
        return f"{self.title}"


class ProductImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(to=Product, verbose_name="상품", on_delete=models.CASCADE)
    image = models.ImageField("이미지", upload_to="product/image/",  max_length=None, null=True, blank=True)


class ProductOption(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(to=Product, verbose_name="상품", on_delete=models.CASCADE)
    name = models.CharField("상품명", max_length=100)
    price = models.IntegerField("가격", validators=[MinValueValidator(0)])
    quantity = models.IntegerField("수량", validators=[MinValueValidator(0)])
    is_discount = models.BooleanField("할인 여부", default=False)
    discount_price = models.IntegerField("할인 가격", validators=[MinValueValidator(0)], null=True, blank=True)
    discount_start_date = models.DateTimeField("할인 시작일", null=True, blank=True)
    discount_end_date = models.DateTimeField("할인 종료일", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"