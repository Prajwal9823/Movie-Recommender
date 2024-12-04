import pickle
import streamlit as st
import requests

# def fetch_poster(movie_id):
#     api_key = '05e90f50a4c102972b6782fecbd8389f'  # Replace with your TMDB API key
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
#     response = requests.get(url)
#     data = response.json()
#     poster_path = data['poster_path']
#     full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
#     return full_path

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{movie_id}/external_ids"
#
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMTJkOTUxYzNmYmJmZTIwMGZlZWNhNWJmMmUwMjQ1YiIsIm5iZiI6MTczMzE2ODY2OS45OTcsInN1YiI6IjY3NGUwZTFkYWY2YjNlMDE4MmExYzJhOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.yNBC9c8iAIh1u5B6xuRrsK9q_A8MVPOcL8doYTicbQs"
#     }
#
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     poster_path = data['poster_path']
#     full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
#     return full_path

def fetch_poster(movie_id):
    # Use an f-string to format the URL properly
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNWU5MGY1MGE0YzEwMjk3MmI2NzgyZmVjYmQ4Mzg5ZiIsIm5iZiI6MTczMzE2ODY2OS45OTcsInN1YiI6IjY3NGUwZTFkYWY2YjNlMDE4MmExYzJhOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.qljFeA3s4rKeYyIP8RrNjYXCJp5IPJQFgnDXLI2uWWc"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # Check if the 'poster_path' key exists in the response
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
        return full_path
    else:
        return "Poster not found"



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




