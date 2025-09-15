"""
The main app file sets up a Streamlit UI with tabs for two example tasks.
Each tab calls a function from streamlit_handler to display its content.
"""
import streamlit as st
from aiweb_common.streamlit.page_renderer import StreamlitUIHelper
from Webapp4.streamlit_interface import BaseHandler


from Webapp4_config.config import Webapp4Config



def main():
    """
    Main sets up the web app title, header and tabs.
    """
    st.set_page_config(page_title="Webapp4", page_icon="🏷️")
    st.title("🏷️ Webapp4 🤖")
    st.markdown(Webapp4Config.HEADER_MARKDOWN)
    
    # Create a UI helper instance. (This can be used to wrap Streamlit calls if needed.)
    ui = StreamlitUIHelper()
    bh = BaseHandler(ui)
    # Create two tabs in the app for the example tasks.
    tab1, tab2 = st.tabs(["Example Upload", "Example Download"])
    
    with tab1:
        # Call task A — CSV file upload and preview.
        bh.upload_csv_preview()
        
    with tab2:
        # Call task B — Dummy report generation and download.
        bh.download_dummy_report()

if __name__ == "__main__":
    main()