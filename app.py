import streamlit as st
import pickle
import requests
import pandas as pd

def poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=df5dae4f7e94b86eb0507c309742f165&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/original' + data['poster_path']
def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_lists = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recom_movies = []
    recom_movie_posters = []
    for i in movies_lists:
        recom_movies.append(movie_list.iloc[i[0]].title)
        recom_movie_posters.append(poster(movie_list.iloc[i[0]].movie_id))
    return recom_movies,recom_movie_posters

movie_list = pickle.load(open('movies.pkl','rb'))
movie_list_names = movie_list['title'].values

similarity = pickle.load(open('simi.pkl','rb'))
st.title('Movie-Recommender-System')

selected_movie = st.selectbox(
    'Which movie would you like to watch?',
    movie_list_names
)

if st.button('recommend'):
    recomended_movies,posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(recomended_movies[0])
        st.image(posters[0])
    with col2:
        st.header(recomended_movies[1])
        st.image(posters[1])
    with col3:
        st.header(recomended_movies[2])
        st.image(posters[2])
    with col4:
        st.header(recomended_movies[3])
        st.image(posters[3])
    with col5:
        st.header(recomended_movies[4])
        st.image(posters[4])