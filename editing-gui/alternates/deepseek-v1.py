import streamlit as st
import pandas as pd
import os
from fuzzywuzzy import process

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
    try:
        data.to_csv(path, index=False)
        st.success("Changes saved successfully!")
    except Exception as e:
        st.error(f"Error saving data: {e}")

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
        search_term = st.text_input("Search for a company")
        if search_term:
            matches = process.extract(search_term, df['company_name'], limit=1)
            if matches and matches[0][1] > 80:
                selected_company = matches[0][0]
            else:
                selected_company = "All"
        else:
            selected_company = "All"

    # Filtered data table
    if selected_company == "All":
        filtered_df = df
    else:
        filtered_df = df[df['company_name'] == selected_company]

    # Main content area with tabs
    tab1, tab2 = st.tabs(["Edit", "Add New Company"])

    # Tab 1: Edit Company Data
    with tab1:
        st.subheader("Company Data")

        # Get the list of unique company names
        company_names = df['company_name'].unique()
        company_names = sorted(company_names)

        # Initialize session state with the current index
        if 'current_index' not in st.session_state:
            st.session_state.current_index = 0

        # Get the current company based on the current index
        current_company = company_names[st.session_state.current_index]

        # Create next and previous buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.session_state.current_index > 0:
                if st.button("Previous"):
                    st.session_state.current_index -= 1
        with col2:
            st.write(f"Company {st.session_state.current_index + 1} of {len(company_names)}")
        with col3:
            if st.session_state.current_index < len(company_names) - 1:
                if st.button("Next"):
                    st.session_state.current_index += 1

        # Get the row index to edit based on the current company
        row_index_to_edit = df.loc[df['company_name'] == current_company].index[0]

        # Create a form for editing the company data
        with st.form(f"edit_form_{row_index_to_edit}"):
            edited_row = {}

            # Company Information
            st.expander("Company Information", expanded=True)
            col1, col2 = st.columns(2)
            with col1:
                edited_row['company_name'] = st.text_input("Company Name", value=str(df.at[row_index_to_edit, 'company_name']))
            with col2:
                edited_row['stock_ticker'] = st.text_input("Stock Ticker", value=str(df.at[row_index_to_edit, 'stock_ticker']))

            col1, col2 = st.columns(2)
            with col1:
                edited_row['sector'] = st.text_input("Sector", value=str(df.at[row_index_to_edit, 'sector']))
            with col2:
                edited_row['sics_sector'] = st.text_input("SICS Sector", value=str(df.at[row_index_to_edit, 'sics_sector']))

            col1, col2 = st.columns(2)
            with col1:
                edited_row['headquarters_country'] = st.text_input("Headquarters Country", value=str(df.at[row_index_to_edit, 'headquarters_country']))
            with col2:
                edited_row['iso_3166_code'] = st.text_input("ISO 3166 Code", value=str(df.at[row_index_to_edit, 'iso_3166_code']))

            # EBITDA
            st.expander("EBITDA", expanded=True)
            col1, col2 = st.columns(2)
            with col1:
                edited_row['ebitda_2022'] = st.text_input("EBITDA 2022", value=str(df.at[row_index_to_edit, 'ebitda_2022']))
            with col2:
                edited_row['ebitda_currency'] = st.text_input("EBITDA Currency", value=str(df.at[row_index_to_edit, 'ebitda_currency']))

            col1, col2 = st.columns(2)
            with col1:
                edited_row['ebitda_source'] = st.text_input("EBITDA Source", value=str(df.at[row_index_to_edit, 'ebitda_source']))
            with col2:
                edited_row['ebitda_unit'] = st.text_input("EBITDA Unit", value=str(df.at[row_index_to_edit, 'ebitda_unit']))

            col1, col2 = st.columns(2)
            with col1:
                edited_row['non_usd'] = st.text_input("Non USD", value=str(df.at[row_index_to_edit, 'non_usd']))

            # GHG Emissions
            st.expander("GHG Emissions", expanded=True)
            col1, col2 = st.columns(2)
            with col1:
                edited_row['scope_1_emissions'] = st.text_input("Scope 1 Emissions", value=str(df.at[row_index_to_edit, 'scope_1_emissions']))
            with col2:
                edited_row['scope_2_emissions'] = st.text_input("Scope 2 Emissions", value=str(df.at[row_index_to_edit, 'scope_2_emissions']))

            col1, col2 = st.columns(2)
            with col1:
                edited_row['scope_3_emissions'] = st.text_input("Scope 3 Emissions", value=str(df.at[row_index_to_edit, 'scope_3_emissions']))
            with col2:
                edited_row['emissions_reporting_unit'] = st.text_input("Emissions Reporting Unit", value=str(df.at[row_index_to_edit, 'emissions_reporting_unit']))

            # Additional Information
            st.expander("Additional Information", expanded=True)
            col1, col2 = st.columns(2)
            with col1:
                edited_row['sustainability_report'] = st.text_input("Sustainability Report", value=str(df.at[row_index_to_edit, 'sustainability_report']))
            with col2:
                edited_row['notes'] = st.text_input("Notes", value=str(df.at[row_index_to_edit, 'notes']))

            col1, col2 = st.columns(2)
            with col1:
                edited_row['stock_live'] = st.text_input("Stock Live", value=str(df.at[row_index_to_edit, 'stock_live']))
            with col2:
                edited_row['stock_historic'] = st.text_input("Stock Historic", value=str(df.at[row_index_to_edit, 'stock_historic']))

            col1, col2 = st.columns(2)
            with col1:
                edited_row['llm_derived'] = st.text_input("LLM Derived", value=str(df.at[row_index_to_edit, 'llm_derived']))
            with col2:
                edited_row['human_verified'] = st.text_input("Human Verified", value=str(df.at[row_index_to_edit, 'human_verified']))

            col1, col2 = st.columns(2)
            with col1:
                edited_row['exchange'] = st.text_input("Exchange", value=str(df.at[row_index_to_edit, 'exchange']))

            # Save and delete buttons
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
                st.session_state.current_index -= 1  # Move to the previous company
                st.experimental_rerun()

    # Tab 2: Add New Company
    with tab2:
        st.subheader("Add New Company")
        with st.form("add_form"):
            new_row = {}

            # Company Information
            st.expander("Company Information", expanded=True)
            col1, col2 = st.columns(2)
            with col1:
                new_row['company_name'] = st.text_input("Company Name")
            with col2:
                new_row['stock_ticker'] = st.text_input("Stock Ticker")

            col1, col2 = st.columns(2)
            with col1:
                new_row['sector'] = st.text_input("Sector")
            with col2:
                new_row['sics_sector'] = st.text_input("SICS Sector")

            col1, col2 = st.columns(2)
            with col1:
                new_row['headquarters_country'] = st.text_input("Headquarters Country")
            with col2:
                new_row['iso_3166_code'] = st.text_input("ISO 3166 Code")

            # EBITDA
            st.expander("EBITDA", expanded=True)
            col1, col2 = st.columns(2)
            with col1:
                new_row['ebitda_2022'] = st.text_input("EBITDA 2022")
            with col2:
                new_row['ebitda_currency'] = st.text_input("EBITDA Currency")

            col1, col2 = st.columns(2)
            with col1:
                new_row['ebitda_source'] = st.text_input("EBITDA Source")
            with col2:
                new_row['ebitda_unit'] = st.text_input("EBITDA Unit")

            col1, col2 = st.columns(2)
            with col1:
                new_row['non_usd'] = st.text_input("Non USD")

            # GHG Emissions
            st.expander("GHG Emissions", expanded=True)
            col1, col2 = st.columns(2)
            with col1:
                new_row['scope_1_emissions'] = st.text_input("Scope 1 Emissions")
            with col2:
                new_row['scope_2_emissions'] = st.text_input("Scope 2 Emissions")

            col1, col2 = st.columns(2)
            with col1:
                new_row['scope_3_emissions'] = st.text_input("Scope 3 Emissions")
            with col2:
                new_row['emissions_reporting_unit'] = st.text_input("Emissions Reporting Unit")

            # Additional Information
            st.expander("Additional Information", expanded=True)
            col1, col2 = st.columns(2)
            with col1:
                new_row['sustainability_report'] = st.text_input("Sustainability Report")
            with col2:
                new_row['notes'] = st.text_input("Notes")

            col1, col2 = st.columns(2)
            with col1:
                new_row['stock_live'] = st.text_input("Stock Live")
            with col2:
                new_row['stock_historic'] = st.text_input("Stock Historic")

            col1, col2 = st.columns(2)
            with col1:
                new_row['llm_derived'] = st.text_input("LLM Derived")
            with col2:
                new_row['human_verified'] = st.text_input("Human Verified")

            col1, col2 = st.columns(2)
            with col1:
                new_row['exchange'] = st.text_input("Exchange")

            add_button = st.form_submit_button("Add Company")

            if add_button:
                # Validate numerical fields
                try:
                    float(new_row['ebitda_2022'])
                    float(new_row['scope_1_emissions'])
                    float(new_row['scope_2_emissions'])
                    float(new_row['scope_3_emissions'])
                except ValueError:
                    st.error("Please enter valid numerical values for EBITDA and emissions fields.")
                else:
                    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                    save_data(df, csv_path)
                    st.experimental_rerun()

if __name__ == "__main__":
    main()