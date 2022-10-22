from django.db import OperationalError
from django.http import Http404
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required,permission_required

from movies.forms import MovieForm
from movies.models import Movie


def get_movies(request ):
    movies = Movie.objects.all()
    context = {
        "movies": movies,
    }
    return render(request, "movie_list.html", context)


def get_movie(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except (OperationalError, Movie.DoesNotExist):
        raise Http404(f"no movie found matching {movie_id}")

    context = {
        "movie": movie,
    }
    return render(request, "movie_detail.html", context)

@login_required
@permission_required("movies.view_movies")
def create_movie(request):
    form = MovieForm()
    if request.method == "POST":
        # BONUS: This needs to have the `user` injected in the constructor
        # somehow
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "form": form,
    }
    

    return render(request, "movie_create.html", context)

