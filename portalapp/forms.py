from django import forms
from portalapp.models import UserInfo

class getUserInfo(forms.ModelForm):
	#user =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
	class Meta:
		model = UserInfo
		exclude = ('status','created_at','updated_at','user')
