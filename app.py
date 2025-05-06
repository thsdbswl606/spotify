from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

app = Flask(__name__)

#Load and preprocess data
spotify_data = pd.read_csv("spotifydata.csv")
X = spotify_data.select_dtypes(include=[np.number])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=0.95)
X_pca = pca.fit_transform(X_scaled)

#Fit KMeans
optimal_k = 6
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_pca)
spotify_data["Cluster"] = clusters

#Recommendation function
def recommend_songs(song_name, num_recommendations=5):
    if song_name not in spotify_data["name"].values:
        return ["Song not found in dataset."]
    
    song_cluster = spotify_data.loc[spotify_data["name"] == song_name, "Cluster"].values[0]
    similar_songs = spotify_data[(spotify_data["Cluster"] == song_cluster) & (spotify_data["name"] != song_name)]

    if similar_songs.empty:
        return ["No similar songs found."]
    
    recommendations = similar_songs.sample(n=min(num_recommendations, len(similar_songs)), random_state=42)
    return [f"{row['name']} — {row['artists']}" for _, row in recommendations.iterrows()]

#Flask routes
@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        song = request.form['song']
        recommendations = recommend_songs(song)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
