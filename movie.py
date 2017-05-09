import media
import fresh_tomatoes

#this contains list of movies

love_story = media.Movie("Love Rosie", "love story", "http://www.impawards.com/2014/posters/love_rosie_ver5_xlg.jpg", "https://www.youtube.com/watch?v=Te8rfiN6_Qo")
#print(love_story.storyline)
avatar = media.Movie("Avatar", "marine on alien planet", "http://moviecultists.com/wp-content/uploads/2009/11/avatar-poster.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

now_you_see_me = media.Movie("Now You See Me", "The Four Horsemen resurface and are forcibly recruited by a tech genius to pull off their most impossible heist yet.", "http://www.impawards.com/2016/posters/now_you_see_me_two_ver23_xxlg.jpg", "https://www.youtube.com/watch?v=4I8rVcSQbic")

a_beautiful_mind = media.Movie("A Beautiful Mind", "A Beautiful Mind is a 2001 American biographical drama film based on the life of John Nash, a Nobel Laureate in Economics.","https://media.licdn.com/mpr/mpr/AAEAAQAAAAAAAAk5AAAAJDA3ZmFmY2RjLWRlNTktNGUyMS1hMmE3LTU5NTZhOTAxOWRkNQ.jpg", "https://fmovies.is/film/a-beautiful-mind.rlxm")

divergent = media.Movie("Divergent", "Tris, an adult resident of a futuristic world divided into five factions, elects to join the Dauntless faction. But she actually belongs to another faction, which she must hide, as a major war looms.","http://resizing.flixster.com/ATk50ODLNE5Kua1DSOgST5ct-38=/800x1200/v1.bTsxMTE3ODkxMDtqOzE3NDE5OzIwNDg7ODAwOzEyMDA", "https://fmovies.is/film/divergent.2950")

insurgent = media.Movie("Insurgent" , "The Divergent Series: Insurgent (also known simply as Insurgent) is a 2015 American science fiction action film directed by Robert Schwentke, based on Insurgent, the second book in the Divergent trilogy by Veronica Roth. It is the sequel to the 2014 film Divergent and the second installment in The Divergent Series","https://images-na.ssl-images-amazon.com/images/I/51uewbwd7nL.jpg", "https://xmovies8.org/watch?v=Insurgent_2015")
#print(avatar.storyline)
#love_story.show_trailer()
movies = [love_story, avatar, now_you_see_me,a_beautiful_mind,divergent,insurgent]
fresh_tomatoes.open_movies_page(movies)
#print(movie.Movie.VALID_RATINGS)
#print(movie.Movie.__doc__)
#print(movie.Movie.__name__)
#print(movie.Movie.__module__)
