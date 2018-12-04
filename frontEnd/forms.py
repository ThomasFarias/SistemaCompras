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
		self.helper.form_id= 'formularioUsuario'
		self.fields['username'].label = 'Nombre de Usuario'
		self.fields['email'].label = 'Correo Electronico'
		self.fields['username'].help_text = None
		self.fields['password'].label = 'Contraseña'
		self.fields['password'].widget = forms.PasswordInput()
		


		self.helper.layout = Layout(
			
			Div(
				Div('username', css_class=""),
				Div('email', css_class=""),
				Div('password', css_class=""),
				Div('password2', css_class=""),
				css_class = 'column'
			),
			Div(
				ButtonHolder(
						Submit('save', 'Enviar', css_class="BotonEnviar btn-secondary")
				)
			),
		)

class FormLogin(forms.ModelForm):


	class Meta:
		model = User
		
		fields = ('username', 'password')


	def __init__(self, *args, submit_title="Enviar", **kwargs):
		super().__init__(*args, **kwargs)
		#user = super().save(commit=False) #snippet
		self.helper=FormHelper()
		self.helper.form_id= 'formLogin'
		self.fields['username'].label = 'Nombre de Usuario'
		self.fields['username'].help_text = None
		self.fields['password'].label = 'Contraseña'
		self.fields['password'].widget = forms.PasswordInput()
		

		self.helper.layout = Layout(
			
			Div(
				Div('username', css_class=""),
				Div('password', css_class=""),
				css_class = 'column'
			),
			Div(
				ButtonHolder(
						Submit('save', 'Ingresar', css_class="BotonEnviar btn-secondary")
				)
			),
		)
       