from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.forms import fields
from .models import Vehicle_Details




class VehicleModelForm(BSModalModelForm):

    class Meta:
        model = Vehicle_Details
        fields = "__all__"


