from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserAddress as UserAddressModel

""""""
class OtherUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username", "name", "profile_image", "introduce", "is_seller"]


class UserAddressSerializer(serializers.ModelSerializer):
    """회원 주소 등록, 조회, 수정"""
    class Meta:
        model = UserAddressModel
        fields = ["address", "zip_code", "address_tag", "name"]


class UserSerializer(serializers.ModelSerializer):
    """
    회원가입(is not authenticate)
    전체 회원 조회(admin)
    """
    gender_str = serializers.SerializerMethodField()
    useraddress_set = UserAddressSerializer(many=True, required=False)
    def get_gender_str(self, obj):
        if obj.gender:
            return "남자"
        return "여자"

    class Meta:
        model = UserModel
        # default 값이 있는 필드는 data들어올 때 key, value가 없어도 validate 통과 //
        fields = ["username", "profile_image", "password", "name", "email", "gender", "gender_str", "date_of_birth",
                  "mobile_number", "introduce", "join_date", "is_seller", "is_terms_of_service", "is_privacy_policy",
                  "is_receive_marketing_info", "is_secession", "useraddress_set"]
        extra_kwargs = {
            "password": {"write_only": True},
            "gender": {"write_only": True},
            "introduce": {"required": False}
        }
        read_only_fields = ["join_date", "is_secession"]

    def validate(self, data):
        print(f"validate: {data}")
        # custom validation pattern
        if not data.get("is_terms_of_service", "") or not data.get("is_privacy_policy"):
            # validation에 통과하지 못할 경우 ValidationError class 호출
            raise serializers.ValidationError(
                # custom validation error message
                detail={"error": "서비스 이용약관과 개인정보 활용에 동의해야 가입할 수 있습니다"},
            )

        # validation에 문제가 없을 경우 data return
        return data

    def create(self, validated_data):
        print(f"create: {validated_data}")
        # User object 생성
        instance = UserModel(**validated_data)
        if validated_data["is_seller"]:
            # 판매자 계정의 경우 관리자가 승인해줘야되기 때문에 is_active를 False로 바꿔준다.
            instance.is_active = False
        instance.introduce = F"안녕하세요~ {validated_data['name']}입니다"
        instance.set_password(validated_data["password"])
        instance.save()
        return instance


class UserDetailSerializer(serializers.ModelSerializer):
    gender_str = serializers.SerializerMethodField()
    useraddress_set = UserAddressSerializer(many=True, required=False)

    def get_gender_str(self, obj):
        if obj.gender:
            return "남자"
        return "여자"

    class Meta:
        model = UserModel
        fields = ["username", "profile_image", "password", "name", "email", "gender", "gender_str", "date_of_birth",
                  "mobile_number", "introduce", "join_date", "is_seller", "is_terms_of_service", "is_privacy_policy",
                  "is_receive_marketing_info", "is_secession", "useraddress_set"]
        extra_kwargs = {
            "password": {"write_only": True},
            "gender": {"write_only": True},
        }
        read_only_fields = ["username", "join_date", "is_seller", "is_terms_of_service", "is_receive_marketing_info"]

    def update(self, instance, validated_data):
        # instance에는 입력된 object가 담긴다.
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue

            setattr(instance, key, value)
        instance.save()
        return instance