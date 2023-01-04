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
    """Эндпоинт для получения всех имен жителей."""

    def get(self, request):
        str_names = Tenant.objects.only('tenant_all_name').all()
        result = dict(username=str_names)
        return Response(data=result, status=OK)


class WorkerListApiView(APIView):
    """Эндпоинт для получения всех имен работников."""

    def get(self, request):
        full_names = Worker.objects.only('full_name').all()
        result = dict(username=full_names)
        return Response(data=result, status=OK)


class ProviderListApiView(APIView):
    """Эндпоинт для получения всех названий организаций."""

    def get(self, request):
        names_organizations = Provider.objects.only('name_organization').all()
        result = dict(username=names_organizations)
        return Response(data=result, status=OK)
