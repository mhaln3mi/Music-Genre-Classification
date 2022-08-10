# Music-Genre-Classification
## Overview
Music has been an important part of our lives since time immemorial. Every artist has a signature, making music a subjective art. We have scales/metrics to measure the quality of music. But, is it possible to train a machine learning model to predict the genre and quality of the music?

Currently, many music aggregator applications rely on machine learning to power their recommendation engine, and curate playlists. MachineHack is challenging data scientists and machine learning practitioners to build a highly scalable ML model for a music aggregator app (Company ABC) to accurately predict the genre of songs in the dataset.

## Introduction:

In this repo we will be analyzing and building models for Music Genre Classification dataset from Kaggle and try to build a model that can predict the genre of a given recodr. We got our dataset from [Kaggle](https://www.kaggle.com/datasets/purumalgi/music-genre-classification). 

## About Dataset

Training dataset: 17,996 rows with 17 columns 

Column details: artist name; track name; popularity; ‘danceability’; energy; key; loudness; mode; ‘speechiness’; ‘acousticness’; ‘instrumentalness’; liveness; valence; tempo; duration in milliseconds and time_signature. 

Target Variable: 'Class’ such as Rock, Indie, Alt, Pop, Metal, HipHop, Alt_Music, Blues, Acoustic/Folk, Instrumental, Country, Bollywood, 

Test dataset: 7,713 rows with 16 columns 
### Data dictionary

| Variable      | Description |
| ----------- | ----------- |
| artist name    | Name of the artist.       |
| track name   | Name of the track.       |
| popularity  | The popularity of the track out of 100.        |
| danceability   | Whether the track is danceable or not.        |
| energy   | What is the energy of the track.        |
| key   | The key of the track.         |
| loudness   | What is the loudness of the music.       |
| mode   | The mode of the track.        |
| speechiness   | Speechiness detects the presence of spoken words in a track.      |
| acousticness   | This value describes how acoustic a track is. A score of 1.0 means the track is most likely to be an acoustic one.        |
| instrumentalness   | This value represents the amount of vocals in the track. The closer it is to 1.0, the more instrumental the track is.       |
| liveness   | This value describes the probability that the track was recorded with a live audience.       |
| valence   | A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.      |
| tempo   | The tempo of the track.      |
| duration_in min/ms   | The time of the track.      |
| time_signature   | The Time Signature      |
| class   | Genre Class      |


## Libraries used

- pandas
- numpy
- matplotlib
- seaborn
- scipy
- sklrean
- pprint
- autosklearn
- inspect
- PipelineProfiler


## Collaborators

- [Maan Al Neami](https://github.com/mhaln3mi)
- [Nourah Almutairi](https://github.com/xnuray98s)
- [Lina Alhuri](https://github.com/alhuri)
- [Asma AlQahtani](https://github.com/somahq)
- [Yousef Alotaibi](https://github.com/YousefAlotaibi)

## Sources

- https://www.kaggle.com/datasets/purumalgi/music-genre-classification
- https://automl.github.io/auto-sklearn/master/
- https://towardsdatascience.com/introduction-to-data-preprocessing-in-machine-learning-a9fa83a5dc9d
