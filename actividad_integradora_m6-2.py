# -*- coding: utf-8 -*-
"""Actividad Integradora M6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1abqWyCSS3NNHDrEGbK0BzY01jJqIjTo5
"""

import pandas as pd
import streamlit as st
import numpy as np

import plotly as px

import plotly.figure_factory as ff

from bokeh.plotting import figure

import matplotlib.pyplot as plt

st.title( 'Police Incident Reports from 2018 to 2020 in San Francisco')

df = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")

st.markdown("The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.")

mapa=pd.DataFrame()
mapa=mapa.dropna()
st.map(mapa.astype(int))