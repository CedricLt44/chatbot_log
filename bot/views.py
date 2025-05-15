from django.shortcuts import render

# Create your views here.

def bot_page(request):
  return render(request,'bot/bot.html')