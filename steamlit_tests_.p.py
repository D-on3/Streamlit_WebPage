import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

#functions resposible for the animation
#If we are using it localy
def load_lottie(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)

#if we are using it from url
def load_lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# FIND MORE EMOJIS HERE:https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = "This is my page",page_icon= ':snake:',layout='wide')

#------HEADER SECTION ------
st.subheader ('Hi, I am Test Page :snake:')
st.title('This is the strange process of build up')
with st.container():
    st.write("")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write('Im page a purpose')
        st.write('I have no binary function i just exist to annoy')

    with right_column:
        animation = load_lottie_url('https://assets10.lottiefiles.com/private_files/lf30_fYLO8U.json')
        st_lottie(animation, key='1')

#------WHAT I DO-----

with st.container():
    st.write("")
    left_column ,right_column = st.columns(2)
    with left_column:
        st.header("What i do")
        st.write('##')
        st.write('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pharetra ultricies mattis. \
        Suspendisse pellentesque risus in elit pretium, eu euismod ex lobortis. Nulla sollicitudin quis est vel tempus.\
        Nunc feugiat urna ac placerat eleifend. Cras pharetra, justo eu commodo rhoncus, turpis ex porta risus, quis \
        tincidunt eros justo vel elit. Nunc in libero dolor. Fusce vel mattis orci, sed porta dolor. Suspendisse elit \
        ipsum, pellentesque lacinia lectus pretium, lacinia ullamcorper lorem. Etiam ut sollicitudin lorem. Vivamus et \
        malesuada lacus.
        Phasellus semper orci consectetur urna laoreet pulvinar. Pellentesque imperdiet lectus eget rutrum elementum. \
        Nulla viverra tellus ut purus pretium tempus vel eu sem. Mauris commodo sollicitudin magna, nec convallis nulla \
        commodo eget. Pellentesque accumsan egestas nunc, non maximus nisi viverra pulvinar. Pellentesque habitant morbi\
        tristique senectus et netus et malesuada fames ac turpis egestas. Ut ac turpis quam.''')
        #visualisation of the animation
    with right_column:
        # Calling the function responsible for the animation
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')

        st.write('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pharetra ultricies mattis. \
        Suspendisse pellentesque risus in elit pretium, eu euismod ex lobortis. Nulla sollicitudin quis est vel tempus.\
        Nunc feugiat urna ac placerat eleifend. Cras pharetra, justo eu commodo rhoncus, turpis ex porta risus, quis \
        tincidunt eros justo vel elit. Nunc in libero dolor. Fusce vel mattis orci, sed porta dolor. Suspendisse elit \
        ipsum, pellentesque lacinia lectus pretium, lacinia ullamcorper lorem. Etiam ut sollicitudin lorem. Vivamus et \
        malesuada lacus.
        Phasellus semper orci consectetur urna laoreet pulvinar. Pellentesque imperdiet lectus eget rutrum elementum. \
        Nulla viverra tellus ut purus pretium tempus vel eu sem. Mauris commodo sollicitudin magna, nec convallis nulla \
        commodo eget. Pellentesque accumsan egestas nunc, non maximus nisi viverra pulvinar. Pellentesque habitant morbi\
        tristique senectus et netus et malesuada fames ac turpis egestas. Ut ac turpis quam.''')



# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    #todo: Email must be checked and confirmed after this the email string should be substitute

    contact_form = """
    <form action="https://formsubmit.co/330659a1fbcf955e6728859239fc1888" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <br><input type="email" name="email" placeholder="Your email" required>
        <br><textarea name="message" placeholder="Your message here" required with = "400" height = "400"></textarea>
        <br><button type="submit">Send</button>
    </form>
    """
    
#---Contact form---init

st.markdown(contact_form, unsafe_allow_html=True)

with st.container():
   
    other_links = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="CSS3 Hexagon Buttons" >
	<meta name="author" content="Shariar">
	<title>CSS3 Hexagon Buttons</title>
	<link rel="stylesheet" type="text/css" href="assets/css/bootstrap.min.css"> 
	<link rel="stylesheet" type="text/css" href="assets/css/page-style.css">
	<link rel="stylesheet" type="text/css" href="assets/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="assets/css/hexagons.min.css"> 
</head>
<body>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-twitter"></i></span></a> 
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-google-plus"></i></span></a>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-youtube"></i></span></a>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-linkedin-square"></i></span></a>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-tumblr-square"></i></span></a>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-rss-square"></i></span></a>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-pinterest-square"></i></span></a> 
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-vimeo-square"></i></span></a>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-github-alt"></i></span></a>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-flickr"></i></span></a>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-dropbox"></i></span></a>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-xing"></i></span></a>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-dribbble"></i></span></a>
		<a href="#"><span class="hb hb-sm spin"><i class="fa fa-tencent-weibo"></i></span></a>
		
	<script src="assets/js/jquery-2.1.0.min.js"></script>
	<script src="assets/js/hexagons.min.js"></script>
</body>
</html>
'''

components.html(other_links)
#st.markdown(other_links)
    # st.write('[GitHub>>](https://github.com/D-on3)')