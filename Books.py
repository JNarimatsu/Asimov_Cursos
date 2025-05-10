#print('Hello, world!')
import streamlit as st #Pacote para visualizar o projeto
import pandas as pd
import  plotly.express as px


st.set_page_config(layout = "wide") #Configurando para que a configuração d tela cheia persista

st.title('Books')
#Importando as tabelas com reviews e livros coletada do kaggle
df_reviews = pd.read_csv(r'customer reviews.csv')
df_top100_books = pd.read_csv(r'Top-100 Trending Books.csv')

#Configuração do filtro de preços utilizando o componente slider do streamlit
price_max = df_top100_books['book price'].max()
price_min = df_top100_books['book price'].min()
max_price = st.sidebar.slider('Price Range', price_min, price_max, price_max)
df_books = df_top100_books[df_top100_books['book price']<= max_price]
df_books

#Colocando Gráficos 
#filtrando livros por ano de publicação
col1, col2 = st.columns(2) #Colocando os gráficos lado a lado 
fig = px.bar(df_books['year of publication'].value_counts()) 
col1.plotly_chart(fig)
#Filtrando por preços
fig_02 = px.histogram(df_books['book price'])
col2.plotly_chart(fig_02)

