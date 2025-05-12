from rest_framework import serializers

class PicoPlacaRequestSerializer(serializers.Serializer):
    plate = serializers.CharField()
    date  = serializers.DateField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])
    time  = serializers.TimeField(format='%H:%M', input_formats=['%H:%M'])

class PicoPlacaResponseSerializer(serializers.Serializer):
    can_drive = serializers.BooleanField()
