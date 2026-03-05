from rest_framework import serializers
from .models import WaitlistEntry


class WaitlistEntrySerializer(serializers.ModelSerializer):
    
    def validate(self, attrs):
        email = attrs.get('email')
        if WaitlistEntry.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email is already on the waitlist.")
        return attrs
    
    
    class Meta:
        model = WaitlistEntry
        fields = '__all__'