from django import forms

class RegistrarFuncionario(forms.Form):

	nome = form.CharField(required=True)
	email = form.CharField(required=True)
	senha = form.CharField(required=True)
	telefone = form.CharField(required=True)
	empresa = form.CharField(required=True)