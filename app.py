import streamlit as st
import pickle
import pandas as pd
#import requests
# api not working
# def fetch_poster(movie_id):
#     #response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=442ba11230c60218d707d0f65560af2c&language=en-US'.format(movie_id))
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

movie_dict = pickle.load(open('movielist.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('dist_matrix.pkl','rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    # recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        # movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

st.header("Movie Recommendation system")

list_of_movies = movies['title'].values
selected_movie = st.selectbox(
'',
list_of_movies
)
st.markdown(
    f'<p style="font-size: 24px; font-weight: bold; color: #ff9900;">🎬 Select a Movie </p>',
    unsafe_allow_html=True
)
st.markdown(
    f'<p style="font-size: 16px; font-style: italic;">Recommendations like : {selected_movie}</p>',unsafe_allow_html=True
)
if st.button('recommend'):
    movie_name = recommend(selected_movie)
    for name in movie_name:
        st.markdown(f'<div style="border: 2px solid #ff9900; padding: 10px; border-radius: 5px; margin:2px;">{name}</div>', unsafe_allow_html=True)


