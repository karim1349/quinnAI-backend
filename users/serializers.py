from rest_framework import serializers

from users.models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber

        fields =("id", "tokens", 'user', 'access_token', 'refresh_token', 'expires_in')
