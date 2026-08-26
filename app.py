import streamlit as st
from recommender import df, recommend

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬")
st.title("🎬 Movie Recommendation System")
st.write("Get movies similar to a selected movie using TF-IDF and cosine similarity.")

movie = st.selectbox("Select a movie", df["title"].tolist())
n = st.slider("Number of recommendations", 1, 10, 5)

if st.button("🍿 Recommend Movies", use_container_width=True):
    result = recommend(movie, n)
    st.subheader(f"Movies similar to: {movie}")
    for _, row in result.iterrows():
        st.markdown(f"### 🎬 {row['title']}")
        st.write(f"Genres: {row['genres']}")
        st.write(f"Similarity score: {row['similarity']:.3f}")
        st.divider()

st.caption("Educational project • TF-IDF + Cosine Similarity")
