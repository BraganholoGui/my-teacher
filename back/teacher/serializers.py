from rest_framework import serializers
from teacher.models import Teacher,Class
from django.forms import ValidationError


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields= '__all__'

class SaveClassSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=245)
    name = serializers.CharField(max_length=100)

    def validate_name(self, value):
        if len(value):
            raise ValidationError("Deve ter pelo menos 3 caracteres")
        return value


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'