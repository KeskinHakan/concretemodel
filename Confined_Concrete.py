# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:56:55 2022

@author: hakan
"""

import streamlit as st
import pandas as pd
from math import sqrt
from PIL import Image


st.title("Confined & Unconfined Concrete Model")

"""
Confined and Unconfined concrete calculator according to Mander Concrete Model

To use the app you should choose at the following items below:
    
"""


# Unconfined and Confined Concrete Model (Mander Model)

def soilType_func(fc,fy, b, h, cover, dia_long, number_long, dia_trans, n_leg_x, n_leg_y, s):
    d = h-cover # clear height
    b_clear = b-cover # clear height
    A_long = 3.14*dia_long**2/4 # pi için math kütüphanesi çağıralacak. Longitudinal rebar area
    A_tra = 3.14*dia_trans**2/4 
    As = A_long*number_long
    bo = d-cover-dia_trans
    ho = b_clear-cover-dia_trans
    A = ho*bo/1000000
    A_tra_x = A_tra*n_leg_x
    A_tra_y = A_tra*n_leg_y
    ratio_x = (n_leg_x*bo*A_tra)/(ho*bo*s)
    ratio_y = (n_leg_x*ho*A_tra)/(ho*bo*s)
    total_ratio = ratio_x + ratio_y
    
    return d, b_clear, A_long, A_tra, As, bo, ho, A, A_tra_x, A_tra_y, ratio_x, ratio_y, total_ratio



img_1 = Image.open("ColumnSection.png")
col1, col2, col3,col4,col5 = st.columns([1,1,1,1,1])
col2.image(img_1, width = 500, caption = "Typical Column Section")

st.sidebar.header("Material Properties")

coefficient = st.sidebar.selectbox("Material Coefficient: ", {"Nominal", "Expected"})

fc = st.sidebar.number_input("Concrete Compressive Strength for Confined Concrete - fc: ",value=20.00, step=1.0)
fy = st.sidebar.number_input("Yield Strength of Longitudinal Rebar - fy: ",value=420.0, step=10.0)

st.sidebar.header("Section Properties")

b = st.sidebar.number_input("Width of the concrete section - b: ",value=600.0, step=50.0)
h = st.sidebar.number_input("Height of the concrete section - h: ",value=600.0, step=50.0)
cover = st.sidebar.number_input("Concrete cover - d': ",value=40.0, step=5.0)

col1, col2, col3, col4 = st.columns(4)
with col1:
    dia_long = st.number_input("Diameter of Longitudinal Rebar - Φ: ",value=18.0, step=1.0)
with col2:
    number_long = st.number_input("Number of Longitudinal Rebar - n: ",value=12.0, step=1.0)
with col3:
    n_of_long_x = st.number_input("Number of longitudinal Rebar for X Dir - nx: ",value=3.0, step=1.0)
with col4:
    n_of_long_y = st.number_input("Number of longitudinal Rebar for Y Dir - ny: ",value=3.0, step=1.0)
col1, col2, col3, col4 = st.columns(4)
with col1:
    dia_trans = st.number_input("Diameter of Transverse Rebar - Φ: ",value=8.0, step=1.0)
with col2:
    s = st.number_input("Spacing of Transverse Rebar - s: ",value=150.0, step=10.0)
with col3:
    n_leg_x = st.number_input("Number of Transverse Rebar - X Dir - n_leg_x: ",value=4.0, step=1.0)
with col4:
    n_leg_y = st.number_input("Number of Transverse Rebar - Y Dir - n_leg_y: ",value=4.0, step=1.0)




if n_of_long_x == 2:
    col1, col2, col3 = st.columns(3)
    with col1:
        ax1 = st.number_input("ax1: ", value=360.0, step=1.0)
elif n_of_long_x == 3:
    col1, col2, col3 = st.columns(3)
    with col1:
        ax1 = st.number_input("ax1: ", value=360.0, step=1.0)
        ax2 = st.number_input("ax2: ", value=180.0, step=1.0)
elif n_of_long_x == 4:
    col1, col2, col3 = st.columns(3)
    with col1:
        ax1 = st.number_input("ax1: ", value=360.0, step=1.0)
        ax2 = st.number_input("ax2: ", value=180.0, step=1.0)
    with col2:
        ax3 = st.number_input("ax3: ", value=180.0, step=1.0)
elif n_of_long_x == 5:
    col1, col2, col3 = st.columns(3)
    with col1:
        ax1 = st.number_input("ax1: ", value=360.0, step=1.0)
        ax2 = st.number_input("ax2: ", value=180.0, step=1.0)
    with col2:
        ax3 = st.number_input("ax3: ", value=180.0, step=1.0)
        ax4 = st.number_input("ax4: ", value=180.0, step=1.0)
elif n_of_long_x == 6:
    col1, col2, col3 = st.columns(3)
    with col1:
        ax1 = st.number_input("ax1: ", value=360.0, step=1.0)
        ax2 = st.number_input("ax2: ", value=180.0, step=1.0)
    with col2:
        ax3 = st.number_input("ax3: ", value=180.0, step=1.0)
        ax4 = st.number_input("ax4: ", value=180.0, step=1.0)
    with col3:
        ax5 = st.number_input("ax5: ", value=180.0, step=1.0)
elif n_of_long_x == 7:
    col1, col2, col3 = st.columns(3)
    with col1:
        ax1 = st.number_input("ax1: ", value=360.0, step=1.0)
        ax2 = st.number_input("ax2: ", value=180.0, step=1.0)
    with col2:
        ax3 = st.number_input("ax3: ", value=180.0, step=1.0)
        ax4 = st.number_input("ax4: ", value=180.0, step=1.0)
    with col3:
        ax5 = st.number_input("ax5: ", value=180.0, step=1.0)
        ax6 = st.number_input("ax6: ", value=180.0, step=1.0)
        
if n_of_long_y == 2:
    col1, col2, col3 = st.columns(3)
    with col1:
        ay1 = st.number_input("ay1: ", value=360.0, step=1.0)
elif n_of_long_y == 3:
    col1, col2, col3 = st.columns(3)
    with col1:
        ay1 = st.number_input("ay1: ", value=360.0, step=1.0)
        ay2 = st.number_input("ay2: ", value=180.0, step=1.0)
elif n_of_long_y == 4:
    col1, col2, col3 = st.columns(3)
    with col1:
        ay1 = st.number_input("ay1: ", value=360.0, step=1.0)
        ay2 = st.number_input("ay2: ", value=180.0, step=1.0)
    with col2:
        ay3 = st.number_input("ay3: ", value=180.0, step=1.0)
elif n_of_long_y == 5:
    col1, col2, col3 = st.columns(3)
    with col1:
        ay1 = st.number_input("ay1: ", value=360.0, step=1.0)
        ay2 = st.number_input("ay2: ", value=180.0, step=1.0)
    with col2:
        ay3 = st.number_input("ay3: ", value=180.0, step=1.0)
        ay4 = st.number_input("ay4: ", value=180.0, step=1.0)
elif n_of_long_y == 6:
    col1, col2, col3 = st.columns(3)
    with col1:
        ay1 = st.number_input("ay1: ", value=360.0, step=1.0)
        ay2 = st.number_input("ay2: ", value=180.0, step=1.0)
    with col2:
        ay3 = st.number_input("ay3: ", value=180.0, step=1.0)
        ay4 = st.number_input("ay4: ", value=180.0, step=1.0)
    with col3:
        ay5 = st.number_input("ay5: ", value=180.0, step=1.0)
elif n_of_long_y == 7:
    col1, col2, col3 = st.columns(3)
    with col1:
        ay1 = st.number_input("ay1: ", value=360.0, step=1.0)
        ay2 = st.number_input("ay2: ", value=180.0, step=1.0)
    with col2:
        ay3 = st.number_input("ay3: ", value=180.0, step=1.0)
        ay4 = st.number_input("ay4: ", value=180.0, step=1.0)
    with col3:
        ay5 = st.number_input("ay5: ", value=180.0, step=1.0)
        ay6 = st.number_input("ay6: ", value=180.0, step=1.0)
   

d, b_clear, A_long, A_tra, As, bo, ho, A, A_tra_x, A_tra_y, ratio_x, ratio_y, total_ratio = soilType_func(fc,fy, b, h, cover, dia_long, number_long, dia_trans, n_leg_x, n_leg_y, s)
ke = (1-180267/(6*bo*ho))*(1-s/(2*bo))*(1-s/(2*ho))*(1-As/(bo*ho))**-1

if coefficient == "Nominal":
    fyh = fy
elif coefficient == "Expected":
    fyh = fy*1.2
fex = ke*ratio_x*fyh
fey = ke*ratio_y*fyh
f1 = (fex+fey)/2
if coefficient == "Nominal":
    fco = fc
elif coefficient == "Expected":
    fco = fc*1.3
lambda_c = 2.254*sqrt(1+7.94*f1/fco)-2*(f1/fco)-1.254
fcc = fco*lambda_c
fsp = 0
eco = 0.002
ecu = 0.0035
esp = 0.005
ecc = eco*(1+5*(lambda_c-1))

Ec = 5000*sqrt(fco)
Esec = fcc/ecc
Esec_unc = fco/eco
r = Ec/(Ec-Esec)
r_unc = Ec/(Ec-Esec_unc)
f_cu = fco*(ecu/eco)*r_unc/(r_unc-1+(ecu/eco)**r_unc)

e = 0
fc_conf= []
fc_unconf= []
ec_conf = []
ec_unconf = []
x_conf = []
x_unconf = []
while e < 0.02:
        x = e/ecc
        fc = (fcc*x*r)/(r-1+x**r)
        fc_conf.append(format(fc, ".3f"))
        ec_conf.append(format(e, ".5f"))
        x_conf.append(format(x, ".3f"))
        e = e + 0.0001
        
e = 0
while e <= esp:
        x = e/eco
        if e <= ecu:
            fc = fco*x*r_unc/(r_unc-1+x**r_unc)
        elif e > ecu and e<=esp:
            fc = f_cu+(e-ecu)*((fsp-f_cu)/(esp-ecu))
        fc_unconf.append(format(fc, ".3f"))
        ec_unconf.append(format(e, ".5f"))
        x_unconf.append(format(x, ".3f"))
        e = e + 0.0001
e = 0.0036
fc1 = f_cu+(e-ecu)*((fsp-f_cu)/(esp-ecu))

df_conf = pd.DataFrame(list(zip(ec_conf, fc_conf)), columns =['Strain', 'Stress'], dtype = float)

#Line Chart
as_list = df_conf["Strain"].tolist()

df_conf.index = as_list

df_fc = df_conf['Stress']
st.line_chart(df_fc)

df_unconf = pd.DataFrame(list(zip(ec_unconf, fc_unconf)), columns =['Strain', 'Stress'], dtype = float)

#Line Chart
as_list = df_unconf["Strain"].tolist()

df_unconf.index = as_list

df_fc = df_unconf['Stress']
st.line_chart(df_fc)

def convert_confined_df(df_conf):
   return df_conf.to_csv().encode('utf-8')
def convert_unconfined_df(df_unconf):
   return df_unconf.to_csv().encode('utf-8')


csv_conf = convert_confined_df(df_conf)
csv_unconf = convert_unconfined_df(df_unconf)

st.download_button(
   "Confined Concrete - Download",
   csv_conf,
   "confined.csv",
   "text/csv",
   key='download-csv'
)

st.download_button(
   "Unconfined Concrete - Download",
   csv_unconf,
   "unconfined.csv",
   "text/csv",
   key='download-csv'
)

