from django.forms import ModelForm, EmailInput
from .models import Newsletter


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email_address"]
        widgets = {
            "email_address": EmailInput(
                attrs={
                    "class": "w-full py-3 text-center bg-slate-50 outline-none border-b-2 border-slate-300 text-slate-600"
                }
            ),
        }
