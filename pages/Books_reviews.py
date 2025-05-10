import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide") #Configurando para que a configuração d tela cheia persista

#Importando as tabelas com reviews e livros coletada do kaggle
df_reviews = pd.read_csv(r'customer reviews.csv')
df_top100_books = pd.read_csv(r'Top-100 Trending Books.csv')

#Configurando o select box com os livros
books = df_top100_books['book title'].unique()
books = st.sidebar.selectbox('Books', books)
df_book = df_top100_books[df_top100_books['book title'] == books]
df_reviews_f = df_reviews[df_reviews['book name']==books]
#Criando variáveis para organizar a pagina
book_title = df_book['book title'].iloc[0]
book_genre = df_book[ 'genre'].iloc[0]
book_price = f"${df_book[ 'book price'].iloc[0]}"
book_rating = df_book[ 'rating'].iloc[0]
book_year = df_book[ 'year of publication'].iloc[0]
#Configurando Layout da pagina
st.title(book_title)
st.subheader(book_genre)
col1, col2, col3 = st.columns(3)
col1.metric('price', book_price)
col2.metric('Rating', book_rating)
col3.metric('Year of Publication', book_year)
#Configurando os reviews
st.divider()
for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])