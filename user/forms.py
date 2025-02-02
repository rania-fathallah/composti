from django import forms

class modifer(forms.Form):
    nom = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
                          'id': "nom", 'name': "nom", 'class':"form-control border border-success mb-3 h3"}))
    prenom = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
                             'id': 'prenom', 'name': 'prenom','class':"form-control border border-success mb-3 h3"}))
    telephone = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
        attrs={'id': 'NB_GSM', 'name': 'NB_GSM', 'class':"form-control border border-success mb-3 h3"}))
    
    def is_valid(self):
        telephone = self.data['telephone']
        if not telephone.isdigit():
            self.add_error("telephone", "Téléphone est incorrect!")
        nom = self.data['nom']
        if any(char.isdigit() for char in nom):
            self.add_error("nom", "Nom est incorrect!")
        prenom = self.data['prenom']
        if any(char.isdigit() for char in prenom):
            self.add_error("prenom", "Prenom est incorrect!")
        value = super(modifer, self).is_valid()
        return value
