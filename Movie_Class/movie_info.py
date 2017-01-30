import movie_class
import fresh_tomatoes

toy_story = movie_class.Movie("Toy Story","A story of toys","https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story1 = movie_class.Movie("Toy Story","A story of toys","https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story2 = movie_class.Movie("Toy Story","A story of toys","https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

#toy_story.show_trailer()

movies = [toy_story,toy_story1,toy_story2]
#fresh_tomatoes.open_movies_page(movies)

print(movie_class.Movie.__doc__)