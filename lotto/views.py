from django.shortcuts import render
from .models import LottoTicket

import random


winning_numbers = sorted(random.sample(range(1, 46), 6))


def calculate_rank(user_numbers, winning_numbers):

    match_count = len(
        set(user_numbers) & set(winning_numbers)
    )

    if match_count == 6:
        return "1등"

    elif match_count == 5:
        return "3등"

    elif match_count == 4:
        return "4등"

    elif match_count == 3:
        return "5등"

    else:
        return "낙첨"


def home(request):

    if request.method == 'POST':

        manual_numbers = request.POST.get(
            'manual_numbers'
        )

        LottoTicket.objects.create(
            numbers=manual_numbers
        )

        numbers = manual_numbers.split()

    else:

        numbers = sorted(
            random.sample(range(1, 46), 6)
        )

        number_string = " ".join(
            map(str, numbers)
        )

        LottoTicket.objects.create(
            numbers=number_string
        )

    context = {
        'numbers': numbers,
        'winning_numbers': winning_numbers
    }

    return render(
        request,
        'lotto/home.html',
        context
    )


def history(request):

    tickets = LottoTicket.objects.all()

    for ticket in tickets:

        user_numbers = list(
            map(int, ticket.numbers.split())
        )

        ticket.result = calculate_rank(
            user_numbers,
            winning_numbers
        )

        ticket.save()

    context = {
        'tickets': tickets,
        'winning_numbers': winning_numbers
    }

    return render(
        request,
        'lotto/history.html',
        context
    )