import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Sukkur Mint Candy",
    page_icon="🍬",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
.main-title{
    font-size:50px;
    font-weight:bold;
    color:#0f9d58;
    text-align:center;
}

.subtitle{
    text-align:center;
    font-size:22px;
}

.product-card{
    padding:15px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-title">🍬 Sukkur Mint Candy</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Fresh Handmade Mint Candy from Sukkur, Sindh</p>', unsafe_allow_html=True)

st.write("")

# Hero image
st.image("https://images.unsplash.com/photo-1606312619344-2c63b5a1e7c5", use_column_width=True)

# About
st.header("About Our Candy 🌿")

st.write("""
Sukkur Mint Candy is famous for its **refreshing mint taste** and traditional recipe.  
We produce **high quality handmade candies** loved across Sindh.
""")

# Products
st.header("Our Products 🍬")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1621939514649-280e2ee25f60")
    st.subheader("Classic Mint Candy")
    st.write("Price: Rs 450")
    st.button("Buy Classic")

with col2:
    st.image("https://images.unsplash.com/photo-1582058091505-f87a2e55a40f")
    st.subheader("Extra Strong Mint")
    st.write("Price: Rs 500")
    st.button("Buy Strong Mint")

with col3:
    st.image("https://images.unsplash.com/photo-1625944525903-c6e1d8c9c1d7")
    st.subheader("Mint Mix Pack")
    st.write("Price: Rs 600")
    st.button("Buy Mix Pack")

# Order section
st.header("Order Your Candy 🛒")

name = st.text_input("Your Name")
phone = st.text_input("Phone Number")

product = st.selectbox(
    "Select Product",
    ["Classic Mint Candy", "Extra Strong Mint", "Mint Mix Pack"]
)

quantity = st.slider("Quantity", 1, 10)

total = quantity * 200
st.write(f"Estimated Total: Rs {total}")

if st.button("Confirm Order"):
    st.success("Order placed successfully! Continue to payment below.")

# Payment section
st.header("Payment Options 💳")

st.markdown("""
### Pay with JazzCash
Send payment to: **3364620555**

### Pay with Easypaisa
Send payment to: **03364620555**
""")

st.info("After payment send screenshot on WhatsApp: 0300-1234567")

# Contact
st.header("Contact Us 📍")

st.write("""
Location: Sukkur, Sindh  
Phone: +92 3364620555 
Email: sukkurmintcandy@gmail.com
""")

st.markdown("---")

st.markdown('<p class="footer">© 2026 Sukkur Mint Candy</p>', unsafe_allow_html=True)

