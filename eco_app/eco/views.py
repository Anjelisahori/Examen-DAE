from django.shortcuts import render, redirect, get_object_or_404
from .models import EcoHabit
from .forms import EcoHabitForm
import requests

# 🧠 Función para obtener un consejo desde una API externa
def obtener_consejo():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        return f"{data[0]['q']} - {data[0]['a']}"
    except:
        return "Cuida el planeta, es el único hogar que tenemos."

# 🏠 Vista principal (inicio)
def index(request):
    habitos = EcoHabit.objects.all()
    total = habitos.count()
    cumplidos = habitos.filter(cumplido=True).count()
    porcentaje = int((cumplidos / total) * 100) if total else 0
    consejo = obtener_consejo()

    # 🏅 Lógica de logros según hábitos cumplidos
    logros = []
    if cumplidos >= 1:
        logros.append("🥉 EcoIniciado")
    if cumplidos >= 3:
        logros.append("🥈 EcoIntermedio")
    if cumplidos >= 5:
        logros.append("🥇 EcoHéroe")

    return render(request, 'index.html', {
        'habitos': habitos,
        'porcentaje': porcentaje,
        'consejo': consejo,
        'logros': logros
    })

# ➕ Agregar un nuevo hábito
def agregar_habito(request):
    form = EcoHabitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'habit_form.html', {'form': form})

# ✏️ Editar un hábito existente
def editar_habito(request, pk):
    habito = get_object_or_404(EcoHabit, pk=pk)
    form = EcoHabitForm(request.POST or None, instance=habito)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'habit_form.html', {'form': form})

# 🗑️ Eliminar un hábito
def eliminar_habito(request, pk):
    habito = get_object_or_404(EcoHabit, pk=pk)
    habito.delete()
    return redirect('index')
