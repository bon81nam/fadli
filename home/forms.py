from django.forms import ModelForm
from django import forms
from .models import InputFormModel



#Jabatan_Choices = [
   # ('JKA', 'JABATAN KEJURUTERAAN AWAM'),
   # ('JKE', 'JABATAN KEJURUTERAAN ELEKTRIK'),
   # ('JKM', 'JABATAN KEJURUTERAAN MEKANIKAL'),
   # ('JP', 'JABATAN PERDAGANGAN'),
   # ('JTMK', 'JABATAN TEKNOLOGI MAKLUMAT DAN KOMPUTER'),
   # ('JKPK', 'JABATAN KEJURUTERAAN PETROKIMIA'),
   # ('JPA', 'JABATAN PENGAJIAN AM'),
   # ('JMSK', 'JABATAN MATEMATIK, SAINS DAN KOMPUTER')
#]

#Tempoh_Aktiviti_Choices = [
   # ('1st_half', 'Sesi Jan - Jun'),
   # ('2nd_half', 'Sesi Jul - Ogos')
#]

#KPI_Choices = [
    #('KPI 1', 'KPI 1: Taklimat OBE kepada pelajar baharu & pensyarah kursus mengikut keperluan manual ETAC dan Garis Panduan Amalan Baik MQA'),
    #('KPI 2', 'KPI 2: Taklimat dan memastikan pensyarah kursus memahami rekabentuk kurikulum'),
    #('KPI 3', 'KPI 3: Taklimat  merancang penilaian dengan mengikut keperluan kurikulum'),
    #('KPI 4', 'KPI 4: Taklimat  membaca laporan CORR dan penghasilan CQI')
#]


class InputForm(ModelForm):
    class Meta:
        model = InputFormModel
        fields = '__all__'

        widgets = {
            'JABATAN' : forms.Select({'class':'form-control'}),
#            'Penyelaras' : forms.TextInput({'class':'form-control'}),
#            'Ketua_Jabatan' : forms.TextInput({'class':'form-control'}),
            'Tempoh' : forms.Select({'class':'form-control'}),
            'tahun' : forms.Select({'class':'form-control'}),
            'KPI' : forms.Select({'class':'form-control'}),
            'Tajuk_Aktiviti' : forms.TextInput({'class':'form-control'}),
            'Tarikh_Aktiviti' : forms.SelectDateWidget(),
            'Objektif_Aktiviti' : forms.Textarea({'class':'form-control'}),
            'Catatan' : forms.Textarea({'class':'form-control'})
            }

    #Tajuk_KPI_Pertama = forms.CharField(initial= 'KPI 1 adalah aktiviti berkaitan TAKLIMAT OBE PELAJAR', label='NAMA AKTIVITI KPI 1', widget=forms.TextInput(attrs={'size':50}))
    #Tarikh_KPI_Pertama = forms.DateField(label='TARIKH AKTIVITI 1', widget=forms.SelectDateWidget)
    #Objektif_KPI_Pertama = forms.CharField(label='OBJEKTIF AKTIVITI 1', widget=forms.Textarea)
    #Tajuk_KPI_Kedua = forms.CharField(initial= 'KPI 2 adalah aktiviti berkaitan PEMBINAAN ITEM', label='NAMA AKTIVITI KPI 2', widget=forms.TextInput(attrs={'size':50}))
    #Tarikh_KPI_Kedua = forms.DateField(label='TARIKH AKTIVITI 2', widget=forms.SelectDateWidget)
    #Objektif_KPI_Kedua = forms.CharField(label='OBJEKTIF AKTIVITI 2', widget=forms.Textarea)
    #Tajuk_KPI_Ketiga = forms.CharField(initial= 'KPI 3 adalah aktiviti berkaitan TAKLIMAT OBE PENSYARAH', label='NAMA AKTIVITI KPI 3', widget=forms.TextInput(attrs={'size':50}))
    #Tarikh_KPI_Ketiga = forms.DateField(label='TARIKH AKTIVITI 3', widget=forms.SelectDateWidget)
    #Objektif_KPI_Ketiga = forms.CharField(label='OBJEKTIF AKTIVITI 3', widget=forms.Textarea)
    #Tajuk_KPI_Keempat = forms.CharField(initial= 'KPI 4 adalah aktiviti berkaitan CQI', label='NAMA AKTIVITI KPI 4', widget=forms.TextInput(attrs={'size':50}))
    #Tarikh_KPI_Keempat = forms.DateField(label='TARIKH AKTIVITI 4', widget=forms.SelectDateWidget)
    #Objektif_KPI_Keempat = forms.CharField(label='OBJEKTIF AKTIVITI 4', widget=forms.Textarea)
