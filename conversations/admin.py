from django.contrib import admin
from .models import Message, Conversation

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass