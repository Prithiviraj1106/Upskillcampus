import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / "data" / "movies.csv")
df["content"] = df["genres"].fillna("") + " " + df["description"].fillna("")

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["content"])
similarity_matrix = cosine_similarity(tfidf_matrix)

def recommend(movie_title, n=5):
    matches = df.index[df["title"].str.lower() == movie_title.lower()]
    if len(matches) == 0:
        return pd.DataFrame(columns=["title", "genres", "similarity"])
    idx = matches[0]
    ranked = sorted(enumerate(similarity_matrix[idx]), key=lambda x:x[1], reverse=True)
    return pd.DataFrame([
        {"title":df.iloc[i]["title"], "genres":df.iloc[i]["genres"], "similarity":round(float(score),3)}
        for i,score in ranked[1:n+1]
    ])

if __name__ == "__main__":
    title=input("Enter a movie title: ")
    result=recommend(title)
    print(result.to_string(index=False) if not result.empty else "Movie not found.")
