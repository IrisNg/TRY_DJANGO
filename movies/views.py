from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer 

# Route
def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def movie_list(request):
    # get all movies, serialize them, return json
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)


def home(request):
    return HttpResponse("welcome home")

def movie_detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def create_movie(request):
    # Get body data from POST request
    title = request.POST.get('title')
    if title:
        # Create new movie row in db
        movie = Movie(title=title)
        movie.save()
        # Redirect to listing page
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/create.html')

def delete_movie(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')

    movie.delete()
    return HttpResponseRedirect('/movies')