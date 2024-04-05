import streamlit as st
import requests
import os
from dotenv import find_dotenv, load_dotenv


load_dotenv()

# TMDb API key
API_KEY = os.environ.get("API_KEY")

def search_movies(query):
    url = f'https://api.themoviedb.org/3/search/movie'
    params = {'api_key': API_KEY, 'query': query}
    response = requests.get(url, params=params)
    data = response.json()
    return data['results']

def main():
    st.title('Movie Recommender with TMDB API')

    categories = st.multiselect('Select movie categories:', ['Action', 'Comedy', 'Drama', 'Thriller', 'Romance'])

    if st.button('Get Recommendations'):
        st.write("Here are some movie recommendations:")
        for category in categories:
            st.subheader(f'{category} Movies:')
            movies = search_movies(category)
            if movies:
                for movie in movies:
                    st.write(f"Title: {movie['title']}")
                    st.write(f"Release Date: {movie['release_date']}")
                    st.write(f"Overview: {movie['overview']}")
                    st.write(f"Average Rating: {movie['vote_average']}")
                    st.write(f"Vote Count: {movie['vote_count']}")
                    st.image(f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}", caption="Poster", use_column_width=True)
                    st.write('---')
            else:
                st.write(f"No recommendations found for {category} movies.")

if __name__ == "__main__":
    main()
