from django.contrib import admin
from .models import txt_to_pdf, feedback, docx_to_pdf

admin.site.register(txt_to_pdf)
admin.site.register(feedback)
admin.site.register(docx_to_pdf)