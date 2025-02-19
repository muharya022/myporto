from .models import ContactMessage

def unread_messages_count(request):
    return {
        'unread_count': ContactMessage.objects.filter(is_read=False).count()
    }
