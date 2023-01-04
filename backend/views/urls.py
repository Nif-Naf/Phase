from rest_framework import routers

from views.views import (
    TenantListApiView,
    WorkerListApiView,
    ProviderListApiView,
)

router = routers.SimpleRouter()

router.registry('views/tenant', TenantListApiView)

router.registry('views/worker', WorkerListApiView)

router.registry('views/provider', ProviderListApiView)
