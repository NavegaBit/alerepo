from django.db.models.signals import post_save
from django.db.models import Avg, FloatField, Count
from django.dispatch import receiver
from datetime import datetime

from .models import Payment
from apps.product.models import ProductType
from apps.report.models import ReportPaymentProduct, ReportPaymentYear, ReportPaymentMounth


@receiver(post_save, sender=Payment, dispatch_uid="update_stats")
def update_stats(sender, instance, **kwargs):
    # payments = Payment.objects.all()
    # Payment.objects.agregate(sum('total'))
    # product_type = ProductType.objects.all().values()
    # ReportPaymentProduct.objects.filter(product_type=instance.product.product_type).delete()
    # # payment_product = ReportPaymentProduct(product_type=instance.product.product_type, total=)
    pass