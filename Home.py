import streamlit as st
import os
import openai
from streamlit.components.v1 import html as st_html

openai.api_key = os.getenv("API_KEY")

st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 575px;
            }}
        </style>
    ''',
    unsafe_allow_html=True
)




def generate_text(input, source):
    input = "Modify this HTML code accoding to these guidelines : " + str(input) + ": Html code  :"+ str(source)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input,
        temperature=0.56,
        max_tokens=2100,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0
    )
    return response.choices[0].text



if 'source' not in st.session_state:
    st.session_state['source'] = """<!DOCTYPE html>
<html>
<head>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<style>
body,h1 {font-family: "Raleway", sans-serif}
body, html {height: 100%}
.bgimg {
  background-color: yellow;
  min-height: 100%;
  background-position: center;
  background-size: cover;
}
</style>
</head>
<body>

<div class="bgimg w3-display-container w3-animate-opacity w3-text-white">
  <div class="w3-display-topleft w3-padding-large w3-xlarge">
    Logo
  </div>
  <div class="w3-display-middle">
    <h1 class="w3-jumbo w3-animate-top">COMING SOON</h1>
    <hr class="w3-border-grey" style="margin:auto;width:40%">
    <p class="w3-large w3-center">35 days left</p>
  </div>

</div>

</body>
</html>
"""

st_html(st.session_state['source'], width=1400, height=400)


query = st.sidebar.text_area("Ask Something", key="query")
submit = st.sidebar.button("Submit")

if submit:
    st.session_state['source'] = generate_text(query, st.session_state['source'])
    st.sidebar.code(st.session_state['source'])


