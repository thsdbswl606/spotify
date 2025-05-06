# 🎧 Spotify Song Recommendation System

This project is a music recommender system built using a large Spotify dataset from Kaggle (220,000+ songs from 1920–2020). It uses unsupervised learning techniques (KMeans clustering, PCA) to recommend songs similar to user input, and includes a Flask-based web app for interactive use.

## 📁 Dataset

- Source: Kaggle
- 220k+ songs
- Key features: `danceability`, `energy`, `valence`, `popularity`, etc.
- Note: Due to file size, the dataset is not included here. Please download from [[Kaggle link]([url](https://www.kaggle.com/datasets/vatsalmavani/spotify-dataset)
- )].

## 🧠 Machine Learning

- **Model**: KMeans clustering
- **Dimensionality Reduction**: PCA
- **Similarity**: Euclidean distance within clusters

## 🌐 Web App

- Built with Flask
- Users can type in a song name and receive similar song recommendations
- Optional version: Spotify OAuth to fetch real playlists (work-in-progress)

## 🚀 How to Run

1. Clone the repo
2. Install requirements: `pip install -r requirements.txt`
3. Run the app: `python app/app.py`
4. Open in browser: `http://127.0.0.1:5000/`

## 🧪 Demo

(Add screenshots or a GIF of your web interface)

## ✅ Future Work

- Improve model performance using deep learning (e.g. Autoencoders)
- Better UI/UX
- Complete Spotify OAuth version

## 🧑‍💻 Author

Yunji Sohn

