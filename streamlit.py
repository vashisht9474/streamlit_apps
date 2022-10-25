import streamlit as st

st.set_page_config(layout="wide")
video_html = """
		<style>

		#myVideo {
		  position: fixed;
		  right: 0;
		  bottom: 0;
		  min-width: 100%; 
		  min-height: 100%;
		}

		.content {
		  position: fixed;
		  bottom: 0;
		  background: rgba(0, 0, 0, 0.5);
		  color: #f1f1f1;
		  width: 100%;
		  padding: 20px;
		}

		</style>	
		<video autoplay muted loop id="myVideo">
		  <source src="https://static.videezy.com/system/resources/previews/000/005/747/original/hand_signs.mp4")>
		  Your browser does not support HTML5 video.
		</video>
        """
st.markdown(video_html, unsafe_allow_html=True)




def check_password():
	
    
    

    def password_entered():
	
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
            
        )
        st.error("😕 User not known or password incorrect")
        
        return False
    else:
        # Password correct.
        return True

if check_password():
	st.write("hello")
	video_html1 = """
		<style>

		#myVideo {
		  position: fixed;
		  right: 0;
		  bottom: 0;
		  min-width: 100%; 
		  min-height: 100%;
		}

		.content {
		  position: fixed;
		  bottom: 0;
		  background: rgba(0, 0, 0, 0.5);
		  color: #f1f1f1;
		  width: 100%;
		  padding: 20px;
		}

		</style>	
		<video autoplay muted loop id="myVideo">
		  <source src="https://static.videezy.com/system/resources/previews/000/047/870/original/Text_01a_2.mp4")>
		  Your browser does not support HTML5 video.
		</video>
        """
st.markdown(video_html1, unsafe_allow_html=True)
import streamlit as st

def deaf_to_deaf():
    st.markdown("# deaf to deaf 🎈")
    st.sidebar.markdown("# deaf to deaf 🎈")

def deaf_to_dumb():
    st.markdown("# deaf to dumb ❄️")
    st.sidebar.markdown("# deaf to dumb ❄️")

def dataset():
    st.markdown("# sign language dataset 🎉")
    st.sidebar.markdown("# dataset 🎉")

page_names_to_funcs = {
    "deaf_to_deaf": deaf_to_deaf,
    "deaf_to_dumb": deaf_to_dumb,
    "dataset": dataset,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
    

    

  
