from django import forms
from .models import MyAccountModel,CustomerAccount,Sale,OrderDetail

# class MyAccountModelAdminForm(forms.ModelForm):
    # class Meta:
    #     model = MyAccountModel
    #     fields = '__all__'
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Make the userID field read-only
    #     self.fields['userID'].widget.attrs['readonly'] = True


class MyAccountModelForm(forms.ModelForm):
    class Meta:
        model = MyAccountModel
        exclude = ['userID']  # Exclude the 'userID' field from the form

class MyCustomerAccountModelForm(forms.ModelForm):
    class Meta:
        model = CustomerAccount
        exclude = ['accountID']  # Exclude the 'userID' field from the form


class MySaleModelForm(forms.ModelForm):
    class Meta:
        model = Sale
        exclude = ['saleID']  # Exclude the 'userID' field from the form


class MyOrderDetailModelForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        exclude = ['orderID']  # Exclude the 'userID' field from the form

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerAccount
        fields = '__all__'  # You can specify the fields you want to include here
