from django.forms import ModelForm
from crud.models import Member
from django import forms
import re


class MemberForm(ModelForm):

    #モデルで定義された条件をオーバーライド？する（Metaの記述より先に書く）
    name = forms.CharField(required=False,max_length=8)

    class Meta:
        model = Member
        fields = ('name','email','age',)

    #各要素のバリデーション
    def clean_email(self):
        email = self.cleaned_data['email']
        #的にだがどりあえず
        if re.match(r'.+@+',email) == None:
            raise forms.ValidationError("メールアドレスではありません。")
        return email