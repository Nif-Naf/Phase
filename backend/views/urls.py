from django.urls import path
from rest_framework.routers import SimpleRouter

from views.views import (
    TenantListApiView,
    WorkerListApiView,
    ProviderListApiView,
)

router = SimpleRouter()

urlpatterns = [
    path('api_views/tenant/', TenantListApiView.as_view()),
    path('api_views/worker/', WorkerListApiView.as_view()),
    path('api_views/provider/', ProviderListApiView.as_view()),
]

# router.register(
#     'api_views/tenant/',
#     TenantListApiView,
#     'tenants_names_list',
# )
#
# router.register(
#     'api_views/worker/',
#     WorkerListApiView,
#     'workers_names_list',
# )
#
# router.register(
#     'api_views/provider/',
#     ProviderListApiView,
#     'providers_names_list',
# )

urlpatterns += router.urls
