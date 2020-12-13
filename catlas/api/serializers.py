from rest_framework import serializers

from api.models import Member

class CreateMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'account', 'password', 'salt', 'name', 'email')