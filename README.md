# 🎬 Movie Recommendation by Similarity

Beginner content-based movie recommendation system.

## How it works
Dataset → combine genres + description → TF-IDF → cosine similarity → rank movies → top recommendations.

## Run
```bash
pip install -r requirements.txt
python recommender.py
streamlit run app.py
```

## Files
- `data/movies.csv` — starter dataset
- `recommender.py` — recommendation engine
- `app.py` — Streamlit interface
- `PROJECT_REPORT.txt` — project report

The dataset is intentionally small for learning.
