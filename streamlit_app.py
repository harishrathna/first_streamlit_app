import streamlit
import snowflake.connector
streamlit.title('My Parents New Healthy Diner')


streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') # the mutli value will was set to the fruit index


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries']) # gives the first value in the column 
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
## streamlit.text(fruityvice_response.json())


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)




