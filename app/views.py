from django.shortcuts import render
from django_user_agents.utils import get_user_agent
import socket

# Create your views here.
def index(request):
    return render(request, 'app/index.html', {})

def info(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        tipo = 'Movil'
    elif user_agent.is_tablet:
        tipo = 'Tablet'
    elif user_agent.is_pc:
        tipo = 'PC'
    elif user_agent.is_bot:
        tipo = 'Bot'
    esTactil = "Si" if user_agent.is_touch_capable else "No"
    hostname = socket.gethostname()  # Obtengo
    ip_address = socket.gethostbyname(hostname)
    return render(request, 'app/info.html', {
        'nombrehost': hostname, 'ipcliente': ip_address, 'tactil': esTactil, 'device': tipo
    })