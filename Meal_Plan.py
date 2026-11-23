
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="South Indian Meal Planner",
    page_icon="🥗",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f7faf7;
}
h1 {
    color: #176b45;
}
h2, h3 {
    color: #28734d;
}
.meal-card {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    border-left: 5px solid #299764;
    margin-bottom: 12px;
}
.stButton>button {
    background-color: #218653;
    color: white;
    border-radius: 8px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🥗 7-Day South Indian Meal Planner")
st.write("Healthy vegetarian meal planning for working professionals")
st.divider()

# Sidebar
st.sidebar.header("⚙️ Meal Preferences")

name = st.sidebar.text_input("Your Name", "Gokul")

goal = st.sidebar.selectbox(
    "Your Fitness Goal",
    ["Weight Loss", "Muscle Building",
     "Fat Loss + Muscle Gain", "Healthy Lifestyle"]
)

diet = st.sidebar.selectbox(
    "Diet Preference",
    ["Pure Vegetarian", "Vegetarian with Eggs"]
)

calories = st.sidebar.selectbox(
    "Daily Calorie Target",
    [1500, 1700, 1800, 2000, 2200, 2500]
)

# Weekly meal data
meal_data = {
    "Monday": [
        "Idli + Sambar + Chutney",
        "Guava",
        "Brown Rice + Sambar + Beans Poriyal + Curd",
        "Sundal + Green Tea",
        "Chapati + Vegetable Kurma"
    ],
    "Tuesday": [
        "Ven Pongal + Sambar",
        "Papaya",
        "Rice + Rasam + Keerai Kootu + Curd",
        "Roasted Peanuts",
        "Vegetable Dosa + Tomato Chutney"
    ],
    "Wednesday": [
        "Ragi Dosa + Sambar",
        "Apple",
        "Rice + Drumstick Sambar + Cabbage Poriyal",
        "Sprouts Sundal",
        "Chapati + Channa Masala"
    ],
    "Thursday": [
        "Oats Idli + Sambar",
        "Orange",
        "Rice + Vatha Kuzhambu + Beans Poriyal + Curd",
        "Buttermilk + Almonds",
        "Adai + Avial"
    ],
    "Friday": [
        "Pesarattu + Chutney",
        "Watermelon",
        "Rice + Keerai Masiyal + Rasam + Curd",
        "Boiled Corn",
        "Vegetable Upma + Sambar"
    ],
    "Saturday": [
        "Idiyappam + Vegetable Kurma",
        "Banana",
        "Rice + Paruppu + Carrot Poriyal + Rasam",
        "Channa Sundal",
        "Ragi Dosa + Sambar"
    ],
    "Sunday": [
        "Masala Dosa + Sambar",
        "Seasonal Fruits",
        "Vegetable Biryani + Onion Raita",
        "Nuts + Buttermilk",
        "Chapati + Mixed Vegetable Kurma"
    ]
}

meal_types = [
    "🌅 Breakfast",
    "🍎 Mid-Morning Snack",
    "🍚 Lunch",
    "☕ Evening Snack",
    "🌙 Dinner"
]

# Egg options
if diet == "Vegetarian with Eggs":
    meal_data["Monday"][0] += " + 2 Boiled Eggs"
    meal_data["Wednesday"][0] += " + 2 Boiled Eggs"
    meal_data["Friday"][3] += " + 2 Boiled Eggs"
    meal_data["Sunday"][3] += " + 2 Boiled Eggs"

# Main dashboard
st.subheader(f"Welcome, {name}! 👋")

col1, col2, col3 = st.columns(3)

col1.metric("Duration", "7 Days")
col2.metric("Daily Calories", f"{calories} kcal")
col3.metric("Goal", goal)

st.divider()

# Day selector
selected_day = st.selectbox(
    "📅 Select Your Day",
    list(meal_data.keys())
)

st.subheader(f"🍽️ {selected_day} Meal Schedule")

for meal, food in zip(meal_types, meal_data[selected_day]):
    st.markdown(
        f"""
        <div class="meal-card">
            <h4>{meal}</h4>
            <p>{food}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Full weekly planner
st.divider()
st.subheader("📋 Complete Weekly Meal Plan")

rows = []

for day, foods in meal_data.items():
    for meal, food in zip(meal_types, foods):
        rows.append({
            "Day": day,
            "Meal": meal,
            "Menu": food
        })

df = pd.DataFrame(rows)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# Download button
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Weekly Meal Plan",
    data=csv,
    file_name="south_indian_7_day_meal_plan.csv",
    mime="text/csv"
)

# Shopping list
st.divider()
st.subheader("🛒 Weekly Grocery Shopping List")

shopping_list = [
    "Rice",
    "Idli Rice",
    "Ragi Flour",
    "Wheat Flour",
    "Oats",
    "Toor Dal",
    "Channa",
    "Green Gram",
    "Black Chickpeas",
    "Carrot",
    "Beans",
    "Cabbage",
    "Spinach",
    "Drumstick",
    "Tomato",
    "Onion",
    "Cucumber",
    "Banana",
    "Apple",
    "Guava",
    "Papaya",
    "Curd",
    "Milk",
    "Almonds",
    "Peanuts"
]

for item in shopping_list:
    st.checkbox(item, key=f"grocery_{item}")

st.divider()

st.success("Your 7-Day South Indian Vegetarian Meal Planner is ready! 🥗")

st.caption("Eat healthy | Stay consistent | Build a stronger body")
