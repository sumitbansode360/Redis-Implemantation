from celery import shared_task
import time

@shared_task
def send_email_task(email):
    print(f"Sending email to {email}...")

    time.sleep(5) # delay

    print("Email sent!")


@shared_task(bind=True, max_retries=3)
def send_email_task_e(self, email):
    try:
        print(f"sending email to {email}...")
        raise Exception("email failed")
    except Exception as e:
        print("retrying...")
        raise self.retry(exc=e, countdown=5)