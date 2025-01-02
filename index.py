import streamlit as st
import pandas as pd
import datetime
import numpy as np

st.set_page_config(
	layout="wide",
	page_title="IMDB Movies",
	page_icon="🦈",
	initial_sidebar_state="auto",
)
df = pd.read_csv("IMDB-Dataset.csv")
d = st.date_input("Selecione a data")
#st.write("Variavel:", type(d.year))
year_choose = df[df["Released_Year"] == d.year]
year_choose
print(type(d))
# date_selected = df[df["Released_Year"] >= d.year]

gender_movies = df["Genre"]

gender = st.selectbox(
    "Escolha o gênero do filme",
    (gender_movies),
)

gender_choose = df[df["Genre"] == gender]

gender_choose

st.write("You selected:", gender)
gender

classification = st.slider("Select a range of values", 0.0, 10.0)

final_classification = df[df["IMDB_Rating"] >= classification]
final_classification


#Grafico votos por genero
votes_by_genre = df.groupby("Genre")["No_of_Votes"].sum().reset_index()

# Configurar os eixos para o gráfico de barras
genres = votes_by_genre["Genre"]  # Gêneros
votes = votes_by_genre["No_of_Votes"]  # Número de votos

# Criar o gráfico de barras no Streamlit
st.bar_chart(data=votes_by_genre, x="Genre", y="No_of_Votes")

#Gráfico classificação por genero 
rating_by_genre = df.groupby("Genre")["IMDB_Rating"].sum().reset_index()

ratings = rating_by_genre["IMDB_Rating"]

st.bar_chart(data=rating_by_genre, x="Genre", y="IMDB_Rating")

#Grafico filme por ano

titles_by_movie = df.groupby("Released_Year")["Series_Title"].count().reset_index()

titles = titles_by_movie["Series_Title"]
movie_year = titles_by_movie["Released_Year"]

titles_by_movie.columns = ["Released_Year", "Series_Title"]


st.bar_chart(data=titles_by_movie, x="Released_Year", y="Series_Title")


title = st.text_input("Movie title")
st.write("The current movie title is", title)

contains = df[df["Series_Title"].str.contains(title, case=False, na=False)]

contains











