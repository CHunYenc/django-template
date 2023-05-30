from django.db import models
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets, permissions
from django.http import HttpResponse
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["API"])
class BaseViewSet(viewsets.ViewSet):
    """ ViewSet, 包含 JWTAuthentication """
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class TimeStampMixinModel(models.Model):
    """
    擴充 models，加入 create_at & update_at 欄位的基礎類別
    """
    created_at = models.DateTimeField(
        help_text="時間戳記，為最初建立資料的時間。", auto_now_add=True)
    updated_at = models.DateTimeField(
        help_text="時間戳記，為每次更新資料時間。", auto_now=True)

    class Meta:
        abstract = True


def get_client_ip(request):
    """ 可以獲取當前瀏覽者的 IP 位置 """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse(ip)
