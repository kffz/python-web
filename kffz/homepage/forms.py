#coding=UTF-8
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

import re

class SignupForm(forms.ModelForm):
    username = forms.CharField(label='用户名',required=True,error_messages={'required':'Please enter your username','max_length':'over 16','min_length':'less than 4'},\
                               max_length=16,min_length=4,widget=forms.TextInput(attrs={'placeholder':'4~16'}));
    email = forms.EmailField(label='email',error_messages={'required':'Please enter your email','invalid':'Please enter the correct email'});
    password = forms.CharField(label='密码',required=True,error_messages={'required':'Please enter your password','max_length':'over 20',\
                                                             'min_length':'less than 6'},max_length=20,min_length=6,widget=forms.PasswordInput(attrs={'placeholder':'6-20'}));
    confirm_password = forms.CharField(error_messages={'required':'Please enter your password','max_length':'over 20','min_length':'less than 6'}, \
                                       label='确认密码', max_length=20, min_length=6, widget=forms.PasswordInput(attrs={'placeholder': '6-20'}))
    class Meta:
        model = get_user_model()
        fields = ('username','email','password')


    def cleaned_email(self):
        UserModel = get_user_model()
        email  = self.cleaned_data['email']
        try:
            UserModel._default_manager.get(email=email)
        except:
            return email
        raise forms.ValidationError('该邮箱地址已被注册')

    def clean_confirm_password(self):
         password = self.cleaned_data['password']
         confirm_password = self.cleaned_data['confirm_password']
         if not(password == confirm_password):
              raise forms.ValidationError('确认密码和密码不一致')
         return confirm_password

    def clean_username(self):
        UserModel = get_user_model()
        username = self.cleaned_data['username']
        n=re.sub('[^\u4e00-\u9fa5a-zA-Z]','',username)
        mgc = ['admin','qaq','kffz','KFFZ']
        if n in mgc:
            raise forms.ValidationError('Please change an username')
        try:
            UserModel._default_manager.get(username=username)
        except:
            return username
        raise forms.ValidationError('有人已经注册了该名称')

#class ArticleForm(forms.ModelForm):
    #title = forms.CharField(label="标题",required=True,error_messages={'required':'请输入您文章标题','max_length':'标题长度不超过30个字','min_length':'标题长度不小于5个字'},\
    #                        max_length=30,min_length=5,widget=forms.TextInput(attrs={'placeholder':'请输入您文章标题，5到30字之间'}))
    #tag = forms.CharField(label="标签",required=False,error_messages={'max_length':'标签长度不超过10个字'},max_length=10,widget=forms.TextInput(attrs={'placeholder':'请输入您文章的标签'}))
    #content = forms.MultiValueField