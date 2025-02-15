from celery import shared_task
from django.core.mail import send_mail
from .models import Post
from django.utils.timezone import now


# ✅ Send Welcome Email on User Registration
@shared_task
def send_welcome_email(user_email):
    send_mail(
        "Welcome to Blog API",
        "Thank you for registering!",
        "admin@blogapi.com",
        [user_email],
        fail_silently=False,
    )


# ✅ Generate Daily Post Statistics
@shared_task
def generate_daily_post_stats():
    today = now().date()
    total_posts = Post.objects.filter(created_at__date=today).count()
    print(f"Total posts today: {total_posts}")
    return total_posts
