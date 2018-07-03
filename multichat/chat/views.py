from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room,QuestionBank


@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")

    questionbank = QuestionBank.objects.order_by("question_no")
    # Render that in the index template
    return render(request, "index.html", {
        "rooms": rooms,
        "questionbank":questionbank
    })
