#!/usr/bin/env python
# coding: utf-8

# In[47]:


#Lat 1
import math
a = int(input("Masukkan bilangan bulat pertama (a): "))
b = int(input("Masukkan bilangan bulat kedua (b): "))

penjumlah = a + b
pengurangan = b - a
perkalian = a * b
sisa_pembagian = a % b
pembagian = a / b
log_a = math.log10(a)
pangkat = a ** b

print(f"penjumlahan: {jumlah}")
print(f"pengurangan: {selisih}")
print(f"perkalian: {hasil_kali}")
print(f"sisa_pembagian: {sisa_pembagian}")
print(f"Pembagian: {pembagian}")
print(f"log(a): {log_a}")
print(f"pemangkatan: {pangkat}")


# In[38]:


#Lat 2
# Rumus Haversine Formula :
# Δlat = lat2- lat1
# Δlong = long2- long1
# a = sin2 (Δlat/2) + cos(lat1).cos(lat2).sin2 (Δlong/2)
# c = 2atan2(√a, √1-a)
# d = R.c
# Keterangan :
# R = jari-jari bumi sebesar 6371(km)
# Δlat = besaran perubahan latitude
# Δlong = besaran perubahan longitude
# C = kalkulasi perpotongan sumbu
# d = jarak (km)
# 1 derajat = 0.0174532925 radian
from math import *
R = 6371.0
lintang1 = math.radians(float(input("lintang kota 1 = ")))
bujur1 = math.radians(float(input("bujur kota 1 = ")))
lintang2 = math.radians(float(input("lintang kota 2 = ")))
bujur2 = math.radians(float(input("bujur kota 2 = ")))
R = 6371

lat = lintang2 - lintang1
long = bujur2-bujur1
a = math.sin(lat/2)**2 + math.cos(lintang1)*math.cos(lintang2)*math.sin(long/2)**2
c = 2*math.atan2(sqrt(a), sqrt(1-a))
d = R*c
print(d)


# In[ ]:




