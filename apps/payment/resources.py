from import_export import resources
from .models import PayState, Gateway, Payment


class PayStateResources(resources.ModelResource):
    class Meta:
        model = PayState


class GatewayResources(resources.ModelResource):
    class Meta:
        model = Gateway


class PaymentResources(resources.ModelResource):
    class Meta:
        model = Payment
