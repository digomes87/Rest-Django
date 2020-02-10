from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializers a name field for testinf ou apiview"""
    name = serializers.CharField(max_length=10)
