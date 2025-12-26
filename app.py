import streamlit as st
from recommender import recommend

st.title("🍽️ Smart Restaurant Recommender")

city = st.selectbox(
    "Select City",
    ["Bangalore", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Pune"]
)
cuisine = st.selectbox("What do you want to eat?", ["Indian", "Italian", "Chinese", "Fast Food"])
price = st.slider("Max Budget (₹)", 100, 500, 300)

if st.button("Recommend"):
    results = recommend(city, cuisine, price)

    if results:
        st.subheader("Top Recommendations:")
        for name, score in results:
            st.write(f"⭐ **{name}** — Score: {score}")
    else:
        st.warning("No restaurants found matching your preferences.")
