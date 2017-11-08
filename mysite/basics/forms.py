from django import forms

import basics.models as db_models


class ContactForm(forms.ModelForm):
    class Meta:
        model = db_models.Contact
        exclude = ('id','user', )


class TagsAddForm(forms.ModelForm):
    class Meta:
        model = db_models.Tag
        exclude = ('id',)
