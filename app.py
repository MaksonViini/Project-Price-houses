import pandas as pd
import streamlit as st
import plotly.express as px
from multiapp import MultiApp
from apps import dataapp

app = MultiApp()


# # Adicionando todos as paginas na aplicacao
app.add_app('Dataapp', dataapp.app)

# Main app
app.run()
