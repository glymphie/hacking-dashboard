from rest_framework import serializers

from .models import FtpLogin

class FtpLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FtpLogin
        fields = ('date', 'ip', 'status')
