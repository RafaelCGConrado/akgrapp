import config
import util 
from tab_concept_load import concept_load_tab
from tab_semantics import semantics_tab
from tab_data_load import data_load_tab
from tab_eda import eda_tab
import pandas as pd
import streamlit as st

def launch_dashboard():
    tab_concept_load, tab_semantics, tab_data_load, tab_eda = st.tabs(["Carregar Conceitos", "Definir Semânticas",
                                                                       "Carregar Dados", "GraFOCAL"])

    with tab_concept_load:
        concept_load_tab()
    
    with tab_semantics:
        semantics_tab()

    with tab_data_load:
        data_load_tab()

    with tab_eda:
        eda_tab()

