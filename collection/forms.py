from django import forms
from collection.models import Newsletter_subscriber, Simulation_model, Uploaded_dataset


class Subscriber_registrationForm(forms.ModelForm):
	class Meta:
		model = Newsletter_subscriber
		fields = ('first_name', 'email', )


class Subscriber_preferencesForm(forms.ModelForm):
	class Meta:
		model = Newsletter_subscriber
		fields = ('is_templar', 'is_alchemist', 'is_scholar', )
		# fields = ('email', 'userid', 'first_name', 'is_templar', 'is_alchemist', 'is_scholar', 'created', 'updated',)


class Simulation_modelForm(forms.ModelForm):
	class Meta:
		model = Simulation_model
		fields = ('name', 'specification', )



class UploadFileForm(forms.Form):
    file = forms.FileField()

class Uploaded_datasetForm2(forms.ModelForm):
	class Meta:
		model = Uploaded_dataset
		fields = ('name', 'content_specification', )

class Uploaded_datasetForm3(forms.ModelForm):
	class Meta:
		model = Uploaded_dataset
		fields = ('name', 'context_specification', )
