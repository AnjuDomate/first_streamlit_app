import streamlit
streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breatfast Menu')
streamlit.text('🥣 Omega3 & blueberry oatmeal')
streamlit.text('🥗 kale, spinch & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free Range Egg')
streamlit.text('🥑🍞 Avocado and Bread')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
