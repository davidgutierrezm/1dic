from django import forms
class FormularioPacientes(forms.Form):

    TIPOAFILIADO = (
        (1,'Cotizante'),
        (2,'Beneficiario')
        
    )
    REGIMEN = (
        (1,'Contributivo'),
        (2, 'Subsidiado')

    )
    GRUPOINGRESO = (
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (3, 'D')
    )

    nombre = forms.CharField(
        widget = forms.TextInput(attrs={"class":"form-control mb-3"}),
        required = True,
        max_length = 15
    )
    apellidos = forms.CharField(
        widget = forms.TextInput(attrs={"class":"form-control mb-3"}),
        required = True,
        max_length = 35
    )
    cedula = forms.CharField(
        widget = forms.TextInput(attrs={"class":"form-control mb-3"}),
        required = True,
        max_length = 10
    )
    tipo_afiliado = forms.ChoiceField(
        widget = forms.Select(attrs={"class":"form-select mb-3"}),
        required = True,
        choices = TIPOAFILIADO
    )
    regimen = forms.ChoiceField(
        widget = forms.Select(attrs={"class":"form-select mb-3"}),
        required = True,
        choices = REGIMEN
    )
    grupo_ingreso = forms.ChoiceField (
        widget = forms.Select(attrs={"class":"form-select mb-3"}),
        required = True,
        choices = GRUPOINGRESO
    )
    celular = forms.CharField(
        widget = forms.TextInput(attrs={"class":"form-control mb-3"}),
        required = True,
        max_length = 15
    )
    correo = forms.CharField(
        widget = forms.TextInput(attrs={"class":"form-control mb-3"}),
        required = True,
        max_length = 15
    )