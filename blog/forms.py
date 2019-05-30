from django import forms
from .models import Blog

class BlogForms(forms.ModelForm):
    class Meta:  #대표하는 특징
        #우리가 만들어주는 클래스의 특징을 규정해줌
        model = Blog
        fields = ('title','body',) #모델안에 있는 필드중에서우리가 form으로 띄어주고 싶은 것
