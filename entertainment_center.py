import fresh_tomatoes
import media

pursuit_of_happiness=media.Movie("Pursuit Of Hapiness",
                                 "Life struggle to happiness",
                                 "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                                 "https://www.youtube.com/watch?v=89Kq8SDyvfg")
                                 
fantastic_fox=media.Movie("fantastic Mr Fox",
                         "Fox story",
                         "https://upload.wikimedia.org/wikipedia/en/a/af/Fantastic_mr_fox.jpg",
                         "https://www.youtube.com/watch?v=n2igjYFojUo")
zootopia=media.Movie("zootopia",
                     "Bunny police officer",
                     "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                     "https://www.youtube.com/watch?v=jWM0ct-OLsM")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toy that come to life",
                        "https://i.ytimg.com/vi/8gL2nKAa9Q8/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc" )
avatar = media.Movie("Avatar",
                     "A marine goes to alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY" )
jason_bourne=media.Movie("Jason Bourne",
                         "FBI officer on run",
                         "https://upload.wikimedia.org/wikipedia/en/b/b2/Jason_Bourne_%28film%29.jpg",
                         "https://www.youtube.com/watch?v=MIJ53m77-kw")

movies=[jason_bourne,pursuit_of_happiness,fantastic_fox,zootopia,toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)

