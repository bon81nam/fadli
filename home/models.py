from django.db import models


class InputFormModel(models.Model):
    Jabatan_Choices = [
        ('JABATAN KEJURUTERAAN AWAM', 'JABATAN KEJURUTERAAN AWAM'),
        ('JABATAN KEJURUTERAAN ELEKTRIK', 'JABATAN KEJURUTERAAN ELEKTRIK'),
        ('JABATAN KEJURUTERAAN MEKANIKAL', 'JABATAN KEJURUTERAAN MEKANIKAL'),
        ('JABATAN PERDAGANGAN', 'JABATAN PERDAGANGAN'),
        ('JABATAN TEKNOLOGI MAKLUMAT DAN KOMPUTER', 'JABATAN TEKNOLOGI MAKLUMAT DAN KOMPUTER'),
        ('JABATAN KEJURUTERAAN PETROKIMIA', 'JABATAN KEJURUTERAAN PETROKIMIA'),
        ('JABATAN PENGAJIAN AM', 'JABATAN PENGAJIAN AM'),
        ('JABATAN MATEMATIK, SAINS DAN KOMPUTER', 'JABATAN MATEMATIK, SAINS DAN KOMPUTER')
    ]

    Tempoh_Aktiviti_Choices = [
        ('JAN - JUL', 'Sesi Jan - Jun'),
        ('JUL - OGOS', 'Sesi Jul - Ogos')
    ]

    KPI_Choices = [
        ('KPI1',
         'KPI 1: Taklimat OBE kepada pelajar baharu & pensyarah kursus mengikut keperluan manual ETAC dan Garis Panduan Amalan Baik MQA'),
        ('KPI2', 'KPI 2: Taklimat dan memastikan pensyarah kursus memahami rekabentuk kurikulum'),
        ('KPI3', 'KPI 3: Taklimat  merancang penilaian dengan mengikut keperluan kurikulum'),
        ('KPI4', 'KPI 4: Taklimat  membaca laporan CORR dan penghasilan CQI')
    ]

    Date_Choices = [
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026')
    ]

    JABATAN = models.CharField(choices=Jabatan_Choices, max_length=200)
#    Penyelaras = models.CharField(max_length=200)
#    Ketua_Jabatan = models.CharField(max_length=200)
    Tempoh = models.CharField(max_length=200, choices=Tempoh_Aktiviti_Choices)
    tahun = models.CharField(max_length=200, choices=Date_Choices)
    KPI = models.CharField(max_length=200, choices=KPI_Choices)
    Tajuk_Aktiviti = models.CharField(max_length=200)
    Tarikh_Aktiviti = models.DateField()
    Objektif_Aktiviti = models.TextField(max_length=1000)
    Catatan = models.TextField(max_length=1000)

    def __str__(self):
        return self.Tajuk_Aktiviti
