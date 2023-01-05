from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_200_OK as OK,
)

from all_models.models import (
    Tenant,
    Worker,
    Provider,
)


class TenantListApiView(APIView):
    """
    Эндпоинт для получения всех имен жителей. Без сериализация.
    Адрес: http://localhost:8000/views/api_views/tenant/
    """

    def get(self, request):
        return Response(
            data=[user.tenant_all_name for user in Tenant.objects.all()],
            status=OK
        )


class WorkerListApiView(APIView):
    """
    Эндпоинт для получения всех имен работников. Без сериализации.
    Адрес: http://localhost:8000/views/api_views/worker/
    """

    def get(self, request):
        return Response(
            data=[worker.full_name for worker in Worker.objects.all()],
            status=OK,
        )


class ProviderListApiView(APIView):
    """
    Эндпоинт для получения всех названий организаций. Без сериализации.
    Адрес: http://localhost:8000/views/api_views/provider/
    """

    def get(self, request):
        return Response(
            data=[provider.name_organization for provider in Provider.objects.all()],
            status=OK,
        )
