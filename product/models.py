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
    image1 = models.ImageField("이미지1", upload_to="product/image/",  max_length=None, null=True, blank=True)
    image2 = models.ImageField("이미지2", upload_to="product/image/",  max_length=None, null=True, blank=True)
    image3 = models.ImageField("이미지3", upload_to="product/image/",  max_length=None, null=True, blank=True)
    image4 = models.ImageField("이미지4", upload_to="product/image/",  max_length=None, null=True, blank=True)
    image5 = models.ImageField("이미지5", upload_to="product/image/",  max_length=None, null=True, blank=True)
