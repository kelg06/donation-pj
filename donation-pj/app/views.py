from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe 

stripe.api_key = "sk_test_51Qc7F6FdYIKcNkBIyzoag1jC9Yk0MP2pqWGvkbpjTFciLkLrybnMiNFMfO2c3aAnFLfr8pndLV7ndwlRhXCMVOIh00sb9oPmPf"

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def donate(request):
    return render(request, "donate.html")

def thank_you(request):
    return render(request, "thankyou.html")

def index(request):
    return render(request, 'payment/checkout.html')

def charge(request):
    return render(request, "payment/template.html")

def successMsg(request, args):
    amount = args
    return render(request, 'payment/success.html', {'amount':amount})