import time

from threading import Thread
from datetime import datetime

from django.core.management.base import BaseCommand
from django.db.models.aggregates import Sum
from django.db.models import Q

from apps.user.models import UserManagement, UserProfile
from apps.product.models import ProductType
from apps.payment.models import Payment
from apps.report.models import ReportPaymentYear, ReportPaymentMounth, ReportPaymentProduct


class Command(BaseCommand):
    """ New command to populate database"""

    @staticmethod
    def crontab(self):
        while True:
            try:
                time.sleep(600)
                payments = Payment.objects.all()
                users = UserManagement.objects.all()
                if users:
                    product_type = ProductType.objects.all()
                    for user in users:
                        users_profiles = UserProfile.objects.filter(belong_to=user.id).values('user__id')
                        self.report_year(users_profiles, user, payments)
                        self.report_month(users_profiles, user, payments)
                        self.report_product(users_profiles, user, payments, product_type)
            except Exception as e:
                print("Command complete with errors: {}".format(str(e)))

    def handle(self, *args, **options) -> None:
        try:
            thread = Thread(target=self.crontab, args=[self])
            thread.start()

        except Exception as e:
            print("Command complete with errors: {}".format(str(e)))

    @staticmethod
    def report_year(users_profiles, user, payments):
        payment = payments.filter(
            Q(product__belong_to__id=user.id) |
            Q(product__belong_to__id__in=users_profiles)
        ).filter(created_at__year=datetime.now().year)
        if payment:
            report = ReportPaymentYear.objects.filter(year=datetime.now().year, user=user).first()
            pay_neto = payment.aggregate(Sum('neto'))
            if report:
                if report.total != pay_neto['neto__sum']:
                    report.total = pay_neto['neto__sum']
                    report.save()
            else:
                report_user = ReportPaymentYear(
                    year=datetime.now().year,
                    user=user,
                    total=pay_neto['neto__sum']
                )
                report_user.save()

    @staticmethod
    def report_month(users_profiles, user, payments):
        payment = payments.filter(
            Q(product__belong_to__id=user.id) |
            Q(product__belong_to__id__in=users_profiles)
        ).filter(
            created_at__year=datetime.now().year,
            created_at__month=datetime.now().month
        )
        if payment:
            report = ReportPaymentMounth.objects.filter(
                year=datetime.now().year,
                mounth=datetime.now().month,
                user=user
            ).first()
            pay_neto = payment.aggregate(Sum('neto'))
            if report:
                if report.total != pay_neto['neto__sum']:
                    report.total = pay_neto['neto__sum']
                    report.save()
            else:
                report_user = ReportPaymentMounth(
                    year=datetime.now().year,
                    mounth=datetime.now().month,
                    user=user,
                    total=pay_neto['neto__sum']
                )
                report_user.save()

    @staticmethod
    def report_product(users_profiles, user, payments, product_type):
        payment = payments.filter(
            Q(product__belong_to__id=user.id) |
            Q(product__belong_to__id__in=users_profiles)
        )
        if payment:
            for type in product_type:
                report = ReportPaymentProduct.objects.filter(product_type=type, user=user).first()
                pay_neto = payment.filter(product__product_type=type).aggregate(Sum('neto'))
                print(report, pay_neto)
                if report and pay_neto:
                    if report.total != pay_neto['neto__sum']:
                        report.total = pay_neto['neto__sum']
                        report.save()
                elif pay_neto['neto__sum']:
                    report_user = ReportPaymentProduct(
                        user=user,
                        product_type=type,
                        total=pay_neto['neto__sum']
                    )
                    report_user.save()
