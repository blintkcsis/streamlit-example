# Import libraries
import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Hunch", page_icon="🐍", layout="wide")
st.title("Hunch")

# Connect to the Google Sheet
sheet_id = "1TyeydBGOvcDrSm_OZZqfgI0Xpc0e2mQMXfZvgH8xsUc"
sheet_name = "slack"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url, dtype=str).fillna("")


# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search for information across apps", value="")

# Filter the dataframe using masks
m1 = df["Author"].str.contains(text_search)
m2 = df["Timestamp"].str.contains(text_search)
m3 = df["Text"].str.contains(text_search)
df_search = df[m1 | m2 | m3]

# Another way to show the filtered results
# Show the cards
N_cards_per_row = 3
if text_search:
    for n_row, row in df_search.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="large")
        # draw the card
        with cols[n_row%N_cards_per_row]:
            st.caption(f"Slack - {row['Timestamp'].strip()}")
            st.markdown(f"*'{row['Text'].strip()}'*")
            st.markdown(f"**{row['Author'].strip()}**")
            


