import pandas as pd
import streamlit as st
import pickle


def recommend(movie):
    mindex = movies[movies['title'] == movie].index[0]
    distances = similiarity[mindex]
    mlist = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return mlist


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similiarity = pickle.load(open('similiarity.pkl', 'rb'))
st.title('Movie Recommender')
movie_name = st.selectbox('Chose the movie you liked', movies['title'].values)

if st.button('Recommend'):
    r = recommend(movie_name)
    st.header(movies.iloc[r[0][0]].title)
    im = 'http://image.tmdb.org/t/p/w500' + movies.iloc[r[0][0]].poster_path
    st.image(im)
    st.header(movies.iloc[r[2][0]].title)
    im = 'http://image.tmdb.org/t/p/w500' + movies.iloc[r[1][0]].poster_path
    st.image(im)
    st.header(movies.iloc[r[2][0]].title)
    im = 'http://image.tmdb.org/t/p/w500' + movies.iloc[r[2][0]].poster_path
    st.image(im)
    st.header(movies.iloc[r[3][0]].title)
    im = 'http://image.tmdb.org/t/p/w500' + movies.iloc[r[3][0]].poster_path
    st.image(im)
    st.header(movies.iloc[r[4][0]].title)
    im = 'http://image.tmdb.org/t/p/w500' + movies.iloc[r[4][0]].poster_path
    st.image(im)

    # c1 = st.beta_columns(1)
    # # with c1:
    # #     # st.text(movies.iloc[r[0][0]].title)
    # #     # im='http://image.tmdb.org/t/p/w500'+movies.iloc[r[0][0]].poster_path
    # #     st.image('http://image.tmdb.org/t/p/w500/lD8V3DBban95Mxz4sjuA81Tw771.jpg')
