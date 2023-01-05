from django.contrib import admin
from all_models.models import (
    Tenant,
    Worker,
    Provider,
)

# Все модели отвечающие за сущности.
essence_models = [Tenant, Worker, Provider]

admin.register(essence_models)
