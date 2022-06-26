from rest_framework import serializers

from user.models import User as UserModel

""""""
class UserSerializer(serializers.ModelSerializer):
    """회원가입 및 프로필 수정(allow), 전체 회원 조회(admin)"""
    def get_gender(self, obj):
        if obj.gender:
            return "남자"
        return "여자"

    class Meta:
        model = UserModel
        gender = serializers.SerializerMethodField()


        fields = ["user", "password", "name", "email", "gender", "date_of_birth", "mobile_number", "introduce",
                  "join_date", "is_seller", "is_terms_of_service", "is_privacy_policy", "is_receive_marketing_info"]
        extra_kwargs = {
            "password": {"write_only": True}
        }
        read_only_fields = ["join_date", "is_seller", "is_terms_of_service", "is_privacy_policy"]

    def validate(self, data):
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
        # User object 생성
        user = UserModel(**validated_data)
        if validated_data["is_seller"]:
            # 판매자 계정의 경우 관리자가 승인해줘야되기 때문에 is_active를 False로 바꿔준다.
            user.is_active = False
        user.introduce = F"안녕하세요~ {validated_data['name']}입니다"
        user.save()

    def update(self, instance, validated_data):
        # instance에는 입력된 object가 담긴다.
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue

            setattr(instance, key, value)
        instance.save()
        return instance