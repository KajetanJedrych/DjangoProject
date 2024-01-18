from django.shortcuts import render


rooms = [
    {'id':1, 'name': 'Porozmawiajmy o Pilipiuku'},
    {'id':2, 'name': 'Porozmawiajmy o "Dawno temu w Warszawie" '},
    {'id':3, 'name': 'Porozmawiajmy o "Zły"'},


]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'playground/home.html', context)

def room(request, pk):
    room = None
    for i  in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}

    return render(request, 'playground/room.html', context)
