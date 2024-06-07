import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", 'rb'))
corresponding_movies = pickle.load(open("corresponding_movies", 'rb'))
movies_list = movies['title'].values

st.header("Want to find a movie that is similar to your favorites ?")
selectvalue = st.selectbox("Select movie:", movies_list)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=10261a3dc163b01000728bce8ea4303f".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster = data['poster_path']
    full_poster = "https://image.tmdb.org/t/p/w500/"+poster
    return full_poster

def recommendFunction(movie):
    index = movies[movies['title']==movie].index[0]
    checker = sorted(list(enumerate(corresponding_movies[index])),reverse=True, key=lambda vector:vector[1])
    give_newmovie = []
    give_poster = []
    for i in checker[1:6]:
        movies_id = movies.iloc[i[0]].id
        give_newmovie.append(movies.iloc[i[0]].title)
        give_poster.append(fetch_poster(movies_id))
    return give_newmovie, give_poster


if st.button("Show recommended"):
    movie_name, movie_poster = recommendFunction(selectvalue)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])