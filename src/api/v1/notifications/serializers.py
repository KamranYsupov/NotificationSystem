from rest_framework import serializers

from src.utils.validators import russian_phone_number_validator


class ContactSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15,)

    def validate_phone_number(self, value):
        if not russian_phone_number_validator(value):
            raise serializers.ValidationError(
                "Номер телефона не соответствует российскому формату."
            )

        return value
