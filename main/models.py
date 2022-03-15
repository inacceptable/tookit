from django.db import models

# Create your models here.
class txt_to_pdf(models.Model):
	txt_file = models.FileField(upload_to='PDF_to_txt', blank=True)
	pdf_file = models.FileField(upload_to='PDF_to_txt', blank=True)

class feedback(models.Model): 
	subject = models.CharField(max_length = 100) 
	email = models.CharField(max_length = 100) 
	suggestion = models.TextField() 
	def __str__(self):
		return self.subject