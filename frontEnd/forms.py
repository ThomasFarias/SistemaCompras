from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe          



class FormRegistroUsuario(forms.ModelForm):
	password2 =forms.CharField(widget=forms.PasswordInput(),label="Confirmar contraseña")

	class Meta:
		model = User
		# specify what fields should be used in this form.
		fields = ('email',
				'username', 'password'
				)


	def __init__(self, *args, submit_title="Enviar", **kwargs):
		super().__init__(*args, **kwargs)
		#user = super().save(commit=False) #snippet
		self.helper=FormHelper()
		self.fields['username'].label = 'Nombre de usuario'
		self.fields['username'].help_text = None
		self.fields['password'].label = 'Contraseña'
		self.fields['password'].widget = forms.PasswordInput()
		


		self.helper.layout = Layout(
			
			Div(
				Div('username', css_class="col-sm-6"),
				Div('email', css_class="col-sm-6"),
				css_class = 'row'
			),
			
			Div(
				Div('password', css_class="col-sm-6"),
				Div('password2', css_class="col-sm-6"),
				css_class = 'row'
			),
			ButtonHolder(
						Submit('save', 'Enviar')
			)
		)
       