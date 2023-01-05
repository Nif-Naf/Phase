from django.db.models import (
    Model,
    CharField
)


class Tenant(Model):
    """Модель описывающая сущность: Жильца."""
    tenant_all_name = CharField()


class Worker(Model):
    """Модель описывающая сущность: Сотрудника."""
    full_name = CharField()


class Provider(Model):
    """Модель описывающая сущность: Организации."""
    name_organization = CharField()
