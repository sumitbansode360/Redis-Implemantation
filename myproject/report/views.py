from .serializers import ReportSerializer
from .models import Report
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import genrate_report

@api_view(["POST"])
def create_report(request):
    name = request.data['name']
    report = Report.objects.create(name=name)

    # trigger report genration
    genrate_report.delay(report.id)
    return Response({
        "message": "report generation started...",
        "report_id": report.id
    })



@api_view(["GET"])
def get_report(request, report_id):
    report = Report.objects.get(id=report_id)
    serializer = ReportSerializer(report)
    return Response({"details": serializer.data})
