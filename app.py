import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="For My Sister ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

PHOTO = Path(__file__).parent / "assets" / "photo.jpg"

@st.cache_data
def get_photo_b64():
    return base64.b64encode(PHOTO.read_bytes()).decode()

st.markdown("""
<style>
.stApp {
    background:
      radial-gradient(circle at 15% 8%, rgba(171,78,139,.35), transparent 30%),
      radial-gradient(circle at 90% 85%, rgba(110,53,105,.25), transparent 30%),
      #100a10;
    color:white;
}
.block-container {max-width:650px;padding:35px 20px 55px;}
.hero {text-align:center;font-family:Georgia,serif;margin-bottom:24px;}
.kicker {font:11px Arial,sans-serif;letter-spacing:4px;text-transform:uppercase;opacity:.65;}
h1 {font-size:clamp(34px,9vw,48px);margin:8px 0 20px;}
.photo {width:100%;display:block;border-radius:24px;box-shadow:0 22px 70px rgba(0,0,0,.5);}
.thoughts {margin-top:30px;text-align:center;}
.thought {font:19px/1.85 Georgia,serif;margin:0 0 24px;animation:rise .8s ease both;}
.thought:nth-child(1){animation-delay:.15s}
.thought:nth-child(2){animation-delay:.45s}
.thought:nth-child(3){animation-delay:.75s}
.thought:nth-child(4){animation-delay:1.05s}
.thought:nth-child(5){animation-delay:1.35s}
.thought:nth-child(6){animation-delay:1.65s}
@keyframes rise {from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
.divider {width:55px;height:1px;background:rgba(255,255,255,.35);margin:32px auto;}
.final {text-align:center;font:italic 21px/1.65 Georgia,serif;margin-top:36px;}
.heart {text-align:center;font-size:30px;margin-top:12px;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<div class="kicker">A little something for you</div>
<h1>For My Sister ❤️</h1>
</div>
""", unsafe_allow_html=True)

photo_b64 = get_photo_b64()
st.markdown(
    f'<img class="photo" src="data:image/jpeg;base64,{photo_b64}" alt="Brother and sister">',
    unsafe_allow_html=True
)

st.markdown("""
<div class="thoughts">
<p class="thought">Bachpan mein kitni baar lade hain,<br>kitni baar ek dusre ko irritate kiya hai...</p>
<p class="thought">Par shayad yehi toh bhai-behen ka rishta hai. ❤️</p>
<p class="thought">Waqt badlega, hum apni-apni zindagi mein busy ho jayenge,</p>
<p class="thought">lekin ek baat kabhi nahi badlegi —<br>main hamesha tere saath rahunga.</p>
<p class="thought">Tujhe har baar bol nahi pata,<br>par tu mere liye bahut important hai.</p>
<p class="thought"><b>Bas aise hi rehna... meri behan. ❤️</b></p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="final">
Kuch rishte explain nahi kiye jaate...<br>
bas feel kiye jaate hain.<br><br>
<b>Lucky hoon ki tu meri behan hai.</b>
</div>
<div class="heart">❤️</div>
""", unsafe_allow_html=True)
