from import_export import resources
from .models import UserManagement, ContractUser, Contract, UserProfile


class UserProfileResources(resources.ModelResource):
    class Meta:
        model = UserProfile


class UserManagementResources(resources.ModelResource):
    class Meta:
        model = UserManagement


class ContractUserManagementResources(resources.ModelResource):
    class Meta:
        model = ContractUser


class ContractManagementResources(resources.ModelResource):
    class Meta:
        model = Contract
