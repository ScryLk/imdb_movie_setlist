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





st.write("Têndencia de Votos p/categoria")

st.write()

categories_index = df[df["Genre"]].index
votes = df[df["No_of_votes"]]

st.bar_chart(categories_index, votes)







