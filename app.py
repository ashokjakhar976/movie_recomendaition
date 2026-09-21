import streamlit as st
import pickle as pkl
import pandas as pd
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = simi[index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    finalmovies = []

    for i in movies_list:
        movie_id = i[0]
        finalmovies.append(movies.iloc[i[0]]['title'])

    return finalmovies
# 52ab92a041192fc37188ba505d0fca24
simi = pkl.load(open('simi.pkl', 'rb'))
movies_list =pkl.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)


st.title('Movie Recommendation System')
secleted_movie_name = st.selectbox('hello' , movies['title'].values )

if(st.button('Recommend')):
    recommendtion= recommend (secleted_movie_name)
    for i in recommendtion:
     st.write(i)
