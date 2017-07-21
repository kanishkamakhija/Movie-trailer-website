import media
import fresh_tomatoes

# This file contains list of movie objects

love_story = media.Movie("Love Rosie",
                         "love story",
                         "http://www.impawards.com/2014/posters/love_rosi"
                         "e_ver5_xlg.jpg",
                         "https://www.youtube.com/watch?v=5zL3YJKygd4")

avatar = media.Movie("Avatar",
                     "marine on alien planet",
                     "http://moviecultists.com/wp-content/upl"
                     "oads/2009/11/avatar-poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

now_you_see_me = media.Movie("Now You See Me",
                             "The Four Horsemen resurface and are forcibly"
                             "recruited by a"
                             "tech genius to pull off their"
                             " most impossible heist yet.",
                             "http://www.impawards.com/2016"
                             "/posters/now_you_see_me_two_ver23_xxlg.jpg",
                             "https://www.youtube.com/watch?v=KzJNYYkkhzc")

a_beautiful_mind = media.Movie("A Beautiful Mind",
                               "A Beautiful Mind is a 2001 Am"
                               "erican biographical drama"
                               "film based on the life of"
                               " John Nash, a Nobel Laureate"
                               "in Economics.",
                               "https://media.licdn.com/mpr/mp"
                               "r/AAEAAQAAAAAAAAk5AAAAJDA"
                               "3ZmFmY2RjLWRlNTktNGUyMS1hMmE3L"
                               "TU5NTZhOTAxOWRkNQ.jpg",
                               "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

divergent = media.Movie("Divergent",
                        "Tris, an adult resident of a futuristic world"
                        "divided into five factions, elects to join the"
                        "Dauntless faction. But she actually belongs to"
                        "another faction, which she must hide, as a major"
                        "war looms.",
                        "http://resizing.flixster.com/ATk50ODLNE5Kua1DSOg"
                        "ST5ct-38=/800x1200/v1.bTsxMTE3ODk"
                        "xMDtqOzE3NDE5OzIwNDg7ODAwOzEyMDA",
                        "https://www.youtube.com/watch?v=sutgWjz10sM")

insurgent = media.Movie("Insurgent",
                        "The Divergent Series: Insurgent (also known simpl"
                        "y as Insurgent) is a 2015 American science fiction"
                        "action film directed by Robert Schwentke, based"
                        "on Insurgent, the second book in the Divergent"
                        "trilogy by Veronica Roth. It is the sequel to"
                        "the 2014 film Divergent and the second installment"
                        "in The Divergent Series",
                        "https://images-na.ssl-images-amazon.com/imag"
                        "es/I/51uewbwd7nL.jpg",
                        "https://www.youtube.com/watch?v=UtgPdoxU-SY")

movies = [love_story,
          avatar,
          now_you_see_me,
          a_beautiful_mind,
          divergent,
          insurgent]

fresh_tomatoes.open_movies_page(movies)
