import streamlit as st

# Adding title of app
st.title('My first App')

# Adding simple text
st.write('Here is the simple text')

# User input
number = st.slider('Pick a number', 0, 100, 10) # default setting after comma

# print text of number
st.write(f'You selected: {number}')

# adding a button
if st.button('Greetings'):
    st.write('Hi,  hello there')
else: 
    st.write('Goodbye') 

# add radio buttons with options
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary')
)  

# print the text of genre
st.write(f'You selected: {genre}')

# add a drop down list
option = st.selectbox(
    "How would you like to be contacted?",
    ('Email', 'Home phone', 'Mobile phone')
)

# add a drop down list on the left sidebar
option = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ('Email', 'Home phone', 'Mobile phone')
)

# add your whatsapp number
st.sidebar.text_input('Enter your whatsapp number')

# add a file uploader
upload_file = st.sidebar.file_uploader('Choose a CSV file', type="csv")
