from django.shortcuts import render
from django.http import JsonResponse
from .ciphers import caesar_encode

def greetings(request):
    return JsonResponse({'message': 'Hello, World!'})

def encode(request,plaintext,shift):
    parameters=dict(request.GET)
    print(parameters)
    return JsonResponse({'cipher_text': caesar_encode(plaintext,shift)})

