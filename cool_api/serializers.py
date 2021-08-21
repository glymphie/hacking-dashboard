from rest_framework import serializers

from .models import FtpLogin, Endlessh

class FtpLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FtpLogin
        fields = ('date', 'ip', 'status')

class EndlesshSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endlessh
        fields = ('date', 'ip', 'time_wasted', 'bytes_sent')
