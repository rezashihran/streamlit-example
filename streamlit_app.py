import streamlit as st
import pandas as pd

# Here's your DataFrame
df_t = pd.read_csv('column_items.csv')
rules = pd.read_csv('rules_items.csv')

column_names = df_t.columns.tolist()

# Add a title
st.title('Top 10 Highest Support')

# Replace the antecedents and consequents columns with text inside single quotes
rules['antecedents'] = rules['antecedents'].apply(lambda x: x.replace("{", "").replace("}", "").replace("'", "").strip())
rules['consequents'] = rules['consequents'].apply(lambda x: x.replace("{", "").replace("}", "").replace("'", "").strip())

# Add a multiselect box for the user to select 'pilih barang' from df_t
selected_items = st.multiselect(
    'Select Columns',
    column_names)

# If no items are selected, show top 10 highest support for all data.
# If any item is selected, filter data based on user selection and show top 10 highest support for selected items.
if not selected_items:
    st.subheader('Top 10 for all data')
    rules.sort_values('support', ascending=False, inplace=True)
    st.dataframe(rules[:10])
else:
    st.subheader(f'Top 10 for selected items')
    # Filter rules where any of the selected_items appear in the antecedents
    filtered_rules = rules[rules['antecedents'].apply(lambda x: any(item in selected_items for item in x))]
    filtered_rules.sort_values('support', ascending=False, inplace=True)
    st.dataframe(filtered_rules[:10])
