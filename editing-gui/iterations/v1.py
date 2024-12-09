import streamlit as st
import pandas as pd
import os

# Path to the CSV file
csv_path = '/home/daniel/Git/ghg-emissions-data-pipeline/company_data.csv'

# Load the CSV file
@st.cache_data
def load_data(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        st.error("CSV file not found!")
        return pd.DataFrame()

# Save the updated data back to the CSV file
def save_data(data, path):
    data.to_csv(path, index=False)
    st.success("Changes saved successfully!")

# Convert column names to more human-readable equivalents
def humanize_column_names(columns):
    return [col.replace("_", " ").title() for col in columns]

# Main function for the Streamlit app
def main():
    st.set_page_config(layout="wide")
    st.title("GHG Emissions Editor")

    # Load data
    df = load_data(csv_path)

    if df.empty:
        st.warning("No data available to display.")
        return

    # Sidebar for filtering by company name
    with st.sidebar:
        st.header("Filter by Company Name")
        company_names = df['company_name'].unique()
        selected_company = st.selectbox("Select a company", options=["All"] + list(company_names))

    # Filtered data table
    if selected_company == "All":
        filtered_df = df
    else:
        filtered_df = df[df['company_name'] == selected_company]

    # Main content area with tabs
    tab1, tab2 = st.tabs(["Data Table", "Add New Company"])

    # Tab 1: Display Data Table
    with tab1:
        st.subheader("Company Data")
        st.dataframe(filtered_df)

        if selected_company != "All":
            st.subheader(f"Edit/Delete Data for {selected_company}")
            row_index_to_edit = filtered_df.index[0]  # Assuming one row per company

            # Links for EBITDA source and sustainability report
            ebitda_source = df.at[row_index_to_edit, 'ebitda_source'] if 'ebitda_source' in df.columns else None
            sustainability_report = df.at[row_index_to_edit, 'sustainability_report'] if 'sustainability_report' in df.columns else None

            col1, col2 = st.columns(2)
            with col1:
                if ebitda_source:
                    st.markdown(f"[Open EBITDA Source]({ebitda_source})", unsafe_allow_html=True)
            with col2:
                if sustainability_report:
                    st.markdown(f"[Open Sustainability Report]({sustainability_report})", unsafe_allow_html=True)

            # Split column view for editing fields
            col1, col2 = st.columns(2)
            with st.form(f"edit_form_{row_index_to_edit}"):
                edited_row = {}
                for i, col in enumerate(df.columns):
                    human_col_name = col.replace("_", " ").title()
                    if i % 2 == 0:  # Left column
                        with col1:
                            edited_row[col] = st.text_input(human_col_name, value=str(df.at[row_index_to_edit, col]))
                    else:  # Right column
                        with col2:
                            edited_row[col] = st.text_input(human_col_name, value=str(df.at[row_index_to_edit, col]))

                save_button, delete_button = st.columns(2)
                with save_button:
                    save_changes = st.form_submit_button("Save Changes")
                with delete_button:
                    delete_row = st.form_submit_button("Delete Row")

                if save_changes:
                    for col in edited_row:
                        df.at[row_index_to_edit, col] = edited_row[col]
                    save_data(df, csv_path)

                if delete_row:
                    df = df.drop(index=row_index_to_edit).reset_index(drop=True)
                    save_data(df, csv_path)
                    st.experimental_rerun()

    # Tab 2: Add New Company
    with tab2:
        st.subheader("Add New Company")
        with st.form("add_form"):
            new_row = {}
            col1, col2 = st.columns(2)
            for i, col in enumerate(df.columns):
                human_col_name = col.replace("_", " ").title()
                if i % 2 == 0:  # Left column
                    with col1:
                        new_row[col] = st.text_input(human_col_name)
                else:  # Right column
                    with col2:
                        new_row[col] = st.text_input(human_col_name)

            add_button = st.form_submit_button("Add Company")

            if add_button:
                df = df.append(new_row, ignore_index=True)
                save_data(df, csv_path)
                st.experimental_rerun()

if __name__ == "__main__":
    main()