from django.contrib import admin
from django.contrib import admin
from .models import MyAccountModel, CustomerAccount,Sale,OrderDetail
from .form import MyAccountModelForm, MyCustomerAccountModelForm, MySaleModelForm,MyOrderDetailModelForm

class AccountModelAdmin(admin.ModelAdmin):
    form = MyAccountModelForm
    list_display = ('userID', 'email', 'firstname', 'lastname', 'role', 'create_date')
    list_filter = ('email',)
    search_fields = ('email', 'firstname', 'lastname')

    def save_model(self, request, obj, form, change):
        if not obj.userID:
            # Calculate the next available user ID
            latest_user = MyAccountModel.objects.order_by('-userID').first()
            if latest_user:
                latest_id = int(latest_user.userID.split('-')[1])
                next_user_id = f'USER-{latest_id + 1}'
            else:
                next_user_id = 'USER-1'

            obj.userID = next_user_id

        super().save_model(request, obj, form, change)

class CustomerAccountModelAdmin(admin.ModelAdmin):
    form = MyCustomerAccountModelForm
    list_display = ('accountID', 'email', 'firstname', 'lastname', 'birthdate', 'phone_number' ,'address' ,'state' ,'city' ,'zipcode' ,'created_date')
    list_filter = ('email', 'address','firstname', 'lastname','phone_number',)
    search_fields = ('email', 'address','firstname', 'lastname', 'birthdate','phone_number')

    def save_model(self, request, obj, form, change):
        if not obj.accountID:
            # Calculate the next available user ID
            latest_user = CustomerAccount.objects.order_by('-accountID').first()
            if latest_user:
                latest_id = int(latest_user.accountID.split('-')[1])
                next_account_id = f'ACCOUNT-{latest_id + 1}'
            else:
                next_account_id = 'ACCOUNT-1'

            obj.accountID = next_account_id

        super().save_model(request, obj, form, change)

class SaleModelAdmin(admin.ModelAdmin):
    form = MySaleModelForm
    list_display = ('saleID', 'email', 'product_or_service','price', 'created_date')
    list_filter = ('email',)
    search_fields = ('email', 'product_or_service','accountID')

    def save_model(self, request, obj, form, change):
        if not obj.saleID:
            # Calculate the next available user ID
            latest_user = Sale.objects.order_by('-saleID').first()
            if latest_user:
                latest_id = int(latest_user.saleID.split('-')[1])
                next_sale_id = f'SALE-{latest_id + 1}'
            else:
                next_sale_id = 'SALE-1'

            obj.saleID = next_sale_id

        super().save_model(request, obj, form, change)

class OrderDetailModelAdmin(admin.ModelAdmin):
    form = MyOrderDetailModelForm
    list_display = ('orderID', 'total')
    list_filter = ('orderID',)
    search_fields = ('email', 'saleID')

    def save_model(self, request, obj, form, change):
        if not obj.orderID:
            # Calculate the next available user ID
            latest_user = OrderDetail.objects.order_by('-orderID').first()
            if latest_user:
                latest_id = int(latest_user.userID.split('-')[1])
                next_order_id = f'ORDER-{latest_id + 1}'
            else:
                next_order_id = 'ORDER-1'

            obj.orderID = next_order_id

        super().save_model(request, obj, form, change)


admin.site.register(MyAccountModel, AccountModelAdmin)
admin.site.register(CustomerAccount, CustomerAccountModelAdmin)
admin.site.register(Sale, SaleModelAdmin)
admin.site.register(OrderDetail, OrderDetailModelAdmin)