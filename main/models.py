from django.db import models

# Create your models here.
class txt_to_pdf(models.Model):
	txt_file = models.FileField(upload_to='PDF_to_txt', blank=True)
	pdf_file = models.FileField(upload_to='PDF_to_txt', blank=True)