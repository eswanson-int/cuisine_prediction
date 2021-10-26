import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)

st.title('What cuisine is your recipe')

page = st.sidebar.selectbox(
    'Page',
    ('About', 'EDA', 'Make a Prediction')
)


@st.cache
def load_data():
    df = pd.read_csv('data_labels.csv')
    return df


if page == 'About':
    st.subheader('About this project')
    st.write('''
    This is a Streamlit app that hosts my cuisine decider model.

    The best model I found was gradientBoost
    ''')

elif page == 'EDA':
    df = load_data()
    st.table(df.sample(5))

elif page == 'Make a Prediction':

    with open('models/cuisine_pipe.pkl', 'rb') as pickle_in:
        pipe = pickle.load(pickle_in)

    your_text = st.text_input('Please enter some ingredients:', max_chars=500)

    #predicted_author = pipe.predict([your_text])[0]

    #st.write(f'You write like {predicted_author.title()}.')
    predicted_cuisine_num = pipe.predict([your_text])[0]

    code = {'brazilian': 0,
            'british': 1,
            'cajun_creole': 2,
            'chinese': 3,
            'filipino': 4,
            'french': 5,
            'greek': 6,
            'indian': 7,
            'irish': 8,
            'italian': 9,
            'jamaican': 10,
            'japanese': 11,
            'korean': 12,
            'mexican': 13,
            'moroccan': 14,
            'russian': 15,
            'southern_us': 16,
            'spanish': 17,
            'thai': 18,
            'vietnamese': 19}
    predicted_cuisine_name = list(code.keys())[list(code.values()).index(predicted_cuisine_num)]

    st.write(f'You recipe is probably a {predicted_cuisine_name.title()} cuisine.')