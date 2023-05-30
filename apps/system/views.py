from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.utils import BaseViewSet
from drf_spectacular.utils import extend_schema
from .models import Version
from .serializers import VersionSerializer


# Create your views here.


@extend_schema(summary="系統歷程資訊", tags=["SYSTEM-API"])
class VersionViewSet(BaseViewSet):
    """_summary_

    Args:
        BaseViewSet (_type_): _description_

    Returns:
        _type_: _description_
    """
    @extend_schema(
        description="提供系統全部的更新歷程資訊。",
        responses={200: VersionSerializer})
    def list(self, request):
        queryset = Version.objects.filter(activate=True) \
            .order_by('-created_at') \
            .all()
        serializer = VersionSerializer(queryset, many=True)
        # response
        response = Response()
        response.data = serializer.data
        response.status_code = status.HTTP_200_OK
        return response

    @extend_schema(
        description="提供系統最新的版本資訊。",
        responses={200: VersionSerializer})
    @action(detail=False, methods=["GET"], url_path="last")
    def last(self, request):
        queryset = Version.objects.filter(activate=True).last()
        serializer = VersionSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
