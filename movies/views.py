from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer 

# GET api, returns json instead
# POST api, reads from json body
# Only GET & POST triggers this view function due to the decorator
@api_view(['GET', 'POST'])
def movies_REST(request, format=None):
    if request.method == 'GET':
        # get all movies, serialize them, return json
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        # request.data includes both json data and form data
        # + other differences from request.POST
        # serializer converts to python dict
        serializer = MovieSerializer(data=request.data)
        # Built in validation helper
        if serializer.is_valid():
            # Save to db
            serializer.save()
            # Return json response with 201 status code
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_REST(request, id, format=None):
    try:
        # django ORM throws error if object not found
        movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Route
def get_movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})


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