import xadmin
from django import forms

from .models import DailyThink

class ThinkDailyForm(forms.ModelForm):

    class Meta:
        model = DailyThink
        fields = '__all__'



class ThinkDailyAdmin(object):
    list_display = ["content", "author", "add_time", "update_time"]
    list_editable = ["content", "author", "add_time", "update_time"]

xadmin.site.register(DailyThink, ThinkDailyAdmin)