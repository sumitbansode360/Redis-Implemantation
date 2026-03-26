from celery import shared_task
import time
from .models import Report

@shared_task(bind=True, max_retries=3)
def genrate_report(self, report_id):
    report = Report.objects.get(id=report_id)
    report.status = "PROCESSING"
    report.save()

    print("genrating report...")
    time.sleep(10)

    report.status = "COMPLETED"
    report.pdf_genrated = True
    report.save()
    print("report generation done!")

