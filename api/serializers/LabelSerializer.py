from rest_framework.fields import ChoiceField
from rest_framework.serializers import ModelSerializer, Serializer, CharField
from api.models import Label


class ColorSerializer(Serializer):
    textColor = CharField(max_length=255)
    backgroundColor = CharField(max_length=255)


class LabelSerializer(ModelSerializer):
    MESSAGE_VISIBILITY_CHOICES = (
        ('show', 'show'),
        ('hide', 'hide'),
    )
    LABEL_VISIBILITY_CHOICES = (
        ('labelShow', 'labelShow'),
        ('labelShowIfUnread', 'labelShowIfUnread'),
        ('labelHide', 'labelHide'),
    )

    labelListVisibility = ChoiceField(choices=LABEL_VISIBILITY_CHOICES)
    messageListVisibility = ChoiceField(choices=MESSAGE_VISIBILITY_CHOICES)
    name = CharField(max_length=255, required=False)
    color = ColorSerializer(required=False)

    class Meta:
        model = Label
        fields = ("id", "label_id", "user", "labelListVisibility", "messageListVisibility", "name", "color", )
        read_only_fields = ("label_id", "user")
