from django.contrib import admin
from .models import Message, Conversation

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 
        'created'
    )


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'count_messages',
        'count_participants'
    )