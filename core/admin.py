from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Congregation, CustomUser, Donation


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

    # TODO: dropdown aparecer dinamicamente
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance and self.instance.category != 'CL':
    #         self.fields['department'].widget = forms.HiddenInput()
    #         self.fields['department'].required = False


class CustomUserAdmin(UserAdmin):
    form = CustomUserForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("category", "department", "congregations")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Congregation)
class CongregationAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name", "address")


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = (
        "donation_type",
        "amount",
        "donation_date",
        "payment_method",
        "user",
        "anonymous",
    )
    list_filter = ("donation_type", "payment_method", "anonymous")
    search_fields = ("user__username", "amount")
