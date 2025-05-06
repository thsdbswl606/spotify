# 🎧 Spotify Song Recommendation System

This project is a music recommender system built using a large Spotify dataset from Kaggle (220,000+ songs from 1920–2020). It uses unsupervised learning techniques (KMeans clustering, PCA) to recommend songs similar to user input, and includes a Flask-based web app for interactive use.

## 📁 Dataset

- Source: Kaggle
- 220k+ songs
- Key features: `danceability`, `energy`, `valence`, `popularity`, etc.
- Note: Due to file size, the dataset is not included here. Please download from [([Kaggle link](https://www.kaggle.com/datasets/vatsalmavani/spotify-dataset))]. 

## 🧠 Machine Learning

- **Model**: KMeans clustering
- **Dimensionality Reduction**: PCA
- **Similarity**: Euclidean distance within clusters

## 🌐 Web App

- Built with Flask
- Users can type in a song name and receive similar song recommendations
- Optional version: Spotify OAuth to fetch real playlists by allowing users to log in using their real account (work-in-progress)

## 🚀 How to Run

1. Clone the repo
2. Install requirements: `pip install -r requirements.txt`
3. Run the app: `python app/app.py`
4. Open in browser: `http://127.0.0.1:5000`

## 🧪 Demo

1. Open the website via link
<img width="357" alt="Screen Shot 2025-05-06 at 9 39 41 AM" src="https://github.com/user-attachments/assets/602f2f72-9315-45c3-badc-18dc77878ed3" />

2. Type in the desired song 
<img width="368" alt="Screen Shot 2025-05-06 at 9 39 29 AM" src="https://github.com/user-attachments/assets/8259f78a-db0f-4613-9b13-29070a54ec19" />

3. Get your recommendations!
<img width="618" alt="Screen Shot 2025-05-06 at 9 39 05 AM" src="https://github.com/user-attachments/assets/687b8e04-9efd-474b-aa9e-c17c44ccc339" />

## ✅ Future Work

- Improve model performance using deep learning (e.g. Autoencoders)
- Better UI/UX
- Complete Spotify OAuth version
- Work on limitations of this system; now the recommendation is only based on songs within the data file.
- E.g.)
If song is not found in the dataset, it shows: 
<img width="363" alt="Screen Shot 2025-05-06 at 9 41 57 AM" src="https://github.com/user-attachments/assets/d0a6912e-8260-48a2-bf99-eca61bd57dcf" />


## 🧑‍💻 Author

Yunji Sohn

