from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Q
from django.contrib.auth.hashers import make_password

from .models import UserManagement, ContractUser, Contract, UserProfile

from import_export.admin import ImportExportModelAdmin
from .resources import UserManagementResources, ContractUserManagementResources, ContractManagementResources, \
    UserProfileResources


@admin.register(UserProfile)
class UserProfilePanelFilter(ImportExportModelAdmin):
    list_display = ('user', 'belong_to', 'sex', 'birth')
    search_fields = ['user__username', 'belong_to__username']
    filter_horizontal = ()
    fieldsets = ()
    resources = UserProfileResources
    list_per_page = 25


    def render_change_form(self, request, context, *args, **kwargs):
        form_instance = context['adminform'].form
        # form_instance.fields['birth'].widget.attrs['min'] = str(datetime.date(
        #     datetime.date.today().year - 150,
        #     datetime.date.today().month,
        #     datetime.date.today().day
        # ))
        # form_instance.fields['birth'].widget.attrs['max'] = str(datetime.date(
        #     datetime.date.today().year,
        #     datetime.date.today().month,
        #     datetime.date.today().day
        # ))
        if not request.user.is_superuser:
            form_instance.fields['user'].queryset = form_instance.fields['user'].queryset.exclude(
                Q(id__in=UserProfile.objects.filter(
                    belong_to=request.user.id
                ).values('user__id')) | Q(id__in=UserManagement.objects.filter(is_superuser=True).values('id'))
            )
            form_instance.fields['belong_to'].queryset = form_instance.fields['belong_to'].queryset.filter(
                id=request.user.id
            )

        return super(UserProfilePanelFilter, self).render_change_form(request, context, *args, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Q(belong_to=request.user.id) | Q(id=request.user.id))

    def save_model(self, request, obj, form, change):
        """
                Override save method to include the user are creating the object
                :return: Object
                """
        obj.belong_to = request.user
        super().save_model(request, obj, form, change)


@admin.register(UserManagement)
class UserPanelFilter(UserAdmin):
    list_display = ('username', 'email', 'phone_no')
    search_fields = ['username']
    list_filter = ['username', 'email', 'phone_no']
    filter_horizontal = ()
    fieldsets = ()
    resources = UserManagementResources
    list_per_page = 25


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
        return qs.filter(Q(id__in=users_profiles) | Q(id=request.user.id))

    def save_model(self, request, obj, form, change):
        """
                Override save method to include the user are creating the object
                :return: Object
                """
        super(UserPanelFilter, self).save_model(request, obj, form, change)
        user = form.username
        password = make_password(form.password)
        # user = UserManagement.objects.filter(user=)

        # UserProfile(user=, belong_to=request.user, )


@admin.register(ContractUser)
class ContractUserPanelFilter(ImportExportModelAdmin):
    list_display = ('user', 'contract', 'start_date', 'end_date')
    search_fields = ['user__username', 'contract__name']
    list_filter = ['user__username']
    filter_horizontal = ()
    fieldsets = ()
    resources = ContractUserManagementResources
    list_per_page = 25


    def get_queryset(self, request):
        qs = super(ContractUserPanelFilter, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
        return qs.filter(Q(id__in=users_profiles) | Q(id=request.user.id))


@admin.register(Contract)
class ContractPanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'price', 'time_in_days')
    search_fields = ['name', 'price']
    list_filter = ['name']
    filter_horizontal = ()
    fieldsets = ()
    resources = ContractManagementResources
    list_per_page = 25

