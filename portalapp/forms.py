from django import forms
from portalapp.models import UserInfo

class getUserInfo(forms.ModelForm):
	
	class Meta:
		model = UserInfo
		exclude = ('status','created_at','updated_at','user')
