from django.shortcuts import render
import requests 
from django.http import JsonResponse
import string
from django.core.files.storage import default_storage
from random import * 
from django.conf import settings
import textwrap
import os 
from docx2pdf import convert
import re 
from fpdf import FPDF
from .models import txt_to_pdf, feedback, docx_to_pdf


"""Function to convert binary numbers to integers"""
def valid_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def home(request): 
	converters = (['Binary to number converter', 'binary_to_number_converter', "html/binary_to_number_converter.html"], ['Number to binary converter', 'number_to_binary_converter', "html/number_to_binary_converter.html"], ['Hours to seconds converter', 'hours_to_seconds_converter', "html/hours_to_seconds_converter.html"], ['TXT document to pdf', 'txt_document_to_pdf_converter', 'html/txt_document_to_pdf_converter.html'], ['DOCX to PDF', 'docx_to_pdf_converter', 'html/docx_to_pdf_converter.html'] )

	generators = (['Password Generator', 'password_generator', 'html/password_generator.html'],)
	context = { 
		'converters' : converters,
		'generators' : generators,

	}
	return render(request, 'html/home.html', context) 

def binary_to_number_converter(request):
	number_input = str(request.GET.get('inputted'))
	if "0b" in number_input:
		number_input = number_input.replace("Ob","")
	try:	
		new_number = int(number_input, 2)
	except: 
		new_number = "Please enter a valid number."
	new_number = str(new_number)

	data = {
		'new_number' : new_number, 
	}
	return JsonResponse(data) 

def hours_to_seconds_converter(request):
	number_input = str(request.GET.get('inputted'))
	try:
		number_input = int(number_input) * 60 * 60
	except: 
		number_input = "Please enter a valid number."
	data = {
		'number_input' : number_input,
	}
	return JsonResponse(data)

def number_to_binary_converter(request):
	number_input = str(request.GET.get('inputted'))
	number_input = bin(int(number_input))
	data = { 
		'number_input' : number_input,
	}
	return JsonResponse(data) 

def password_generator(reqeust): 
	characters = string.ascii_letters + string.punctuation + string.digits 
	password = "".join(choice(characters) for x in range(randint(8,16)))
	data = {
		'number_input' : password, 
	}
	return JsonResponse(data)

def send_feedback(request): 
	subject = request.GET.get('subject')
	email = request.GET.get('email')
	suggestion = request.GET.get('suggestion')
	email_test = valid_email(email) 
	if email_test == False: 
		message = "Please enter a valid email address" 
		data = { 
			'message' : message, 
		}
		return JsonResponse(data)
	new_object = feedback(subject=subject, email=email, suggestion=suggestion)
	new_object.save()
	message = "Feedback delivered" 
	data = { 
		'message' : message, 
	}
	return JsonResponse(data)

def txt_document_to_pdf_converter(request): 
	txt_file = request.FILES.get('txt_file')
	new_object = txt_to_pdf(txt_file = request.FILES.get('txt_file'))
	pdf = FPDF() 
	pdf.add_page() 
	pdf.set_font('arial', size=10)
	path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
	new_object.save()
	txt_path = path+new_object.txt_file.url
	pdf_c_path = txt_path.replace(".txt", ".pdf")
	pdf_path = "http://toolkit-website.herokuapp.com" + new_object.txt_file.url
	pdf_path = pdf_path.replace(".txt", ".pdf")
	text_file = open(txt_path, 'r')
	for text in text_file:
		pdf.cell(200, 10, txt = text, ln=1,align='L') 
	pdf.output(pdf_c_path)	
	new_object.pdf_file = pdf_path
	new_object.save()
	data = {
		'pdf_path' : pdf_path
	}
	return JsonResponse(data)

def docx_to_pdf_converter(request): 
	new_object = docx_to_pdf(docx_file = request.FILES.get('docx_file'))
	path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
	new_object.save()
	txt_path = path+new_object.docx_file.url
	pdf_c_path = txt_path.replace(".docx", ".pdf")
	convert(txt_path, pdf_c_path)	
	new_path = new_object.docx_file.url 
	new_path = new_path.replace('docx', 'pdf')
	new_path = new_path.replace('/media/', '') 
	new_object.pdf_file = new_path
	pdf_path = "https://toolkit-website.herokuapp.com/" + new_object.pdf_file.url
	print(pdf_path)
	print(new_path)
	print(txt_path)
	new_object.save()
	data = {
		'new_url' : pdf_path
	}
	return JsonResponse(data)

