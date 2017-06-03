from rest_framework import serializers
from team.models import Members


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('id','first_name', 'last_name', 'phone', 'email', 'role')    
    def create(self, validated_data):
        """
        Create and return a new `Member` instance, given the validated data.
        """
        return Members.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Member` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance