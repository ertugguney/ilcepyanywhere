#%%
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
import xlsxwriter
from dash.exceptions import PreventUpdate
from app import app

# import dask.dataframe

# # İlce verisi okuma ve birleştirme-Gerektiğinde kullanılacak

# import pandas as pd
# import numpy as np
# ilceData1 = pd.read_csv('../ilce-veri/1_Hepsi_Egitim_vs.csv',sep=',', encoding='windows-1254')
# ilceData2 = pd.read_csv('../ilce-veri/2_Hepsi_Meyveler.csv',sep=',', encoding='windows-1254')
# ilceData3 = pd.read_csv('../ilce-veri/3_Hepsi_Sebzeler+Seracılık.csv',sep=',', encoding='windows-1254')
# ilceData4 = pd.read_csv('../ilce-veri/4_Hepsi_Tarla Bitkileri.csv',sep=',', encoding='windows-1254')
# ilceData5 = pd.read_csv('../ilce-veri/5_Hepsi_Tarımsal_Alet.csv',sep=',', encoding='windows-1254')

# ilceData=pd.concat([ilceData1,ilceData2, ilceData3,ilceData4,ilceData5], ignore_index=True)
# ilceData=ilceData.sort_values(["Yıl","İl Adı","İlçe Adı","anabaslik","ortabaslik","baslik"],ascending=[True,True, True, True,True,True]).reset_index(drop=True)

# export_excel = ilceData.to_csv(r'../ilce-veri/ilceData_02.12.21.csv', index = None, header=True)


import urllib.request, json
with urllib.request.urlopen("https://raw.githubusercontent.com/ertugguney/harita/main/ilceHarita_17.11.21_engchar.geojson") as url:
    counties = json.loads(url.read().decode())

# http://crm.trakyaka.org.tr/ap/datasets/ilceHarita_17.11.21_engchar.geojson

# df = pd.read_csv('../ilce-veri/ilceData_02.12.21.csv',sep=',',encoding='utf-8-sig')

# df = dask.dataframe.read_csv('../ilce-veri/ilceData_02.12.21.csv')
# df = pd.read_csv('datasets/ilceData_04.12.21_Il_Ilcesiz.csv',sep=',',encoding='utf-8-sig')
df = pd.read_csv('https://raw.githubusercontent.com/ertugguney/2017-2020-datasets/main/ilceData_04.12.21_Il_Ilcesiz.csv',sep=',',encoding='utf-8-sig')

# http://crm.trakyaka.org.tr/ap/datasets/ilceData_04.12.21_Il_Ilcesiz.csv

yerlesim= pd.read_csv('https://raw.githubusercontent.com/ertugguney/2017-2020-datasets/main/yerlesim.csv',sep=',',encoding='windows-1254')

# http://crm.trakyaka.org.tr/ap/datasets/yerlesim.csv

# ilce= pd.read_csv('../ilce-veri/ilce_harita_deger.csv',sep=',',encoding='windows-1254')
# ilce_adi= pd.read_csv('../ilce-veri/il_ilce.csv',sep=',',encoding='windows-1254')
# bolge= pd.read_csv('../ilce-veri/bolge-il.csv',sep=',',encoding='windows-1254')

# df1=df.dropna()
# df2=df1.groupby(by=['Yıl', 'İl Adı', 'İlçe Adı', 'İl-İlçe', 'anabaslik','ortabaslik', 'baslik'])['deger'].sum().reset_index()

# df =pd.merge(df,ilce_adi, on=["İlçe Adı","İl-İlçe"])
# df =pd.merge(df,bolge, on="İl Adı")
df =pd.merge(df,yerlesim, on=["İl-İlçe"])

# ilce_adi=ilce_adi[["İlçe Adı","İl-İlçe"]]

ilce_adi=yerlesim[["İlçe Adı","İl-İlçe"]]

# df=df[['Yıl','Bölge (Düzey-2)', 'İl Adı', 'İlçe Adı', 'ilce_no', 'İl-İlçe', 'anabaslik', 'ortabaslik', 'baslik', 'deger']]

# df.to_csv(r'ilceData_26.11.21.csv', index = None, header=True)

# df = pd.read_csv('../ilce-veri/ilceData_26.11.21.csv',sep=',',encoding='utf-8-sig')
# ilce_adi = df[(df["anabaslik"]=="Nüfus")&(df["ortabaslik"]=="Nüfus")&(df["baslik"]=="Nüfus")&(df["Yıl"]==2020)][["İl-İlçe"]].reset_index(drop=True)

# df1 = df.copy()

# #excel download yapılan işlemler

# df1_1=df1.iloc[:1048575]
# df1_2=df1.iloc[1048575:2097150]
# df1_3=df1.iloc[2097150:3145725]
# df1_4=df1.iloc[3145725:4194300]
# df1_5=df1.iloc[4194300:{

# writer = pd.ExcelWriter('new_excel_file.xlsx', engine='xlsxwriter')

# df1_1.to_excel(writer, sheet_name='istatistik1')
# df1_2.to_excel(writer, sheet_name='istatistik2')
# df1_3.to_excel(writer, sheet_name='istatistik3')
# df1_4.to_excel(writer, sheet_name='istatistik4')
# df1_5.to_excel(writer, sheet_name='istatistik5')

# writer.save()

# app = dash.Dash(__name__,
#     external_stylesheets=[dbc.themes.CERULEAN],
#     meta_tags=[{'name':     'viewport',
#                 'content': 'width=device-width, initial-scale=1.0'}]
#     )

# server = app.server

all_options = {
    'Nüfus': {
        'Nüfus': ['Nüfus'],
    },
    'Eğitim': {
        'Bitirilen Eğitim Seviyesi': ['Doktora - Erkek','Doktora - Kadın','Doktora - Toplam','İlkokul - Erkek','İlkokul - Kadın','İlkokul - Toplam','İlköğretim - Erkek','İlköğretim - Kadın','İlköğretim - Toplam','Lise Ve Dengi Meslek Okulu - Erkek','Lise Ve Dengi Meslek Okulu - Kadın','Lise Ve Dengi Meslek Okulu - Toplam','Okuma Yazma Bilen Fakat Bir Okul Bitirmeyen - Erkek','Okuma Yazma Bilen Fakat Bir Okul Bitirmeyen - Kadın','Okuma Yazma Bilen Fakat Bir Okul Bitirmeyen - Toplam','Okuma Yazma Bilmeyen - Erkek','Okuma Yazma Bilmeyen - Kadın','Okuma Yazma Bilmeyen - Toplam','Ortaokul Ve Dengi Meslek Okulu  - Erkek','Ortaokul Ve Dengi Meslek Okulu  - Kadın','Ortaokul Ve Dengi Meslek Okulu  - Toplam','Yüksek Lisans (5 Veya 6 Yıllık Fakülteler Dahil) - Erkek','Yüksek Lisans (5 Veya 6 Yıllık Fakülteler Dahil) - Kadın','Yüksek Lisans (5 Veya 6 Yıllık Fakülteler Dahil) - Toplam','Yüksekokul Veya Fakülte - Erkek','Yüksekokul Veya Fakülte - Kadın','Yüksekokul Veya Fakülte - Toplam'],
    },
    'Hayvancılık': {
        'Arıcılık': ['Bal Mumu Üretimi (Ton)','Bal Üretimi (Ton)','İşletme Sayısı','Kovan Sayısı',],
        'Hayvan Sayısı': ['At','Deve','Domuz','Eşek','Katır','Keçi (Kıl Keçisi Ve Diğer Irklar)','Keçi (Tiftik Keçisi)','Koyun (Merinos Irkı)','Koyun (Yerli Ve Diğer Irklar)','Manda','Sığır (Kültür Irkı)','Sığır (Kültür Melezi Irkı)','Sığır (Yerli  Irk)',],
        'İpekböcekciliği': ['Açılan Kutu (Adet)','Hane Sayısı','Köy Sayısı','Yaş Koza (Ton)',],'Kanatlılar': ['Etçi Tavuk (Adet)','Hindi (Adet)','Kaz (Adet)','Ördek (Adet)','Yumurtacı Tavuk (Adet)',],'Kırkılan Hayvan Sayısı (Baş)': ['Keçi (Kıl)','Keçi (Tiftik)','Koyun (Merinos)','Koyun (Yerli)',],'Sağılan Hayvan Sayısı (Baş)': ['Keçi (Kıl)','Keçi (Tiftik)','Koyun (Merinos)','Koyun (Yerli)','Manda','Sığır (Kültür)','Sığır (Melez)','Sığır (Yerli)',],
        'Süt (Ton)': ['Keçi (Kıl)','Keçi (Tiftik)','Koyun (Merinos)','Koyun (Yerli)','Manda','Sığır (Kültür)','Sığır (Melez)','Sığır (Yerli)',],
        'Yün-Kıl-Tiftik (Ton)': ['Keçi (Kıl)','Keçi (Tiftik)','Koyun (Merinos)','Koyun (Yerli)'],
    },
    'Konut': {
        'Konut Satışı': ['Konut Satışı'],
    },
    'Meyveler': {
        'Meyve Veren Yaşta Ağaç Sayısı': ['Ahududu','Anason','Antep Fıstığı','Armut','Avokado','Ayva','Badem','Böğürtlen','Ceviz','Çay (Yaş)','Çilek','Çörekotu','Dut','Elma (Amasya)','Elma (Diğer)','Elma (Golden)','Elma (Grannysmith)','Elma (Starking)','Erik','Fındık','Greyfurt (Altıntop)','Hünnap','İğde','İncir','Kapari (Gebere Otu)','Kayısı','Keçi Boynuzu','Kekik','Kestane','Kırmızı Biber (Baharatlık-İşlenmemiş)','Kızılcık','Kimyon','Kiraz','Kişniş','Kivi','Limon','Mandalina (Clementin)','Mandalina (Diğer)','Mandalina (King)','Mandalina (Satsuma)','Muşmula','Muz','Nar','Portakal (Diğer)','Portakal (Washington)','Portakal (Yafa)','Rezene','Süpürge Otu','Şeftali (Diğer)','Şeftali (Nektarin)','Trabzon Hurması','Turunç','Üzüm (Kurutmalık-Çekirdekli)','Üzüm (Kurutmalık-Çekirdeksiz)','Üzüm (Sofralık-Çekirdekli)','Üzüm (Sofralık-Çekirdeksiz)','Üzüm (Şaraplık)','Vişne','Yaban Mersini (Mavi Yemiş)','Yenidünya','Zerdali','Zeytin (Sofralık)','Zeytin (Yağlık)',],
        'Meyve Vermeyen Yaşta Ağaç Sayısı': ['Ahududu','Anason','Antep Fıstığı','Armut','Avokado','Ayva','Badem','Böğürtlen','Ceviz','Çay (Yaş)','Çilek','Çörekotu','Dut','Elma (Amasya)','Elma (Diğer)','Elma (Golden)','Elma (Grannysmith)','Elma (Starking)','Erik','Fındık','Greyfurt (Altıntop)','Hünnap','İğde','İncir','Kapari (Gebere Otu)','Kayısı','Keçi Boynuzu','Kekik','Kestane','Kırmızı Biber (Baharatlık-İşlenmemiş)','Kızılcık','Kimyon','Kiraz','Kişniş','Kivi','Limon','Mandalina (Clementin)','Mandalina (Diğer)','Mandalina (King)','Mandalina (Satsuma)','Muşmula','Muz','Nar','Portakal (Diğer)','Portakal (Washington)','Portakal (Yafa)','Rezene','Süpürge Otu','Şeftali (Diğer)','Şeftali (Nektarin)','Trabzon Hurması','Turunç','Üzüm (Kurutmalık-Çekirdekli)','Üzüm (Kurutmalık-Çekirdeksiz)','Üzüm (Sofralık-Çekirdekli)','Üzüm (Sofralık-Çekirdeksiz)','Üzüm (Şaraplık)','Vişne','Yaban Mersini (Mavi Yemiş)','Yenidünya','Zerdali','Zeytin (Sofralık)','Zeytin (Yağlık)',],
        'Toplu Meyveliklerin Alanı (Dekar)': ['Ahududu','Anason','Antep Fıstığı','Armut','Avokado','Ayva','Badem','Böğürtlen','Ceviz','Çay (Yaş)','Çilek','Çörekotu','Dut','Elma (Amasya)','Elma (Diğer)','Elma (Golden)','Elma (Grannysmith)','Elma (Starking)','Erik','Fındık','Greyfurt (Altıntop)','Hünnap','İğde','İncir','Kapari (Gebere Otu)','Kayısı','Keçi Boynuzu','Kekik','Kestane','Kırmızı Biber (Baharatlık-İşlenmemiş)','Kızılcık','Kimyon','Kiraz','Kişniş','Kivi','Limon','Mandalina (Clementin)','Mandalina (Diğer)','Mandalina (King)','Mandalina (Satsuma)','Muşmula','Muz','Nar','Portakal (Diğer)','Portakal (Washington)','Portakal (Yafa)','Rezene','Süpürge Otu','Şeftali (Diğer)','Şeftali (Nektarin)','Trabzon Hurması','Turunç','Üzüm (Kurutmalık-Çekirdekli)','Üzüm (Kurutmalık-Çekirdeksiz)','Üzüm (Sofralık-Çekirdekli)','Üzüm (Sofralık-Çekirdeksiz)','Üzüm (Şaraplık)','Vişne','Yaban Mersini (Mavi Yemiş)','Yenidünya','Zerdali','Zeytin (Sofralık)','Zeytin (Yağlık)',],
        'Üretim (Ton)': ['Ahududu','Anason','Antep Fıstığı','Armut','Avokado','Ayva','Badem','Böğürtlen','Ceviz','Çay (Yaş)','Çilek','Çörekotu','Dut','Elma (Amasya)','Elma (Diğer)','Elma (Golden)','Elma (Grannysmith)','Elma (Starking)','Erik','Fındık','Greyfurt (Altıntop)','Hünnap','İğde','İncir','Kapari (Gebere Otu)','Kayısı','Keçi Boynuzu','Kekik','Kestane','Kırmızı Biber (Baharatlık-İşlenmemiş)','Kızılcık','Kimyon','Kiraz','Kişniş','Kivi','Limon','Mandalina (Clementin)','Mandalina (Diğer)','Mandalina (King)','Mandalina (Satsuma)','Muşmula','Muz','Nar','Portakal (Diğer)','Portakal (Washington)','Portakal (Yafa)','Rezene','Süpürge Otu','Şeftali (Diğer)','Şeftali (Nektarin)','Trabzon Hurması','Turunç','Üzüm (Kurutmalık-Çekirdekli)','Üzüm (Kurutmalık-Çekirdeksiz)','Üzüm (Sofralık-Çekirdekli)','Üzüm (Sofralık-Çekirdeksiz)','Üzüm (Şaraplık)','Vişne','Yaban Mersini (Mavi Yemiş)','Yenidünya','Zerdali','Zeytin (Sofralık)','Zeytin (Yağlık)'],
    },
    'Sebzeler': {
        'Ekilen Alan (Dekar)': ['Acur','Bakla (Taze)','Balkabağı','Bamya','Barbunya Fasulye (Taze)','Bezelye (Taze)','Biber (Çarliston)','Biber (Dolmalık)','Biber (Salçalık, Kapya)','Biber (Sivri)','Börülce (Taze)','Brokoli','Dereotu','Domates','Domates (Salçalık)','Domates (Sofralık)','Enginar','Fasulye (Taze)','Havuç','Hıyar','Hıyar (Sofralık)','Hıyar (Turşuluk)','Ispanak','Kabak (Çerezlik)','Kabak (Sakız)','Karnıbahar','Karpuz','Kavun','Kereviz (Kök)','Kereviz (Sap)','Kırmızı Pancar','Kuşkonmaz','Lahana (Beyaz)','Lahana (Brüksel)','Lahana (Karayaprak)','Lahana (Kırmızı)','Mantar (Kültür)','Marul (Aysberg)','Marul (Göbekli)','Marul (Kıvırcık)','Maydonoz','Nane','Patlıcan','Pazı','Pepino','Pırasa','Roka','Sarımsak (Kuru)','Sarımsak (Taze)','Semizotu','Soğan (Kuru)','Soğan (Taze)','Şalgam','Tere','Turp (Bayır)','Turp (Beyaz)','Turp (Kırmızı)',],
        'Üretim (Ton)': ['Acur','Bakla (Taze)','Balkabağı','Bamya','Barbunya Fasulye (Taze)','Bezelye (Taze)','Biber (Çarliston)','Biber (Dolmalık)','Biber (Salçalık, Kapya)','Biber (Sivri)','Börülce (Taze)','Brokoli','Dereotu','Domates','Domates (Salçalık)','Domates (Sofralık)','Enginar','Fasulye (Taze)','Havuç','Hıyar','Hıyar (Sofralık)','Hıyar (Turşuluk)','Ispanak','Kabak (Çerezlik)','Kabak (Sakız)','Karnıbahar','Karpuz','Kavun','Kereviz (Kök)','Kereviz (Sap)','Kırmızı Pancar','Kuşkonmaz','Lahana (Beyaz)','Lahana (Brüksel)','Lahana (Karayaprak)','Lahana (Kırmızı)','Mantar (Kültür)','Marul (Aysberg)','Marul (Göbekli)','Marul (Kıvırcık)','Maydonoz','Nane','Patlıcan','Pazı','Pepino','Pırasa','Roka','Sarımsak (Kuru)','Sarımsak (Taze)','Semizotu','Soğan (Kuru)','Soğan (Taze)','Şalgam','Tere','Turp (Bayır)','Turp (Beyaz)','Turp (Kırmızı)'],
    },
    'Seracılık (Örtüaltı)': {
        'Alan (Dekar)': ['Bakla (Taze)','Bamya','Bezelye (Taze)','Biber (Çarliston)','Biber (Dolmalık)','Biber (Salçalık, Kapya)','Biber (Sivri)','Börülce (Taze)','Brokoli','Çilek','Dereotu','Domates','Enginar','Erik','Fasulye (Taze)','Hıyar','Ispanak','Kabak (Sakız)','Karnıbahar','Karpuz','Kavun','Kayısı','Lahana (Brüksel)','Lahana (Karayaprak)','Lahana (Kırmızı)','Marul (Aysberg)','Marul (Göbekli)','Marul (Kıvırcık)','Maydonoz','Muz','Nane','Patlıcan','Pepino','Pırasa','Roka','Sarımsak (Taze)','Semizotu','Soğan (Taze)','Şeftali (Nektarin)','Tere','Turp (Beyaz)','Turp (Kırmızı)','Üzüm (Sofralık-Çekirdekli)','Üzüm (Sofralık-Çekirdeksiz)',],
        'Ekilen Alan (M2)': ['Anemon (Manisa Lalesi)','Çiçek Soğanları','Dış Mekan Süs Bitkileri','Diğer Kesme Çiçekler','Fresia','Gerbera','Glayöl (Gladiol)','Gül (Kesme)','Gypsohilla','İç Mekan Süs Bitkileri','İris','Karanfil','Kasımpatı (Krizantem)','Lale','Lilyum (Zambak)','Lisianthus','Nergiz','Orkide','Solidago (Altınbaşak)','Statice','Sümbül','Şebboy',],
        'Örtüaltı Tarım Alanları': ['Toplam Alçak Tünel Alanı (Dekar)','Toplam Cam Sera Alanı (Dekar)','Toplam Örtüaltı Alanı (Dekar)','Toplam Plastik Sera Alanı (Dekar)','Toplam Yüksek Tünel Alanı (Dekar)',],
        'Üretim (Adet)': ['Anemon (Manisa Lalesi)','Çiçek Soğanları','Dış Mekan Süs Bitkileri','Diğer Kesme Çiçekler','Fresia','Gerbera','Glayöl (Gladiol)','Gül (Kesme)','Gypsohilla','İç Mekan Süs Bitkileri','İris','Karanfil','Kasımpatı (Krizantem)','Lale','Lilyum (Zambak)','Lisianthus','Nergiz','Orkide','Solidago (Altınbaşak)','Statice','Sümbül','Şebboy',],
        'Üretim (Ton)': ['Bakla (Taze)','Bamya','Bezelye (Taze)','Biber (Çarliston)','Biber (Dolmalık)','Biber (Salçalık, Kapya)','Biber (Sivri)','Börülce (Taze)','Brokoli','Çilek','Dereotu','Domates','Enginar','Erik','Fasulye (Taze)','Hıyar','Ispanak','Kabak (Sakız)','Karnıbahar','Karpuz','Kavun','Kayısı','Lahana (Brüksel)','Lahana (Karayaprak)','Lahana (Kırmızı)','Marul (Aysberg)','Marul (Göbekli)','Marul (Kıvırcık)','Maydonoz','Muz','Nane','Patlıcan','Pepino','Pırasa','Roka','Sarımsak (Taze)','Semizotu','Soğan (Taze)','Şeftali (Nektarin)','Tere','Turp (Beyaz)','Turp (Kırmızı)','Üzüm (Sofralık-Çekirdekli)','Üzüm (Sofralık-Çekirdeksiz)'],
    },
    'Süs Bitkileri': {
        'Ekilen Alan (M2)': ['Anemon (Manisa Lalesi)','Çiçek Soğanları','Dış Mekan Süs Bitkileri','Diğer Kesme Çiçekler','Fresia','Gerbera','Glayöl (Gladiol)','Gül (Kesme)','Gypsohilla','İç Mekan Süs Bitkileri','İris','Karanfil','Kasımpatı (Krizantem)','Lale','Lilyum (Zambak)','Lisianthus','Nergiz','Orkide','Solidago (Altınbaşak)','Statice','Sümbül','Şebboy',],
        'Üretim (Adet)': ['Anemon (Manisa Lalesi)','Çiçek Soğanları','Dış Mekan Süs Bitkileri','Diğer Kesme Çiçekler','Fresia','Gerbera','Glayöl (Gladiol)','Gül (Kesme)','Gypsohilla','İç Mekan Süs Bitkileri','İris','Karanfil','Kasımpatı (Krizantem)','Lale','Lilyum (Zambak)','Lisianthus','Nergiz','Orkide','Solidago (Altınbaşak)','Statice','Sümbül','Şebboy'],
    },
    'Tarımsal Alan': {
        'Tarım Alanı': ['Meyveler, İçecek Ve Baharat Bitkileri Alanı (Dekar)','Nadas Alanı (Dekar)','Sebze Alanı (Dekar)','Süs Bitkileri Alanı (Dekar)','Tarla Bitkileri Alanı (Dekar)','Toplam Alan (Dekar)'],
    },
    'Tarımsal Alet': {
        'Biçerdöverler': ['Biçerdöver (0-5 Yaş)','Biçerdöver (11-20 Yaş)','Biçerdöver (21 Yaş Ve Üzeri)','Biçerdöver (6-10 Yaş)','Biçerdöver (Kendi Yürür Biçerdöver)',],
        'Hasat Makineleri': ['Döven','Fındık Harman Makinası','Harman Makinası','Kimyevi Gübre Dağıtma Makinası','Kombine Pancar Hasat Makinası','Kombine Pancar Hasat Makineleri Makinası','Kombine Patates Hasat Makinası','Kombine Patates Hasat Makineleri Makinası','Meyve Hasat Makinaları','Meyve Hasat Makineleri Makinaları','Mısır Daneleme Makinası','Mısır Hasat Makinası','Mısır Hasat Makineleri Makinası','Motorlu Tırpan','Orak Makinası','Pamuk Toplama Makinası','Pancar Sökme Makinası','Patates Sökme Makinası','Sap Döver','Selektör (Sabit Veya Seyyar)','Traktörle Çekilen Çayır Biçme Makinası','Ürün Kurutma Makinası','Yem Hazırlama Makinası','Yem Makineleri Hazırlama Makinası','Yerfıstığı Harman Makinası','Yerfıstığı Hasat Makinası','Yerfıstığı Hasat Makineleri Makinası',],
        'Hayvansal Üretim Makineleri': ['Civciv Ana Makinası','Hayvanla Çekilen Çapa Makinaları','Hayvanla Çekilen Çayır Biçme Makinası','Hayvanla Çekilen Hububat Ekim Makinası','Krema Makinası','Kuluçka Makinası','Süt Sağım Makinası (Seyyar)','Süt Sağım Tesisi','Yayık','Yem Dağıtıcı Römork','Yem Makineleri Dağıtıcı Römork',],
        'İlaçlama/Gübreleme Makineleri': ['Atomizör','Çiftlik Gübresi Dağıtma Makinası','Kuyruk Milinden Hareketli Pulverizatör','Motorlu Pulverizatör','Sedyeli, Motorlu Pulverizatör Tozlayıcı  Kombine Atomizör','Sırt Pulverizatörü','Tarımsal Mücadele Uçağı','Tozlayıcı',],
        'Sulama Makineleri': ['Damla Sulama Makineleri Tesisi','Damla Sulama Tesisi','Derin Kuyu Pompa','Elektropomp','Motopomp (Termik)','Santrifüj Pompa','Su Tankeri (Tarımda Kullanılan)','Yağmurlama Tesisi',],
        'Toprak İşleme Makineleri': ['Anıza Ekim Makinası','Ark Açma Pulluğu','Dip Kazan (Subsoiler)','Diskli Anız Pulluğu (Vanvey)','Diskli Tırmık (Diskarolar)','Diskli Traktör Pulluğu','Dişli Tırmık','Döner Kulaklı Traktör Pulluğu','Fide Dikim Makinası','Hayvan Pulluğu','Hayvanla Ve Traktörle Çekilen Ara Çapa Makinası','Karasaban','Kombikürüm (Karma Tırmık)','Kombine Hububat Ekim Makinası','Kulaklı Anız Pulluğu','Kulaklı Traktör Pulluğu','Kültüvatör','Merdane','Ot Tırmığı','Pancar Mibzeri','Patates Dikim Makinası','Pnömatik Ekim Makinası','Rototiller','Sap Parçalama Makinası','Set Yapma Makinası','Taş Toplama Makinası','Toprak Burgusu','Toprak Frezesi (Rotovatör)','Toprak Tesviye Makinası','Traktörle Çekilen Çapa Makinaları','Traktörle Çekilen Hububat Ekim Makinası','Üniversal Ekim Makinası (Mekanik) (Pancar Mibzeri Dahil)','Üniversal Mibzer','Ürün Sınıflandırma Makinası (Selektör Hariç)',],
        'Traktörler': ['Traktörler',],
        'Yardımcı Makineler': ['Kepçe (Tarımda Kullanılan)','Römork (Tarım Arabası)',],
        'Yem Makineleri': ['Balya Makinası','Biçer Bağlar Makinası','Mısır Silaj Makinası','Ot Silaj Makinası','Saman Aktarma-Boşaltma Makinası','Sap Döver Ve Harman Makinası (Batöz)','Sap Toplamalı Saman Yapma Makinası','Tınaz Makinası'],
    },
    'Tarla Bitkileri': {
        'Ekilen Alan (Dekar)': ['Acıbakla','Adaçayı','Arpa (Biralık)','Arpa (Biralık) - Kuru','Arpa (Biralık) - Sulu','Arpa (Diğer)','Arpa (Diğer) - Kuru','Arpa (Diğer) - Sulu','Arpa (Yeşil Ot)','Aspir','Aspir - Kuru','Aspir - Sulu','Ayçiçeği (Çerezlik)','Ayçiçeği (Çerezlik) - 1.Ekiliş, Kuru','Ayçiçeği (Çerezlik) - 2.Ekiliş, Kuru','Ayçiçeği (Çerezlik) - 2.Ekiliş, Sulu','Ayçiçeği (Çerezlik) 1.Ekiliş Sulu','Ayçiçeği (Çerezlik)-1.Ekiliş','Ayçiçeği (Çerezlik)-2.Ekiliş','Ayçiçeği (Yağlık)','Ayçiçeği (Yağlık) - 1.Ekiliş, Kuru','Ayçiçeği (Yağlık) - 1.Ekiliş, Sulu','Ayçiçeği (Yağlık) - 2.Ekiliş, Kuru','Ayçiçeği (Yağlık) - 2.Ekiliş, Sulu','Ayçiçeği (Yağlık)-1. Ekiliş','Ayçiçeği (Yağlık)-2. Ekiliş','Bakla (Hayvan Yemi)','Bakla (Yemeklik)','Bezelye','Bezelye (Yemlik) (Yeşil Ot)','Börülce','Buğday (Diğer)','Buğday (Diğer) - Kuru','Buğday (Diğer) - Sulu','Buğday (Durum)','Buğday (Durum) - Kuru','Buğday (Durum) - Sulu','Buğday (Yeşil Ot)','Burçak (Dane)','Burçak (Kuru Ot)','Burçak (Yesil Ot)','Buy (Çemen Otu)','Çavdar','Çavdar (Yeşil Ot)','Çayır Otu (Yeşil Ot)','Çeltik','Çeltik - 1.Ekiliş','Çeltik - 2.Ekiliş','Darı','Elit (Şekerpancarı Tohumu)','Fasulye (Kuru)','Fasulye (Kuru) - Kuru','Fasulye (Kuru) - Sulu','Fiğ (Adi ) (Yeşil Ot)','Fiğ (Adi) (Dane)','Fiğ (Dane)','Fiğ (Diğer ) (Dane)','Fiğ (Diğer ) (Yeşil Ot)','Fiğ (Kuru Ot)','Fiğ (Macar ) (Dane)','Fiğ (Macar ) (Yeşil Ot)','Fiğ (Yeşil Ot)','Gül (Yağlık)','Haşhaş (Kapsül)','Haşhaş (Tohum)','Hayvan Pancarı','Isırgan Otu','İtalyan Çimi','Kaplıca','Kenevir (Lif)','Kenevir (Tohum)','Keten (Lif)','Keten (Tohum)','Kolza (Kanola)','Kolza (Kanola) - Kuru','Kolza (Kanola) - Sulu','Korunga (Kuru Ot)','Korunga (Tohum)','Korunga (Yeşil Ot)','Kuşyemi','Lavanta','Mahlut','Mercimek (Kırmızı)','Mercimek (Kırmızı) - Kuru','Mercimek (Kırmızı) - Sulu','Mercimek (Yeşil)','Mercimek (Yeşil) - Kuru','Mercimek (Yeşil) - Sulu','Mısır (Dane)','Mısır (Dane) - 1.Ekiliş','Mısır (Dane) - 2.Ekiliş','Mısır (Dane)-1. Ekiliş','Mısır (Dane)-2. Ekiliş','Mısır (Hasıl)','Mısır (Hasıl) - 1.Ekiliş','Mısır (Hasıl) - 2.Ekiliş','Mısır (Hasıl)-1.Ekiliş','Mısır (Hasıl)-2.Ekiliş','Mısır (Silajlık)','Mısır (Silajlık) - 1.Ekiliş','Mısır (Silajlık) - 2.Ekiliş','Mısır (Silajlık)-1.Ekiliş','Mısır (Silajlık)-2.Ekiliş','Mürdümük (Dane)','Mürdümük (Yeşil Ot)','Nohut','Nohut - Kuru','Nohut - Sulu','Oğulotu (Melissa)','Pamuk (Kütlü)','Pamuk (Kütlü) - 1.Ekiliş','Pamuk (Kütlü) - 2.Ekiliş','Pamuk (Kütlü)-1.Ekiliş','Pamuk (Kütlü)-2.Ekiliş','Pamuk (Lif)','Pamuk (Lif) - 1.Ekiliş','Pamuk (Lif) - 2.Ekiliş','Pamuk (Lif)-1.Ekiliş','Pamuk (Lif)-2.Ekiliş','Pamuk Tohumu (Çiğit)','Pamuk Tohumu (Çiğit) - 1.Ekiliş','Pamuk Tohumu (Çiğit) - 2.Ekiliş','Pamuk Tohumu (Çiğit)-1.Ekiliş','Pamuk Tohumu (Çiğit)-2.Ekiliş','Patates (Diğer)','Patates (Diğer) - 1.Ekiliş','Patates (Diğer) - 2.Ekiliş','Patates (Diğer) -1. Ekiliş','Patates (Diğer) -2. Ekiliş','Patates (Tatlı)','Patates (Tatlı) - 1.Ekiliş','Patates (Tatlı) - 2.Ekiliş','Patates (Tatlı) -1.Ekiliş','Patates (Tatlı) -2.Ekiliş','Sorgum (Dane)','Sorgum (Yeşil Ot)','Soya','Soya  - 1.Ekiliş, Kuru','Soya - 1.Ekiliş, Sulu','Soya - 2.Ekiliş, Kuru','Soya - 2.Ekiliş, Sulu','Soya-1.Ekiliş','Soya-2. Ekiliş','Susam','Susam-1. Ekiliş','Susam-1.Ekiliş','Susam-2. Ekiliş','Susam-2.Ekiliş','Şeker Kamışı','Şekerpancarı','Şerbetçiotu','Tritikale (Dane)','Tritikale (Dane) - Kuru','Tritikale (Dane) - Sulu','Tritikale (Yeşil Ot)','Tütün','Üçgül (Kuru Ot)','Üçgül (Tohum)','Üçgül (Yeşil Ot)','Yem Şalgamı','Yerelması','Yerfıstığı','Yerfıstığı - 1.Ekiliş','Yerfıstığı - 2.Ekiliş','Yerfıstığı -1.Ekiliş','Yerfıstığı -2.Ekiliş','Yonca (Kuru Ot)','Yonca (Tohum)','Yonca (Yeşil Ot)','Yulaf (Dane)','Yulaf (Dane) - Kuru','Yulaf (Dane) - Sulu','Yulaf (Yeşil Ot)',],
        'Hasat Edilen Alan (Dekar)': ['Acıbakla','Adaçayı','Arpa (Biralık)','Arpa (Biralık) - Kuru','Arpa (Biralık) - Sulu','Arpa (Diğer)','Arpa (Diğer) - Kuru','Arpa (Diğer) - Sulu','Arpa (Yeşil Ot)','Aspir','Aspir - Kuru','Aspir - Sulu','Ayçiçeği (Çerezlik)','Ayçiçeği (Çerezlik) - 1.Ekiliş, Kuru','Ayçiçeği (Çerezlik) - 2.Ekiliş, Kuru','Ayçiçeği (Çerezlik) - 2.Ekiliş, Sulu','Ayçiçeği (Çerezlik) 1.Ekiliş Sulu','Ayçiçeği (Çerezlik)-1.Ekiliş','Ayçiçeği (Çerezlik)-2.Ekiliş','Ayçiçeği (Yağlık)','Ayçiçeği (Yağlık) - 1.Ekiliş, Kuru','Ayçiçeği (Yağlık) - 1.Ekiliş, Sulu','Ayçiçeği (Yağlık) - 2.Ekiliş, Kuru','Ayçiçeği (Yağlık) - 2.Ekiliş, Sulu','Ayçiçeği (Yağlık)-1. Ekiliş','Ayçiçeği (Yağlık)-2. Ekiliş','Bakla (Hayvan Yemi)','Bakla (Yemeklik)','Bezelye','Bezelye (Yemlik) (Yeşil Ot)','Börülce','Buğday (Diğer)','Buğday (Diğer) - Kuru','Buğday (Diğer) - Sulu','Buğday (Durum)','Buğday (Durum) - Kuru','Buğday (Durum) - Sulu','Buğday (Yeşil Ot)','Burçak (Dane)','Burçak (Kuru Ot)','Burçak (Yesil Ot)','Buy (Çemen Otu)','Çavdar','Çavdar (Yeşil Ot)','Çayır Otu (Yeşil Ot)','Çeltik','Çeltik - 1.Ekiliş','Çeltik - 2.Ekiliş','Darı','Elit (Şekerpancarı Tohumu)','Fasulye (Kuru)','Fasulye (Kuru) - Kuru','Fasulye (Kuru) - Sulu','Fiğ (Adi ) (Yeşil Ot)','Fiğ (Adi) (Dane)','Fiğ (Dane)','Fiğ (Diğer ) (Dane)','Fiğ (Diğer ) (Yeşil Ot)','Fiğ (Kuru Ot)','Fiğ (Macar ) (Dane)','Fiğ (Macar ) (Yeşil Ot)','Fiğ (Yeşil Ot)','Gül (Yağlık)','Haşhaş (Kapsül)','Haşhaş (Tohum)','Hayvan Pancarı','Isırgan Otu','İtalyan Çimi','Kaplıca','Kenevir (Lif)','Kenevir (Tohum)','Keten (Lif)','Keten (Tohum)','Kolza (Kanola)','Kolza (Kanola) - Kuru','Kolza (Kanola) - Sulu','Korunga (Kuru Ot)','Korunga (Tohum)','Korunga (Yeşil Ot)','Kuşyemi','Lavanta','Mahlut','Mercimek (Kırmızı)','Mercimek (Kırmızı) - Kuru','Mercimek (Kırmızı) - Sulu','Mercimek (Yeşil)','Mercimek (Yeşil) - Kuru','Mercimek (Yeşil) - Sulu','Mısır (Dane)','Mısır (Dane) - 1.Ekiliş','Mısır (Dane) - 2.Ekiliş','Mısır (Dane)-1. Ekiliş','Mısır (Dane)-2. Ekiliş','Mısır (Hasıl)','Mısır (Hasıl) - 1.Ekiliş','Mısır (Hasıl) - 2.Ekiliş','Mısır (Hasıl)-1.Ekiliş','Mısır (Hasıl)-2.Ekiliş','Mısır (Silajlık)','Mısır (Silajlık) - 1.Ekiliş','Mısır (Silajlık) - 2.Ekiliş','Mısır (Silajlık)-1.Ekiliş','Mısır (Silajlık)-2.Ekiliş','Mürdümük (Dane)','Mürdümük (Yeşil Ot)','Nohut','Nohut - Kuru','Nohut - Sulu','Oğulotu (Melissa)','Pamuk (Kütlü)','Pamuk (Kütlü) - 1.Ekiliş','Pamuk (Kütlü) - 2.Ekiliş','Pamuk (Kütlü)-1.Ekiliş','Pamuk (Kütlü)-2.Ekiliş','Pamuk (Lif)','Pamuk (Lif) - 1.Ekiliş','Pamuk (Lif) - 2.Ekiliş','Pamuk (Lif)-1.Ekiliş','Pamuk (Lif)-2.Ekiliş','Pamuk Tohumu (Çiğit)','Pamuk Tohumu (Çiğit) - 1.Ekiliş','Pamuk Tohumu (Çiğit) - 2.Ekiliş','Pamuk Tohumu (Çiğit)-1.Ekiliş','Pamuk Tohumu (Çiğit)-2.Ekiliş','Patates (Diğer)','Patates (Diğer) - 1.Ekiliş','Patates (Diğer) - 2.Ekiliş','Patates (Diğer) -1. Ekiliş','Patates (Diğer) -2. Ekiliş','Patates (Tatlı)','Patates (Tatlı) - 1.Ekiliş','Patates (Tatlı) - 2.Ekiliş','Patates (Tatlı) -1.Ekiliş','Patates (Tatlı) -2.Ekiliş','Sorgum (Dane)','Sorgum (Yeşil Ot)','Soya','Soya  - 1.Ekiliş, Kuru','Soya - 1.Ekiliş, Sulu','Soya - 2.Ekiliş, Kuru','Soya - 2.Ekiliş, Sulu','Soya-1.Ekiliş','Soya-2. Ekiliş','Susam','Susam-1. Ekiliş','Susam-1.Ekiliş','Susam-2. Ekiliş','Susam-2.Ekiliş','Şeker Kamışı','Şekerpancarı','Şerbetçiotu','Tritikale (Dane)','Tritikale (Dane) - Kuru','Tritikale (Dane) - Sulu','Tritikale (Yeşil Ot)','Tütün','Üçgül (Kuru Ot)','Üçgül (Tohum)','Üçgül (Yeşil Ot)','Yem Şalgamı','Yerelması','Yerfıstığı','Yerfıstığı - 1.Ekiliş','Yerfıstığı - 2.Ekiliş','Yerfıstığı -1.Ekiliş','Yerfıstığı -2.Ekiliş','Yonca (Kuru Ot)','Yonca (Tohum)','Yonca (Yeşil Ot)','Yulaf (Dane)','Yulaf (Dane) - Kuru','Yulaf (Dane) - Sulu','Yulaf (Yeşil Ot)',],
        'Üretim (Ton)': ['Acıbakla','Adaçayı','Arpa (Biralık)','Arpa (Biralık) - Kuru','Arpa (Biralık) - Sulu','Arpa (Diğer)','Arpa (Diğer) - Kuru','Arpa (Diğer) - Sulu','Arpa (Yeşil Ot)','Aspir','Aspir - Kuru','Aspir - Sulu','Ayçiçeği (Çerezlik)','Ayçiçeği (Çerezlik) - 1.Ekiliş, Kuru','Ayçiçeği (Çerezlik) - 2.Ekiliş, Kuru','Ayçiçeği (Çerezlik) - 2.Ekiliş, Sulu','Ayçiçeği (Çerezlik) 1.Ekiliş Sulu','Ayçiçeği (Çerezlik)-1.Ekiliş','Ayçiçeği (Çerezlik)-2.Ekiliş','Ayçiçeği (Yağlık)','Ayçiçeği (Yağlık) - 1.Ekiliş, Kuru','Ayçiçeği (Yağlık) - 1.Ekiliş, Sulu','Ayçiçeği (Yağlık) - 2.Ekiliş, Kuru','Ayçiçeği (Yağlık) - 2.Ekiliş, Sulu','Ayçiçeği (Yağlık)-1. Ekiliş','Ayçiçeği (Yağlık)-2. Ekiliş','Bakla (Hayvan Yemi)','Bakla (Yemeklik)','Bezelye','Bezelye (Yemlik) (Yeşil Ot)','Börülce','Buğday (Diğer)','Buğday (Diğer) - Kuru','Buğday (Diğer) - Sulu','Buğday (Durum)','Buğday (Durum) - Kuru','Buğday (Durum) - Sulu','Buğday (Yeşil Ot)','Burçak (Dane)','Burçak (Kuru Ot)','Burçak (Yesil Ot)','Buy (Çemen Otu)','Çavdar','Çavdar (Yeşil Ot)','Çayır Otu (Yeşil Ot)','Çeltik','Çeltik - 1.Ekiliş','Çeltik - 2.Ekiliş','Darı','Elit (Şekerpancarı Tohumu)','Fasulye (Kuru)','Fasulye (Kuru) - Kuru','Fasulye (Kuru) - Sulu','Fiğ (Adi ) (Yeşil Ot)','Fiğ (Adi) (Dane)','Fiğ (Dane)','Fiğ (Diğer ) (Dane)','Fiğ (Diğer ) (Yeşil Ot)','Fiğ (Kuru Ot)','Fiğ (Macar ) (Dane)','Fiğ (Macar ) (Yeşil Ot)','Fiğ (Yeşil Ot)','Gül (Yağlık)','Haşhaş (Kapsül)','Haşhaş (Tohum)','Hayvan Pancarı','Isırgan Otu','İtalyan Çimi','Kaplıca','Kenevir (Lif)','Kenevir (Tohum)','Keten (Lif)','Keten (Tohum)','Kolza (Kanola)','Kolza (Kanola) - Kuru','Kolza (Kanola) - Sulu','Korunga (Kuru Ot)','Korunga (Tohum)','Korunga (Yeşil Ot)','Kuşyemi','Lavanta','Mahlut','Mercimek (Kırmızı)','Mercimek (Kırmızı) - Kuru','Mercimek (Kırmızı) - Sulu','Mercimek (Yeşil)','Mercimek (Yeşil) - Kuru','Mercimek (Yeşil) - Sulu','Mısır (Dane)','Mısır (Dane) - 1.Ekiliş','Mısır (Dane) - 2.Ekiliş','Mısır (Dane)-1. Ekiliş','Mısır (Dane)-2. Ekiliş','Mısır (Hasıl)','Mısır (Hasıl) - 1.Ekiliş','Mısır (Hasıl) - 2.Ekiliş','Mısır (Hasıl)-1.Ekiliş','Mısır (Hasıl)-2.Ekiliş','Mısır (Silajlık)','Mısır (Silajlık) - 1.Ekiliş','Mısır (Silajlık) - 2.Ekiliş','Mısır (Silajlık)-1.Ekiliş','Mısır (Silajlık)-2.Ekiliş','Mürdümük (Dane)','Mürdümük (Yeşil Ot)','Nohut','Nohut - Kuru','Nohut - Sulu','Oğulotu (Melissa)','Pamuk (Kütlü)','Pamuk (Kütlü) - 1.Ekiliş','Pamuk (Kütlü) - 2.Ekiliş','Pamuk (Kütlü)-1.Ekiliş','Pamuk (Kütlü)-2.Ekiliş','Pamuk (Lif)','Pamuk (Lif) - 1.Ekiliş','Pamuk (Lif) - 2.Ekiliş','Pamuk (Lif)-1.Ekiliş','Pamuk (Lif)-2.Ekiliş','Pamuk Tohumu (Çiğit)','Pamuk Tohumu (Çiğit) - 1.Ekiliş','Pamuk Tohumu (Çiğit) - 2.Ekiliş','Pamuk Tohumu (Çiğit)-1.Ekiliş','Pamuk Tohumu (Çiğit)-2.Ekiliş','Patates (Diğer)','Patates (Diğer) - 1.Ekiliş','Patates (Diğer) - 2.Ekiliş','Patates (Diğer) -1. Ekiliş','Patates (Diğer) -2. Ekiliş','Patates (Tatlı)','Patates (Tatlı) - 1.Ekiliş','Patates (Tatlı) - 2.Ekiliş','Patates (Tatlı) -1.Ekiliş','Patates (Tatlı) -2.Ekiliş','Sorgum (Dane)','Sorgum (Yeşil Ot)','Soya','Soya  - 1.Ekiliş, Kuru','Soya - 1.Ekiliş, Sulu','Soya - 2.Ekiliş, Kuru','Soya - 2.Ekiliş, Sulu','Soya-1.Ekiliş','Soya-2. Ekiliş','Susam','Susam-1. Ekiliş','Susam-1.Ekiliş','Susam-2. Ekiliş','Susam-2.Ekiliş','Şeker Kamışı','Şekerpancarı','Şerbetçiotu','Tritikale (Dane)','Tritikale (Dane) - Kuru','Tritikale (Dane) - Sulu','Tritikale (Yeşil Ot)','Tütün','Üçgül (Kuru Ot)','Üçgül (Tohum)','Üçgül (Yeşil Ot)','Yem Şalgamı','Yerelması','Yerfıstığı','Yerfıstığı - 1.Ekiliş','Yerfıstığı - 2.Ekiliş','Yerfıstığı -1.Ekiliş','Yerfıstığı -2.Ekiliş','Yonca (Kuru Ot)','Yonca (Tohum)','Yonca (Yeşil Ot)','Yulaf (Dane)','Yulaf (Dane) - Kuru','Yulaf (Dane) - Sulu','Yulaf (Yeşil Ot)',],
        'Verim (Kg/Da)': ['Acıbakla','Adaçayı','Arpa (Biralık)','Arpa (Biralık) - Kuru','Arpa (Biralık) - Sulu','Arpa (Diğer)','Arpa (Diğer) - Kuru','Arpa (Diğer) - Sulu','Arpa (Yeşil Ot)','Aspir','Aspir - Kuru','Aspir - Sulu','Ayçiçeği (Çerezlik)','Ayçiçeği (Çerezlik) - 1.Ekiliş, Kuru','Ayçiçeği (Çerezlik) - 2.Ekiliş, Kuru','Ayçiçeği (Çerezlik) - 2.Ekiliş, Sulu','Ayçiçeği (Çerezlik) 1.Ekiliş Sulu','Ayçiçeği (Çerezlik)-1.Ekiliş','Ayçiçeği (Çerezlik)-2.Ekiliş','Ayçiçeği (Yağlık)','Ayçiçeği (Yağlık) - 1.Ekiliş, Kuru','Ayçiçeği (Yağlık) - 1.Ekiliş, Sulu','Ayçiçeği (Yağlık) - 2.Ekiliş, Kuru','Ayçiçeği (Yağlık) - 2.Ekiliş, Sulu','Ayçiçeği (Yağlık)-1. Ekiliş','Ayçiçeği (Yağlık)-2. Ekiliş','Bakla (Hayvan Yemi)','Bakla (Yemeklik)','Bezelye','Bezelye (Yemlik) (Yeşil Ot)','Börülce','Buğday (Diğer)','Buğday (Diğer) - Kuru','Buğday (Diğer) - Sulu','Buğday (Durum)','Buğday (Durum) - Kuru','Buğday (Durum) - Sulu','Buğday (Yeşil Ot)','Burçak (Dane)','Burçak (Yesil Ot)','Buy (Çemen Otu)','Çavdar','Çavdar (Yeşil Ot)','Çayır Otu (Yeşil Ot)','Çeltik','Çeltik - 1.Ekiliş','Çeltik - 2.Ekiliş','Darı','Elit (Şekerpancarı Tohumu)','Fasulye (Kuru)','Fasulye (Kuru) - Kuru','Fasulye (Kuru) - Sulu','Fiğ (Adi ) (Yeşil Ot)','Fiğ (Adi) (Dane)','Fiğ (Dane)','Fiğ (Diğer ) (Dane)','Fiğ (Diğer ) (Yeşil Ot)','Fiğ (Macar ) (Dane)','Fiğ (Macar ) (Yeşil Ot)','Fiğ (Yeşil Ot)','Gül (Yağlık)','Haşhaş (Kapsül)','Haşhaş (Tohum)','Hayvan Pancarı','Isırgan Otu','İtalyan Çimi','Kaplıca','Kenevir (Lif)','Kenevir (Tohum)','Keten (Lif)','Keten (Tohum)','Kolza (Kanola)','Kolza (Kanola) - Kuru','Kolza (Kanola) - Sulu', 'Korunga (Tohum)','Korunga (Yeşil Ot)','Kuşyemi','Lavanta','Mahlut','Mercimek (Kırmızı)','Mercimek (Kırmızı) - Kuru','Mercimek (Kırmızı) - Sulu','Mercimek (Yeşil)','Mercimek (Yeşil) - Kuru','Mercimek (Yeşil) - Sulu','Mısır (Dane)','Mısır (Dane) - 1.Ekiliş','Mısır (Dane) - 2.Ekiliş','Mısır (Dane)-1. Ekiliş','Mısır (Dane)-2. Ekiliş','Mısır (Hasıl)','Mısır (Hasıl) - 1.Ekiliş','Mısır (Hasıl) - 2.Ekiliş','Mısır (Hasıl)-1.Ekiliş','Mısır (Hasıl)-2.Ekiliş','Mısır (Silajlık)','Mısır (Silajlık) - 1.Ekiliş','Mısır (Silajlık) - 2.Ekiliş','Mısır (Silajlık)-1.Ekiliş','Mısır (Silajlık)-2.Ekiliş','Mürdümük (Dane)','Mürdümük (Yeşil Ot)','Nohut','Nohut - Kuru','Nohut - Sulu','Oğulotu (Melissa)','Pamuk (Kütlü)','Pamuk (Kütlü) - 1.Ekiliş','Pamuk (Kütlü) - 2.Ekiliş','Pamuk (Kütlü)-1.Ekiliş','Pamuk (Kütlü)-2.Ekiliş','Pamuk (Lif)','Pamuk (Lif) - 1.Ekiliş','Pamuk (Lif) - 2.Ekiliş','Pamuk (Lif)-1.Ekiliş','Pamuk (Lif)-2.Ekiliş','Pamuk Tohumu (Çiğit)','Pamuk Tohumu (Çiğit) - 1.Ekiliş','Pamuk Tohumu (Çiğit) - 2.Ekiliş','Pamuk Tohumu (Çiğit)-1.Ekiliş','Pamuk Tohumu (Çiğit)-2.Ekiliş','Patates (Diğer)','Patates (Diğer) - 1.Ekiliş','Patates (Diğer) - 2.Ekiliş','Patates (Diğer) -1. Ekiliş','Patates (Diğer) -2. Ekiliş','Patates (Tatlı)','Patates (Tatlı) - 1.Ekiliş','Patates (Tatlı) - 2.Ekiliş','Patates (Tatlı) -1.Ekiliş','Patates (Tatlı) -2.Ekiliş','Sorgum (Dane)','Sorgum (Yeşil Ot)','Soya','Soya  - 1.Ekiliş, Kuru','Soya - 1.Ekiliş, Sulu','Soya - 2.Ekiliş, Kuru','Soya - 2.Ekiliş, Sulu','Soya-1.Ekiliş','Soya-2. Ekiliş','Susam','Susam-1. Ekiliş','Susam-1.Ekiliş','Susam-2. Ekiliş','Susam-2.Ekiliş','Şeker Kamışı','Şekerpancarı','Şerbetçiotu','Tritikale (Dane)','Tritikale (Dane) - Kuru','Tritikale (Dane) - Sulu','Tritikale (Yeşil Ot)','Tütün', 'Üçgül (Tohum)','Üçgül (Yeşil Ot)','Yem Şalgamı','Yerelması','Yerfıstığı','Yerfıstığı - 1.Ekiliş','Yerfıstığı - 2.Ekiliş','Yerfıstığı -1.Ekiliş','Yerfıstığı -2.Ekiliş', 'Yonca (Tohum)','Yonca (Yeşil Ot)','Yulaf (Dane)','Yulaf (Dane) - Kuru','Yulaf (Dane) - Sulu','Yulaf (Yeşil Ot)'],
    },

}

# all_options2 = {
#     'TR21-TRAKYA-(EDIRNE, KIRKLARELI, TEKIRDAG)':{'EDIRNE':['EDIRNE','ENEZ','HAVSA','IPSALA','KESAN','LALAPASA','MERIC','SULOGLU','UZUNKOPRU',],'KIRKLARELI':['BABAESKI','DEMIRKOY','KIRLARELI','KOFCAZ','LULEBURGAZ','PEHLIVANKOY','PINARHISAR','VIZE',],'TEKIRDAG':['CERKEZKOY','CORLU','ERGENE','HAYRABOLU','KAPAKLI','MALKARA','MARMARA EREGLISI','MURATLI','SARAY','SARKOY','SULEYMANPASA',]},
#     'TR10-ISTANBUL-(ISTANBUL)':{'ISTANBUL':['ADALAR','ARNAVUTKOY','ATASEHIR','AVCILAR','BAGCILAR','BAHCELIEVLER','BAKIRKOY','BASAKSEHIR','BAYRAMPASA','BESIKTAS','BEYKOZ','BEYLIKDUZU','BEYOGLU','BUYUKCEKMECE','CATALCA','CEKMEKOY','ESENLER','ESENYURT','EYUPSULTAN','FATIH','GAZIOSMANPASA','GUNGOREN','KADIKOY','KAGITHANE','KARTAL','KUCUKCEKMECE','MALTEPE','PENDIK','SANCAKTEPE','SARIYER','SILE','SILIVRI','SISLI','SULTANBEYLI','SULTANGAZI','TUZLA','UMRANIYE','USKUDAR','ZEYTINBURNU',]},
#     'TR22-GUNEY MARMARA-(BALIKESIR, CANAKKALE)':{'BALIKESIR':['ALTIEYLUL','AYVALIK','BALYA','BANDIRMA','BIGADIC','BURHANIYE','DURSUNBEY','EDREMIT','ERDEK','GOMEC','GONEN','HAVRAN','IVRINDI','KARESI','KEPSUT','MANYAS','MARMARA','SAVASTEPE','SINDIRGI','SUSURLUK',],'CANAKKALE':['AYVACIK','BAYRAMIC','BIGA','BOZCAADA','CAN','CANAKKALE','ECEABAT','EZINE','GELIBOLU','GOKCEADA','LAPSEKI','YENICE',]},
#     'TR31-IZMIR-(IZMIR)':{'IZMIR':['ALIAGA','BALCOVA','BAYINDIR','BAYRAKLI','BERGAMA','BEYDAG','BORNOVA','BUCA','CESME','CIGLI','DIKILI','FOCA','GAZIEMIR','GUZELBAHCE','KARABAGLAR','KARABURUN','KARSIYAKA','KEMALPASA','KINIK','KIRAZ','KONAK','MENDERES','MENEMEN','NARLIDERE','ODEMIS','SEFERIHISAR','SELCUK','TIRE','TORBALI','URLA',]},
#     'TR32-GUNEY EGE-(AYDIN, DENIZLI, MUGLA)':{'AYDIN':['BOZDOGAN','BUHARKENT','CINE','DIDIM','EFELER','GERMENCIK','INCIRLIOVA','KARACASU','KARPUZLU','KOCARLI','KOSK','KUSADASI','KUYUCAK','NAZILLI','SOKE','SULTANHISAR','YENIPAZAR',],'DENIZLI':['ACIPAYAM','BABADAG','BAKLAN','BEKILLI','BEYAGAC','BOZKURT','BULDAN','CAL','CAMELI','CARDAK','CIVRIL','GUNEY','HONAZ','KALE','MERKEZEFENDI','PAMUKKALE','SARAYKOY','SERINHISAR','TAVAS',],'MUGLA':['BODRUM','DALAMAN','DATCA','FETHIYE','KAVAKLIDERE','KOYCEGIZ','MARMARIS','MENTESE','MILAS','ORTACA','SEYDIKEMER','ULA','YATAGAN',]},
#     'TR33-ZAFER-(AFYONKARAHISAR, KUTAHYA, MANISA, USAK)':{'AFYONKARAHISAR':['AFYONKARAHISAR','BASMAKCI','BAYAT','BOLVADIN','CAY','COBANLAR','DAZKIRI','DINAR','EMIRDAG','EVCILER','HOCALAR','IHSANIYE','ISCEHISAR','KIZILOREN','SANDIKLI','SINANPASA','SUHUT','SULTANDAGI',],'KUTAHYA':['ALTINTAS','ASLANAPA','CAVDARHISAR','DOMANIC','DUMLUPINAR','EMET','GEDIZ','HISARCIK','KUTAHYA','PAZARLAR','SAPHANE','SIMAV','TAVSANLI',],'MANISA':['AHMETLI','AKHISAR','ALASEHIR','DEMIRCI','GOLMARMARA','GORDES','KIRKAGAC','KOPRUBASI','KULA','SALIHLI','SARIGOL','SARUHANLI','SEHZADELER','SELENDI','SOMA','TURGUTLU','YUNUSEMRE',],'USAK':['BANAZ','ESME','KARAHALLI','SIVASLI','ULUBEY','USAK',]},
#     'TR41-BURSA, ESKISEHIR, BILECIK':{'BILECIK':['BILECIK','BOZUYUK','GOLPAZARI','INHISAR','OSMANELI','PAZARYERI','SOGUT','YENIPAZAR',],'BURSA':['BUYUKORHAN','GEMLIK','GURSU','HARMANCIK','INEGOL','IZNIK','KARACABEY','KELES','KESTEL','MUDANYA','MUSTAFAKEMALPASA','NILUFER','ORHANELI','ORHANGAZI','OSMANGAZI','YENISEHIR','YILDIRIM',],'ESKISEHIR':['ALPU','BEYLIKOVA','CIFTELER','GUNYUZU','HAN','INONU','MAHMUDIYE','MIHALGAZI','MIHALICCIK','ODUNPAZARI','SARICAKAYA','SEYITGAZI','SIVRIHISAR','TEPEBASI',]},
#     'TR42-DOGU MARMARA-(BOLU, DUZCE, KOCAELI, SAKARYA, YALOVA)':{'BOLU':['BOLU','DORTDIVAN','GEREDE','GOYNUK','KIBRISCIK','MENGEN','MUDURNU','SEBEN','YENICAGA',],'DUZCE':['AKCAKOCA','CILIMLI','CUMAYERI','DUZCE','GOLYAKA','GUMUSOVA','KAYNASLI','YIGILCA',],'KOCAELI':['BASISKELE','CAYIROVA','DARICA','DERINCE','DILOVASI','GEBZE','GOLCUK','IZMIT','KANDIRA','KARAMURSEL','KARTEPE','KORFEZ',],'SAKARYA':['ADAPAZARI','AKYAZI','ARIFIYE','ERENLER','FERIZLI','GEYVE','HENDEK','KARAPURCEK','KARASU','KAYNARCA','KOCAALI','PAMUKOVA','SAPANCA','SERDIVAN','SOGUTLU','TARAKLI',],'YALOVA':['ALTINOVA','ARMUTLU','CIFTLIKKOY','CINARCIK','TERMAL','YALOVA',]},
#     'TR51-ANKARA-(ANKARA)':{'ANKARA':['AKYURT','ALTINDAG','AYAS','BALA','BEYPAZARI','CAMLIDERE','CANKAYA','CUBUK','ELMADAG','ETIMESGUT','EVREN','GOLBASI','GUDUL','HAYMANA','KAHRAMANKAZAN','KALECIK','KECIOREN','KIZILCAHAMAM','MAMAK','NALLIHAN','POLATLI','PURSAKLAR','SEREFLIKOCHISAR','SINCAN','YENIMAHALLE',]},
#     'TR52-MEVLANA-(KARAMAN, KONYA)':{'KARAMAN':['AYRANCI','BASYAYLA','ERMENEK','KARAMAN','KAZIMKARABEKIR','SARIVELILER',],'KONYA':['AHIRLI','AKOREN','AKSEHIR','ALTINEKIN','BEYSEHIR','BOZKIR','CELTIK','CIHANBEYLI','CUMRA','DERBENT','DEREBUCAK','DOGANHISAR','EMIRGAZI','EREGLI','GUNEYSINIR','HADIM','HALKAPINAR','HUYUK','ILGIN','KADINHANI','KARAPINAR','KARATAY','KULU','MERAM','SARAYONU','SELCUKLU','SEYDISEHIR','TASKENT','TUZLUKCU','YALIHUYUK','YUNAK',]},
#     'TR61-BATI KARADENIZ-(ANTALYA, BURDUR, ISPARTA)':{'ANTALYA':['AKSEKI','AKSU','ALANYA','DEMRE','DOSEMEALTI','ELMALI','FINIKE','GAZIPASA','GUNDOGMUS','IBRADI','KAS','KEMER','KEPEZ','KONYAALTI','KORKUTELI','KUMLUCA','MANAVGAT','MURATPASA','SERIK',],'BURDUR':['AGLASUN','ALTINYAYLA','BUCAK','BURDUR','CAVDIR','CELTIKCI','GOLHISAR','KARAMANLI','KEMER','TEFENNI','YESILOVA',],'ISPARTA':['AKSU','ATABEY','EGIRDIR','GELENDOST','GONEN','ISPARTA','KECIBORLU','SARKIKARAAGAC','SENIRKENT','SUTCULER','ULUBORLU','YALVAC','YENISARBADEMLI',]},
#     'TR62-CUKUROVA-(ADANA, MERSIN)':{'ADANA':['ALADAG','CEYHAN','CUKUROVA','FEKE','IMAMOGLU','KARAISALI','KARATAS','KOZAN','POZANTI','SAIMBEYLI','SARICAM','SEYHAN','TUFANBEYLI','YUMURTALIK','YUREGIR',],'MERSIN':['AKDENIZ','ANAMUR','AYDINCIK','BOZYAZI','CAMLIYAYLA','ERDEMLI','GULNAR','MEZITLI','MUT','SILIFKE','TARSUS','TOROSLAR','YENISEHIR',]},
#     'TR63-DOGU AKDENIZ-(HATAY, KAHRAMANMARAS, OSMANIYE)':{'HATAY':['ALTINOZU','ANTAKYA','ARSUZ','BELEN','DEFNE','DORTYOL','ERZIN','HASSA','ISKENDERUN','KIRIKHAN','KUMLU','PAYAS','REYHANLI','SAMANDAG','YAYLADAGI',],'KAHRAMANMARAS':['AFSIN','ANDIRIN','CAGLAYANCERIT','DULKADIROGLU','EKINOZU','ELBISTAN','GOKSUN','NURHAK','ONIKISUBAT','PAZARCIK','TURKOGLU',],'OSMANIYE':['BAHCE','DUZICI','HASANBEYLI','KADIRLI','OSMANIYE','SUMBAS','TOPRAKKALE',]},
#     'TR71-AHILER-(AKSARAY, KIRIKKALE, KIRSEHIR, NIGDE, NEVSEHIR)':{'AKSARAY':['AGACOREN','AKSARAY','ESKIL','GULAGAC','GUZELYURT','ORTAKOY','SARIYAHSI','SULTANHANI',],'KIRIKKALE':['BAHSILI','BALISEYH','CELEBI','DELICE','KARAKECILI','KESKIN','KIRIKKALE','SULAKYURT','YAHSIHAN',],'KIRSEHIR':['AKCAKENT','AKPINAR','BOZTEPE','CICEKDAGI','KAMAN','KIRSEHIR','MUCUR',],'NEVSEHIR':['ACIGOL','AVANOS','DERINKUYU','GULSEHIR','HACIBEKTAS','KOZAKLI','NEVSEHIR','URGUP',],'NIGDE':['ALTUNHISAR','BOR','CAMARDI','CIFTLIK','NIGDE','ULUKISLA',]},
#     'TR72-ORTA ANADOLU-(KAYSERI, SIVAS, YOZGAT)':{'KAYSERI':['AKKISLA','BUNYAN','DEVELI','FELAHIYE','HACILAR','INCESU','KOCASINAN','MELIKGAZI','OZVATAN','PINARBASI','SARIOGLAN','SARIZ','TALAS','TOMARZA','YAHYALI','YESILHISAR',],'SIVAS':['AKINCILAR','ALTINYAYLA','DIVRIGI','DOGANSAR','GEMEREK','GOLOVA','GURUN','HAFIK','IMRANLI','KANGAL','KOYULHISAR','SARKISLA','SIVAS','SUSEHRI','ULAS','YILDIZELI','ZARA',],'YOZGAT':['AKDAGMADENI','AYDINCIK','BOGAZLIYAN','CANDIR','CAYIRALAN','CEKEREK','KADISEHRI','SARAYKENT','SARIKAYA','SEFAATLI','SORGUN','YENIFAKILI','YERKOY','YOZGAT',]},
#     'TR81-BATI KARADENIZ-(BARTIN, KARABUK, ZONGULDAK)':{'BARTIN':['AMASRA','BARTIN','KURUCASILE','ULUS',],'KARABUK':['EFLANI','ESKIPAZAR','KARABUK','OVACIK','SAFRANBOLU','YENICE',],'ZONGULDAK':['ALAPLI','CAYCUMA','DEVREK','EREGLI','GOKCEBEY','KILIMLI','KOZLU','ZONGULDAK',]},
#     'TR82-KUZEY ANADOLU-(CANKIRI, KASTAMONU, SINOP)':{'CANKIRI':['ATKARACALAR','BAYRAMOREN','CANKIRI','CERKES','ELDIVAN','ILGAZ','KIZILIRMAK','KORGUN','KURSUNLU','ORTA','SABANOZU','YAPRAKLI',],'KASTAMONU':['ABANA','AGLI','ARAC','AZDAVAY','BOZKURT','CATALZEYTIN','CIDE','DADAY','DEVREKANI','DOGANYURT','HANONU','IHSANGAZI','INEBOLU','KASTAMONU','KURE','PINARBASI','SENPAZAR','SEYDILER','TASKOPRU','TOSYA',],'SINOP':['AYANCIK','BOYABAT','DIKMEN','DURAGAN','ERFELEK','GERZE','SARAYDUZU','SINOP','TURKELI',]},
#     'TR83-ORTA KARADENIZ-(AMASYA, CORUM, SAMSUN, TOKAT)':{'AMASYA':['AMASYA','GOYNUCEK','GUMUSHACIKOY','HAMAMOZU','MERZIFON','SULUOVA','TASOVA',],'CORUM':['ALACA','BAYAT','BOGAZKALE','CORUM','DODURGA','ISKILIP','KARGI','LACIN','MECITOZU','OGUZLAR','ORTAKOY','OSMANCIK','SUNGURLU','UGURLUDAG',],'SAMSUN':['19 MAYIS','ALACAM','ASARCIK','ATAKUM','AYVACIK','BAFRA','CANIK','CARSAMBA','HAVZA','ILKADIM','KAVAK','LADIK','SALIPAZARI','TEKKEKOY','TERME','VEZIRKOPRU','YAKAKENT',],'TOKAT':['ALMUS','ARTOVA','BASCIFTLIK','ERBAA','NIKSAR','PAZAR','RESADIYE','SULUSARAY','TOKAT','TURHAL','YESILYURT','ZILE',]},
#     'TR90-DOGU KARADENIZ-(ARTVIN, GIRESUN, GUMUSHANE, ORDU, RIZE, TRABZON)':{'ARTVIN':['ARDANUC','ARHAVI','ARTVIN','BORCKA','HOPA','KEMALPASA','MURGUL','SAVSAT','YUSUFELI',],'GIRESUN':['ALUCRA','BULANCAK','CAMOLUK','CANAKCI','DERELI','DOGANKENT','ESPIYE','EYNESIL','GIRESUN','GORELE','GUCE','KESAP','PIRAZIZ','SEBINKARAHISAR','TIREBOLU','YAGLIDERE',],'GUMUSHANE':['GUMUSHANE','KELKIT','KOSE','KURTUN','SIRAN','TORUL',],'ORDU':['AKKUS','ALTINORDU','AYBASTI','CAMAS','CATALPINAR','CAYBASI','FATSA','GOLKOY','GULYALI','GURGENTEPE','IKIZCE','KABADUZ','KABATAS','KORGAN','KUMRU','MESUDIYE','PERSEMBE','ULUBEY','UNYE',],'RIZE':['ARDESEN','CAMLIHEMSIN','CAYELI','DEREPAZARI','FINDIKLI','GUNEYSU','HEMSIN','IKIZDERE','IYIDERE','KALKANDERE','PAZAR','RIZE',],'TRABZON':['AKCAABAT','ARAKLI','ARSIN','BESIKDUZU','CARSIBASI','CAYKARA','DERNEKPAZARI','DUZKOY','HAYRAT','KOPRUBASI','MACKA','OF','ORTAHISAR','SALPAZARI','SURMENE','TONYA','VAKFIKEBIR','YOMRA',]},
#     'TRA1-KUZEY DOGU ANADOLU-(BAYBURT, ERZINCAN, ERZURUM)':{'BAYBURT':['AYDINTEPE','BAYBURT','DEMIROZU',],'ERZINCAN':['CAYIRLI','ERZINCAN','ILIC','KEMAH','KEMALIYE','OTLUKBELI','REFAHIYE','TERCAN','UZUMLU',],'ERZURUM':['ASKALE','AZIZIYE','CAT','HINIS','HORASAN','ISPIR','KARACOBAN','KARAYAZI','KOPRUKOY','NARMAN','OLTU','OLUR','PALANDOKEN','PASINLER','PAZARYOLU','SENKAYA','TEKMAN','TORTUM','UZUNDERE','YAKUTIYE',]},
#     'TRA2-SERHAT-(AGRI, ARDAHAN, IGDIR, KARS)':{'AGRI':['AGRI','DIYADIN','DOGUBAYAZIT','ELESKIRT','HAMUR','PATNOS','TASLICAY','TUTAK',],'ARDAHAN':['ARDAHAN','CILDIR','DAMAL','GOLE','HANAK','POSOF',],'IGDIR':['ARALIK','IGDIR','KARAKOYUNLU','TUZLUCA',],'KARS':['AKYAKA','ARPACAY','DIGOR','KAGIZMAN','KARS','SARIKAMIS','SELIM','SUSUZ',]},
#     'TRB1-FIRAT-(BINGOL, ELAZIG, MALATYA, TUNCELI)':{'BINGOL':['ADAKLI','BINGOL','GENC','KARLIOVA','KIGI','SOLHAN','YAYLADERE','YEDISU',],'ELAZIG':['AGIN','ALACAKAYA','ARICAK','BASKIL','ELAZIG','KARAKOCAN','KEBAN','KOVANCILAR','MADEN','PALU','SIVRICE',],'MALATYA':['AKCADAG','ARAPGIR','ARGUVAN','BATTALGAZI','DARENDE','DOGANSEHIR','DOGANYOL','HEKIMHAN','KALE','KULUNCAK','PUTURGE','YAZIHAN','YESILYURT',],'TUNCELI':['CEMISGEZEK','HOZAT','MAZGIRT','NAZIMIYE','OVACIK','PERTEK','PULUMUR','TUNCELI',]},
#     'TRB2-DOGU ANADOLU-(BITLIS, HAKKÂRI, MUS, VAN)':{'BITLIS':['ADILCEVAZ','AHLAT','BITLIS','GUROYMAK','HIZAN','MUTKI','TATVAN',],'HAKKARI':['CUKURCA','DERECIK','HAKKARI','SEMDINLI','YUKSEKOVA',],'MUS':['BULANIK','HASKOY','KORKUT','MALAZGIRT','MUS','VARTO',],'VAN':['BAHCESARAY','BASKALE','CALDIRAN','CATAK','EDREMIT','ERCIS','GEVAS','GURPINAR','IPEKYOLU','MURADIYE','OZALP','SARAY','TUSBA',]},
#     'TRC1-IPEKYOLU-(ADIYAMAN, GAZIANTEP, KILIS)':{'ADIYAMAN':['ADIYAMAN','BESNI','CELIKHAN','GERGER','GOLBASI','KAHTA','SAMSAT','SINCIK','TUT',],'GAZIANTEP':['ARABAN','ISLAHIYE','KARKAMIS','NIZIP','NURDAGI','OGUZELI','SAHINBEY','SEHITKAMIL','YAVUZELI',],'KILIS':['ELBEYLI','KILIS','MUSABEYLI','POLATELI',]},
#     'TRC2-KARACADAG-(DIYARBAKIR, SANLIURFA)':{'DIYARBAKIR':['BAGLAR','BISMIL','CERMIK','CINAR','CUNGUS','DICLE','EGIL','ERGANI','HANI','HAZRO','KAYAPINAR','KOCAKOY','KULP','LICE','SILVAN','SUR','YENISEHIR',],'SANLIURFA':['AKCAKALE','BIRECIK','BOZOVA','CEYLANPINAR','EYYUBIYE','HALFETI','HALILIYE','HARRAN','HILVAN','KARAKOPRU','SIVEREK','SURUC','VIRANSEHIR',]},
#     'TRC3-DICLE-(BATMAN, MARDIN, SIRNAK, SIIRT)':{'BATMAN':['BATMAN','BESIRI','GERCUS','HASANKEYF','KOZLUK','SASON',],'MARDIN':['ARTUKLU','DARGECIT','DERIK','KIZILTEPE','MAZIDAGI','MIDYAT','NUSAYBIN','OMERLI','SAVUR','YESILLI',],'SIIRT':['BAYKAN','ERUH','KURTALAN','PERVARI','SIIRT','SIRVAN','TILLO',],'SIRNAK':['BEYTUSSEBAP','CIZRE','GUCLUKONAK','IDIL','SILOPI','SIRNAK','ULUDERE',]
#     },
# }

layout = dbc.Container([

    dbc.Row([
        dbc.Col([
            html.H5('Ulusal İlçe Verileri-Grafik Gösterimi',
                className='text-center text-primary font-weight-bold'),
        ],xl=12),

        dbc.Col([
            html.H5("Aranan Veri",
                    className='text-start text-primary mr-4'),
            dcc.Dropdown(
                id='countries-dropdown12',clearable=False,
                persistence=True, persistence_type='session',
                options=[{'label': k, 'value': k} for k in all_options.keys()],
                value='Nüfus'
                ),

            dcc.Dropdown(id='cities-dropdown12', value='Nüfus',clearable=False,
                persistence=True, persistence_type='session',),

            dcc.Dropdown(id='landmarks-dropdown12',clearable=False,
                persistence=True, persistence_type='session',),

            html.H6(id='display-selected-values12',
                    className='text-start text-danger font-weight-bold mt-3 ml-1'),
        ],
            xs=12, sm=12, md=12, lg=12, xl=12
        ),

        dbc.Col([
            # html.Hr(),
            dcc.Slider(id = 'slider_year12',
                       included = True,
                       updatemode='drag',
                       tooltip={'always_visible': True},
                       min = 1991,
                       max = 2021,
                       step = 1,
                       value = 2020,
                       marks = {str(yr): str(yr) for yr in range(1991, 2022, 1)},
                       className = 'dcc_compon',
                       persistence=True, persistence_type='session',),
        ],
           xs=12, sm=12, md=12, lg=12, xl=12,
        ),
    ],
        style={"position": "fixed",
             "z-index": "999", "background": "#EDF0F6",
             "width": "100%",
                },
    ),

    html.Br(),

    # dbc.Row([
    #     dbc.Col([
    #         dcc.Graph(id='my_bee_map1', figure={},
    #                   ),
    #     ],
    #        xs=12, sm=12, md=12, lg=11, xl=11
    #     )
    # ], align="center",style={'marginTop': 220}),

    # html.Hr(),

    dbc.Row([

        dbc.Col([
            html.H5("Bar Grafiği",
                    className='text-start text-primary mr-4'),
            dcc.Graph(id='bar_graph12', figure={}),
        ],
           xs=12, sm=12, md=12, lg=12, xl=12
        ),

    ], align="center",style={'marginTop': 240}),

    html.Hr(),

    dbc.Row([

        dbc.Col([
            html.H5("Ağaç Haritası",
                    className='text-start text-primary mr-4'),
            dcc.Graph(id='tree_map12', figure={},
                      ),
        ],
           xs=12, sm=12, md=12, lg=12, xl=12
        )
    ], align="start"),

    html.Hr(),

    # dbc.Row([

    #     dbc.Col([
    #         html.H5("Saçılım Grafiği",
    #                 className='text-start text-primary mr-4'),
    #         dcc.Graph(id='polinom_graph', figure={}),
    #     ],
    #        xs=12, sm=12, md=12, lg=12, xl=12
    #     ),

    # ], align="start"),

    # dbc.Row([

    #     dbc.Col([

    #         html.H5("X Ekseni",
    #                 className='text-right text-primary mt-4'),
    #     ],
    #        xs=12, sm=12, md=12, lg=2, xl=2
    #     ),

    #     dbc.Col([

    #         dcc.Dropdown(
    #             id='countries-dropdown1',
    #             options=[{'label': k, 'value': k} for k in all_options.keys()],
    #             value='Nüfus'
    #             ),

    #         dcc.Dropdown(id='cities-dropdown1', value='Nüfus'),

    #         dcc.Dropdown(id='landmarks-dropdown1'),

    #     ],
    #        xs=12, sm=12, md=12, lg=7, xl=7
    #     ),
    # ],
    #     style={
    #         # "position": "fixed",
    #         "z-index": "999", "background": "#EDF0F6",
    #         "width": "99%",
    #     },
    # # no_gutters=False, justify='start'
    # ),

    # html.Hr(),

    ## 3'lü sıralı Bölge, İl, İlçe Dropdown
    # dbc.Row([

    #     dbc.Col([
    #         html.H5("Bölge, İl, İlçe Seçimi",
    #                 className='text-start text-primary mr-4'),
    #         dcc.Dropdown(
    #             id='countries-dropdown2',
    #             options=[{'label': k, 'value': k} for k in all_options2.keys()],
    #             value='TR21-TRAKYA-(EDIRNE, KIRKLARELI, TEKIRDAG)'
    #             ),

    #         dcc.Dropdown(id='cities-dropdown2', value='EDIRNE'),

    #         dcc.Dropdown(id='landmarks-dropdown2'),
    #         html.Br()

    #     ],
    #        xs=12, sm=12, md=12, lg=12, xl=12
    #     ),
    # ],
    #     style={
    #         # "position": "fixed",
    #         "z-index": "999", "background": "#EDF0F6",
    #         "width": "99%",
    #     },
    # ),
#     dbc.Row([

#         dbc.Col([
#             html.H5("Bölge ve İl Seçimi",
#                     className='text-start text-primary mr-4'),
#             dcc.Dropdown(
#                 id='countries-dropdown2',
#                 options=[{'label': k, 'value': k} for k in all_options2.keys()],
#                 value='TR21-TRAKYA-(EDIRNE, KIRKLARELI, TEKIRDAG)',
#                 multi=True,
#                 placeholder="Bölge Seçiniz",
#                 searchable=False
#                 # clearable=False,
#                 ),

#             dcc.Dropdown(id='cities-dropdown2',multi=True,
#             value='EDIRNE',
#             placeholder="İl Seçiniz",
#             searchable=False
#             # clearable=False,
# ),
#         ],
#            xs=12, sm=12, md=12, lg=12, xl=12
#         ),
#     ],
#         style={
#             # "position": "fixed",
#             "z-index": "999", "background": "#EDF0F6",
#             "width": "99%",
#         },
#     ),

#     html.Br(),

    # dbc.Row([

    #     dbc.Col([
    #         html.H5("İlçe Trend Grafiği",
    #                 className='text-start text-primary mr-4'),
    #         dcc.Graph(id='trend_ilce', figure={}),
    #     ],
    #        xs=12, sm=12, md=12, lg=12, xl=12
    #     ),

    # ], align="center"),

    # # html.Hr(),

    # dbc.Row([

    #     dbc.Col([
    #         html.Label(['* Tek ilçe veya tamamını seçmek için çift tıklayınız',], className="font-weight-bold text-dark"),
    #             ],
    #        xs=12, sm=12, md=12, lg=4, xl=4
    #     ),
    #     dbc.Col([
    #         html.Label(['* Yeni bir ilçe eklemek veya çıkarmak için tek tıklayınız',], className="font-weight-bold text-dark"),
    #             ],
    #        xs=12, sm=12, md=12, lg=4, xl=4
    #     ),
    # ], no_gutters=False, justify='center'),

    # html.Hr(),

    # dbc.Row([

    #     dbc.Col([
    #         html.H5("İl Bar Grafiği",
    #                 className='text-start text-primary mr-4'),
    #         dcc.Graph(id='bar_graph_il', figure={}),
    #     ],
    #        xs=12, sm=12, md=12, lg=12, xl=12
    #     ),

    # ], align="center"),

    # html.Hr(),

    # dbc.Row([

    #     dbc.Col([
    #         html.H5("Bölgesel Bar Grafiği",
    #                 className='text-start text-primary mr-4'),
    #         dcc.Graph(id='bar_graph_bolge', figure={}),
    #     ],
    #        xs=12, sm=12, md=12, lg=12, xl=12
    #     ),

    # ], align="center"),

    # html.Hr(),

    # dbc.Row([

    #     dbc.Col([
    #         html.H5("Bölgesel Ağaç Haritası",
    #                 className='text-start text-primary mr-4'),
    #         dcc.Graph(id='tree_map_bolgesel', figure={},
    #                   ),
    #     ],
    #        xs=12, sm=12, md=12, lg=12, xl=12
    #     )
    # ], align="start"),

    # html.Hr(),

    dbc.Row([

        dbc.Col([
            html.Label(['* Tüm istatistikler Türkiye İstatistik Kurumu(TÜİK) veritabanından derlenmiştir',],
                        className="font-weight-bold text-dark"
                       )
        ],
           xs=12, sm=12, md=12, lg=12, xl=12
        ),
    ], no_gutters=False, justify='start'),

    html.Hr(),

    dbc.Row([

        dbc.Col([
            html.Button("Tüm veritabanını CSV olarak indir", id="btn_csv112"),
            dcc.Download(id="download-dataframe-csv112"),
        ],
            xs=12, sm=12, md=12, lg=3, xl=3
        ),

        dbc.Col([
            html.Button("Yerleşim yerleri belgesini CSV olarak indir", id="btn_csv212"),
            dcc.Download(id="download-dataframe-csv212"),
        ],
            xs=12, sm=12, md=12, lg=3, xl=3
        ),

        dbc.Col([
            html.Button("Metaveri belgesini CSV olarak indir", id="btn_csv312"),
            dcc.Download(id="download-dataframe-csv312"),
        ],
            xs=12, sm=12, md=12, lg=3, xl=3
        ),

        # dbc.Col([
        #     html.Button("Tüm veritabanını Excel olarak indir", id="btn_xlsx"),
        #     dcc.Download(id="download-dataframe-xlsx"),
        # ],
        #     xs=6, sm=6, md=6, lg=3, xl=3
        # ),

    ], no_gutters=True, justify='center'),

    html.Hr(),

    dbc.Row([

        dbc.Col([
            html.Label(['Görüş ve öneri için: ',
                        html.A('bilgi@trakyaka.org.tr',
                               href='mailto:bilgi@trakyaka.org.tr;eguney@trakyaka.org.tr;ssimsek@trakyaka.org.tr')],
                        className="font-weight-bold text-dark"
                       )
        ],
           xs=12, sm=12, md=12, lg=3, xl=3
        ),
    ], no_gutters=False, justify='center'),
], fluid=True)

# @app.callback(
#     dash.dependencies.Output('cities-dropdown', 'options'),
#     [dash.dependencies.Input('countries-dropdown', 'value')])
# def set_cities_options(selected_country):
#     return [{'label': i, 'value': i} for i in all_options[selected_country]]

# @app.callback(
#     dash.dependencies.Output('cities-dropdown', 'value'),
#     [dash.dependencies.Input('cities-dropdown', 'options')])
# def set_cities_value(available_options):
#     return available_options[0]['value']

# @app.callback(
#     dash.dependencies.Output('landmarks-dropdown', 'options'),
#     [dash.dependencies.Input('countries-dropdown', 'value'),
#      dash.dependencies.Input('cities-dropdown', 'value')])
# def set_landmarks_options(selected_country, selected_city):
#     return [{'label': i, 'value': i} for i in all_options[selected_country][selected_city]]

# @app.callback(
#     dash.dependencies.Output('landmarks-dropdown', 'value'),
#     [dash.dependencies.Input('landmarks-dropdown', 'options')])
# def set_landmarks_value(available_options):
#     return available_options[0]['value']

#.........................................#
# Alternatif çözüm denemesi: 3 dropdown'ın 2 callback'te gösterilmesi
@app.callback([
    dash.dependencies.Output('cities-dropdown12', 'options'),
    dash.dependencies.Output('cities-dropdown12', 'value'),],
    [dash.dependencies.Input('countries-dropdown12', 'value'),])
def set_landmarks_value(selected_country):
    if selected_country is None:
        raise PreventUpdate
    else:
        return ([{'label': i, 'value': i} for i in all_options[selected_country]],
            [{'label': i, 'value': i} for i in all_options[selected_country]][0]['value'])
@app.callback([dash.dependencies.Output('landmarks-dropdown12', 'options'),
    dash.dependencies.Output('landmarks-dropdown12', 'value'),],
    [dash.dependencies.Input('countries-dropdown12', 'value'),
    dash.dependencies.Input('cities-dropdown12', 'value'),])
def set_landmarks_value(selected_country,selected_city):
    if (selected_country or selected_city) is None:
        raise PreventUpdate
    else:
        return ([{'label': y, 'value': y} for y in all_options[selected_country][selected_city]],
            [{'label': y, 'value': y} for y in all_options[selected_country][selected_city]][0]['value'])

#.........................................#

# @app.callback(
#     dash.dependencies.Output('cities-dropdown1', 'options'),
#     [dash.dependencies.Input('countries-dropdown1', 'value')])
# def set_cities_options1(selected_country1):
#     return [{'label': i, 'value': i} for i in all_options[selected_country1]]

# @app.callback(
#     dash.dependencies.Output('cities-dropdown1', 'value'),
#     [dash.dependencies.Input('cities-dropdown1', 'options')])
# def set_cities_value1(available_options1):
#     return available_options1[0]['value']

# @app.callback(
#     dash.dependencies.Output('landmarks-dropdown1', 'options'),
#     [dash.dependencies.Input('countries-dropdown1', 'value'),
#      dash.dependencies.Input('cities-dropdown1', 'value')])
# def set_landmarks_options1(selected_country1, selected_city1):
#     return [{'label': i, 'value': i} for i in all_options[selected_country1][selected_city1]]

# @app.callback(
#     dash.dependencies.Output('landmarks-dropdown1', 'value'),
#     [dash.dependencies.Input('landmarks-dropdown1', 'options')])
# def set_landmarks_value1(available_options1):
#     return available_options1[0]['value']

#***************************************************
## 3'lü sıralı Bölge, İl, İlçe Dropdown
# @app.callback(
#     dash.dependencies.Output('cities-dropdown2', 'options'),
#     [dash.dependencies.Input('countries-dropdown2', 'value')])
# def set_cities_options2(selected_country2):
#     return [{'label': i, 'value': i} for i in all_options2[selected_country2]]

# @app.callback(
#     dash.dependencies.Output('cities-dropdown2', 'value'),
#     [dash.dependencies.Input('cities-dropdown2', 'options')])
# def set_cities_value2(available_options2):
#     return available_options2[0]['value']

# @app.callback(
#     dash.dependencies.Output('landmarks-dropdown2', 'options'),
#     [dash.dependencies.Input('countries-dropdown2', 'value'),
#      dash.dependencies.Input('cities-dropdown2', 'value')])
# def set_landmarks_options2(selected_country2, selected_city2):
#     return [{'label': i, 'value': i} for i in all_options2[selected_country2][selected_city2]]

# @app.callback(
#     dash.dependencies.Output('landmarks-dropdown2', 'value'),
#     [dash.dependencies.Input('landmarks-dropdown2', 'options')])
# def set_landmarks_value2(available_options2):
#     return available_options2[0]['value']

#***************************************************
# 2'li sıralı Bölge, İl, İlçe Dropdown

# @app.callback(
#     dash.dependencies.Output('cities-dropdown2', 'options'),
#     [dash.dependencies.Input('countries-dropdown2', 'value')])
# def set_cities_options2(selected_country2):
#     # return [{'label': i, 'value': i} for i in all_options2[selected_country2]]
#     if not selected_country2:
#         raise PreventUpdate
#     if type(selected_country2) == 'str':
#         return [{'label': i, 'value': i} for i in all_options2[selected_country2]]
#     else:
#         return [{'label': i, 'value': i} for country in selected_country2 for i in all_options2[country]]

# @app.callback(
#     dash.dependencies.Output('cities-dropdown2', 'value'),
#     [dash.dependencies.Input('cities-dropdown2', 'options')])
# def set_cities_value2(available_options2):
#     # if not available_options2:
#     #     raise PreventUpdate
#     return [available_options2[0]['value']]

    #Alternatif 1
    # if type(available_options2) == 'str':
    #     return [available_options2]

    #Alternatif 2
    # if type(available_options2) == 'str':
    #     return available_options2[0]['value']
    # else:
    #     return [{'label': i, 'value': i} for i in all_options2[0]['value']]

#***************************************************

@app.callback(
    dash.dependencies.Output("download-dataframe-csv112", "data"),
    dash.dependencies.Input("btn_csv112", "n_clicks"),
    prevent_initial_call=True,)
def func(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        # return dcc.send_data_frame(df1.to_csv, "ilce_istatistikleri.csv")
        return dcc.send_file( "datasets/ilceData_04.12.21_Il_Ilcesiz.csv")

@app.callback(
    dash.dependencies.Output("download-dataframe-csv212", "data"),
    dash.dependencies.Input("btn_csv212", "n_clicks"),
    prevent_initial_call=True,)
def func(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        # return dcc.send_data_frame(df1.to_csv, "ilce_istatistikleri.csv")
        return dcc.send_file( "https://raw.githubusercontent.com/ertugguney/2017-2020-datasets/main/yerlesim.csv")

@app.callback(
    dash.dependencies.Output("download-dataframe-csv312", "data"),
    dash.dependencies.Input("btn_csv312", "n_clicks"),
    prevent_initial_call=True,)
def func(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        # return dcc.send_data_frame(df1.to_csv, "ilce_istatistikleri.csv")
        return dcc.send_file( "https://raw.githubusercontent.com/ertugguney/2017-2020-datasets/main/metaveri.csv")

# @app.callback(
#     dash.dependencies.Output("download-dataframe-xlsx", "data"),
#     dash.dependencies.Input("btn_xlsx", "n_clicks"),
#     prevent_initial_call=True,)
# def func1(n_clicks):
#     # return dcc.send_data_frame(df1.to_excel, "ilce_istatistikleri.xlsx", sheet_name="Sayfa1")
#     return dcc.send_file("../ilce-veri/ilce_istatistikleri.xlsx")

@app.callback(
    [dash.dependencies.Output('display-selected-values12', 'children'),
    #  dash.dependencies.Output('my_bee_map1', 'figure'),
     dash.dependencies.Output('bar_graph12','figure'),
     dash.dependencies.Output('tree_map12','figure'),
    #  dash.dependencies.Output('polinom_graph','figure'),
    #  dash.dependencies.Output('trend_ilce','figure'),
    #  dash.dependencies.Output('bar_graph_il','figure'),
    #  dash.dependencies.Output('bar_graph_bolge','figure'),
    #  dash.dependencies.Output('tree_map_bolgesel','figure'),
     ],
    [dash.dependencies.Input('countries-dropdown12', 'value'),
     dash.dependencies.Input('cities-dropdown12', 'value'),
     dash.dependencies.Input('landmarks-dropdown12', 'value'),
    #  dash.dependencies.Input('countries-dropdown1', 'value'),
    #  dash.dependencies.Input('cities-dropdown1', 'value'),
    #  dash.dependencies.Input('landmarks-dropdown1', 'value'),
    #  dash.dependencies.Input('countries-dropdown2', 'value'),
    #  dash.dependencies.Input('cities-dropdown2', 'value'),
    #  dash.dependencies.Input('landmarks-dropdown2', 'value'),   #3'lü Bölge, İl, İlçe Dropdown'da gerekliydi
     dash.dependencies.Input('slider_year12','value'),
     ],
     )

def update_graph(selected_country,selected_city,selected_landmark,
    # selected_country1,selected_city1,selected_landmark1,selected_country2,selected_city2,
    slider_year):

    if (selected_country or selected_city or selected_landmark or slider_year) is None:
        raise PreventUpdate
    else:
        dff = df.copy()
        dff = dff[(dff["anabaslik"]==selected_country)&(dff["ortabaslik"]==selected_city)&(dff["baslik"]==selected_landmark)&(dff["Yıl"]==slider_year)]
        # dffm =pd.merge(ilce_adi,dff, how='left', on=["İlçe Adı","İl-İlçe"]).fillna(0)

        # dff1 = df.copy()
        # dff1 = dff1[(dff1["anabaslik"]==selected_country1)&(dff1["ortabaslik"]==selected_city1)&(dff1["baslik"]==selected_landmark1)&(dff1["Yıl"]==slider_year)]
        # dff1 =pd.merge(ilce_adi,dff1, how='left', on=["İlçe Adı","İl-İlçe"]).fillna(0)
        # dff1.rename(columns={"deger":"deger1"},inplace=True)

        # dff_ilce = df.copy()
        # dff_ilce = dff_ilce[(dff_ilce["anabaslik"]==selected_country)&(dff_ilce["ortabaslik"]==selected_city)&(dff_ilce["baslik"]==selected_landmark)&(dff_ilce["Bölge (Düzey-2)"]==selected_country2)&(dff_ilce["İl Adı"]==selected_city2)&(dff_ilce["İlçe Adı"]==selected_landmark2)]

        #Tekli seçimde çalışan kod-multi değil
        # dff_ilce = dff_ilce[(dff_ilce["anabaslik"]==selected_country)&(dff_ilce["ortabaslik"]==selected_city)&(dff_ilce["baslik"]==selected_landmark)&(dff_ilce["Bölge (Düzey-2)"]==selected_country2)&(dff_ilce["İl Adı"]==selected_city2)]
        # dff_bolge = dff[(dff["Bölge (Düzey-2)"]==selected_country2)]
        # dff_il = dff_bolge[(dff_bolge["İl Adı"]==selected_city2)]


        #Multi'de yalnızca çoklu seçimlerde çalışan, tekli seçimlerde çalışmayan kod
        # dff_ilce = dff_ilce[(dff_ilce["anabaslik"]==selected_country)&(dff_ilce["ortabaslik"]==selected_city)&(dff_ilce["baslik"]==selected_landmark)&(dff_ilce["Bölge (Düzey-2)"].isin(list(selected_country2)))&(dff_ilce["İl Adı"].isin(list(selected_city2)))]
        # dff_bolge = dff[(dff["Bölge (Düzey-2)"].isin(list(selected_country2)))]
        # dff_il = dff_bolge[(dff_bolge["İl Adı"].isin(list(selected_city2)))]

        # if type(selected_country2) == 'str':
        #     if type(selected_city2) == 'str':
        #         dff_ilce = dff_ilce[(dff_ilce["anabaslik"]==selected_country)&(dff_ilce["ortabaslik"]==selected_city)&(dff_ilce["baslik"]==selected_landmark)&(dff_ilce["Bölge (Düzey-2)"]==selected_country2)&(dff_ilce["İl Adı"]==selected_city2)]
        #         dff_bolge = dff[(dff["Bölge (Düzey-2)"]==selected_country2)]
        #         dff_il = dff[(dff["Bölge (Düzey-2)"]==selected_country2)&(dff["İl Adı"]==selected_city2)]
        #     else:
        #         dff_ilce = dff_ilce[(dff_ilce["anabaslik"]==selected_country)&(dff_ilce["ortabaslik"]==selected_city)&(dff_ilce["baslik"]==selected_landmark)&(dff_ilce["Bölge (Düzey-2)"]==selected_country2)&(dff_ilce["İl Adı"].isin(list(selected_city2)))]
        #         dff_bolge = dff[(dff["Bölge (Düzey-2)"]==selected_country2)]
        #         dff_il = dff[(dff["Bölge (Düzey-2)"]==selected_country2)&(dff["İl Adı"].isin(list(selected_city2)))]
        # else:
        #     if type(selected_city2) == 'str':
        #         dff_ilce = dff_ilce[(dff_ilce["anabaslik"]==selected_country)&(dff_ilce["ortabaslik"]==selected_city)&(dff_ilce["baslik"]==selected_landmark)&(dff_ilce["Bölge (Düzey-2)"].isin(list(selected_country2)))&(dff_ilce["İl Adı"]==selected_city2)]
        #         dff_bolge = dff[(dff["Bölge (Düzey-2)"].isin(list(selected_country2)))]
        #         dff_il = dff[(dff["Bölge (Düzey-2)"].isin(list(selected_country2))&(dff["İl Adı"].isin(list(selected_city2))))]

        #     else:
        #         dff_ilce = dff_ilce[(dff_ilce["anabaslik"]==selected_country)&(dff_ilce["ortabaslik"]==selected_city)&(dff_ilce["baslik"]==selected_landmark)&(dff_ilce["Bölge (Düzey-2)"].isin(list(selected_country2)))&(dff_ilce["İl Adı"].isin(list(selected_city2)))]
        #         dff_bolge = dff[(dff["Bölge (Düzey-2)"].isin(list(selected_country2)))]
        #         dff_il = dff[(dff["Bölge (Düzey-2)"].isin(list(selected_country2))&(dff["İl Adı"]==selected_city2))]

        dffYıl=df.copy()
        dffYıl = dffYıl[(dffYıl["anabaslik"]==selected_country)&(dffYıl["ortabaslik"]==selected_city)&(dffYıl["baslik"]==selected_landmark)]
        ilkYıl=np.min(dffYıl['Yıl'])
        sonYıl=np.max(dffYıl['Yıl'])

        if np.sum(dff['deger'])==0:
            # fig4 = go.Figure().add_annotation(x=2, y=2,text=u'Bu başlıkta seçilen yıl için veri bulunmamaktadır, {}-{} yılları arasında veri bulunmaktadır'.format(ilkYıl,sonYıl),font=dict(family="sans serif",size=25,color="red"),showarrow=False,yshift=10),
            fig5 = go.Figure().add_annotation(x=2, y=2,text=u'Bu başlıkta seçilen yıl için veri bulunmamaktadır, {}-{} yılları arasında veri bulunmaktadır'.format(ilkYıl,sonYıl),font=dict(family="sans serif",size=25,color="red"),showarrow=False,yshift=10)
            fig6 = go.Figure().add_annotation(x=2, y=2,text=u'Bu başlıkta seçilen yıl için veri bulunmamaktadır, {}-{} yılları arasında veri bulunmaktadır'.format(ilkYıl,sonYıl),font=dict(family="sans serif",size=25,color="red"),showarrow=False,yshift=10),
            # fig7 = go.Figure().add_annotation(x=2, y=2,text=u'Bu başlıkta seçilen yıl için veri bulunmamaktadır, {}-{} yılları arasında veri bulunmaktadır'.format(ilkYıl,sonYıl),font=dict(family="sans serif",size=25,color="red"),showarrow=False,yshift=10)
            # fig8 = go.Figure().add_annotation(x=2, y=2,text=u'Bu başlıkta seçilen yıl için veri bulunmamaktadır, {}-{} yılları arasında veri bulunmaktadır'.format(ilkYıl,sonYıl),font=dict(family="sans serif",size=25,color="red"),showarrow=False,yshift=10),
            # fig9 = go.Figure().add_annotation(x=2, y=2,text=u'Bu başlıkta seçilen yıl için veri bulunmamaktadır, {}-{} yılları arasında veri bulunmaktadır'.format(ilkYıl,sonYıl),font=dict(family="sans serif",size=25,color="red"),showarrow=False,yshift=10)
            # fig10 = go.Figure().add_annotation(x=2, y=2,text=u'Bu başlıkta seçilen yıl için veri bulunmamaktadır, {}-{} yılları arasında veri bulunmaktadır'.format(ilkYıl,sonYıl),font=dict(family="sans serif",size=25,color="red"),showarrow=False,yshift=10),
            # fig11 = go.Figure().add_annotation(x=2, y=2,text=u'Bu başlıkta seçilen yıl için veri bulunmamaktadır, {}-{} yılları arasında veri bulunmaktadır'.format(ilkYıl,sonYıl),font=dict(family="sans serif",size=25,color="red"),showarrow=False,yshift=10),
            return u'Bu başlıkta seçilen yıl için veri bulunmamaktadır, {}-{} yılları arasında veri bulunmaktadır'.format(ilkYıl,sonYıl),fig5,fig6,
                #,fig4,fig7,fig8,fig9,fig10,fig11
        else:
            # fig = px.choropleth_mapbox(dffm, geojson=counties, locations='ilce_no',
            #     color='deger',
            #     color_continuous_scale=px.colors.sequential.YlOrRd,
            #     range_color=(np.quantile(dff["deger"],0.01), np.quantile(dff["deger"],0.92)),
            #     mapbox_style="carto-positron",
            #     hover_name='İl-İlçe',
            #     hover_data={'ilce_no':False,
            #                 "Yıl":True,'deger':':,'},
            #     zoom=5, center={"lat": 38.9597594, "lon": 34.9249653},
            #     opacity=0.5,
            #     labels={'deger':selected_landmark},
            #     )
            # fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            # fig.update_layout(dragmode=False)

            # fig.update_layout(
            #     hoverlabel=dict(
            #     bgcolor="white",
            #     font_size=14,
            #     font_family="Rockwell"
            #     ))
            # fig.update_layout(coloraxis=dict(colorbar_x=-0.1,
            #     colorbar_y=0.57,
            #     colorbar_len=1,
            #     colorbar_thickness=30))

            figure1 = px.bar(
                data_frame=dff,
                x='İlçe Adı',
                y='deger',
                hover_name='İl-İlçe',
                hover_data={'Yıl':True,'İlçe Adı':False,'deger':':,'},
                labels={'İlçe Adı': 'İlçe Adı','deger': selected_landmark},
                template='ggplot2'
            )
            figure1.update_xaxes(tickangle=45,categoryorder='total ascending')

            dff["Türkiye"] = "Türkiye"
            dff2=dff.copy()
            dff2 = dff.append({'İl-İlçe': 'Türkiye', 'deger': dff2['deger'].sum(),'Türkiye':''}, ignore_index=True)

            figure2=go.Figure(go.Treemap(
                labels=dff2['İl-İlçe'],
                parents=dff2['Türkiye'],
                values=dff2['deger'],
                branchvalues='total',
                hovertemplate='<b>%{label} </b> <br>Değer: %{value:,} <br>TR Payı: %{percentParent:.2%}',
                texttemplate='<b>%{label} </b> <br>Değer: %{value:,} <br>TR Payı: %{percentParent:.2%}',
                ))
            figure2.update_traces(root_color="lightgray")
            figure2.update_layout(margin = dict(t=50, l=25, r=25, b=25))

            # def format_coefs(coefs):
            #     equation_list = [f"{coef}x^{i}" for i, coef in enumerate(coefs)]
            #     equation =" + ".join(equation_list)
            #     replace_map = {"x^0": "", "x^1": "x", '+ -': '- '}
            #     for old, new in replace_map.items():
            #         equation = equation.replace(old, new)
            #     return equation

            # X = dff1.deger1.values.reshape(-1, 1)
            # x_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)

            # figure3 = px.scatter(x=dff1['deger1'], y=dffm['deger'],text=dffm['İl-İlçe'],
            #     labels=dict(text='İlçe',x=selected_landmark1, y=selected_landmark),
            #     hover_data={'Yıl':dffm['Yıl']},
            #     opacity=1)
            # figure3.update_traces(marker_size=7,textposition='top center')

            # figure3.update_layout(legend=dict(
            #     yanchor="top",
            #     y=1.2,
            #     xanchor="left",
            #     x=0
            # ))

            # for degree in [1, 2]:
            #     poly = PolynomialFeatures(degree)
            #     poly.fit(X)
            #     X_poly = poly.transform(X)
            #     x_range_poly = poly.transform(x_range)

            #     model = LinearRegression(fit_intercept=False)
            #     model.fit(X_poly, dffm.deger)
            #     y_poly = model.predict(x_range_poly)

            #     equation = format_coefs(model.coef_.round(15))
            #     figure3.add_traces(go.Scatter(x=x_range.squeeze(), y=y_poly, name=equation))

            # figure4 = px.line(dff_ilce, x='Yıl', y='deger', color='İlçe Adı',
            #     markers=True,
            #     text='deger',
            #     labels={'İl-İlçe': 'İlçe','deger': selected_landmark},
            #     # labels=dict(text='İlçe',x='Yıl', y=selected_landmark),
            #     hover_name='İl-İlçe',
            #     hover_data={'İlçe Adı':False,'İl-İlçe':False,'deger':':,'},
            #     )
            # figure4.update_traces(marker_size=7,textposition='top center',texttemplate='%{text:,}')
            # figure4.update_xaxes(tickmode='linear',range=[np.min(dff_ilce['Yıl'])-0.3, np.max(dff_ilce['Yıl'])+0.3])

            # figure5 = px.bar(
            #     data_frame=dff_il,
            #     x='İlçe Adı',
            #     y='deger',
            #     hover_name='İl-İlçe',
            #     hover_data={'Yıl':True,'İlçe Adı':False,'deger':':,'},
            #     labels={'İlçe Adı': 'İlçe Adı','deger': selected_landmark},
            #     template='ggplot2'
            # )
            # figure5.update_xaxes(tickangle=45,categoryorder='total ascending')

            # figure6 = px.bar(
            #     data_frame=dff_bolge,
            #     x='İlçe Adı',
            #     y='deger',
            #     hover_name='İl-İlçe',
            #     hover_data={'Yıl':True,'İlçe Adı':False,'deger':':,'},
            #     labels={'İlçe Adı': 'İlçe Adı','deger': selected_landmark},
            #     template='ggplot2'
            # )
            # figure6.update_xaxes(tickangle=45,categoryorder='total ascending')

            # figure7 = px.treemap(dff, path=['Türkiye', 'Bölge (Düzey-2)', 'İl Adı', 'İlçe Adı'], values='deger',)
            # figure7.update_traces(root_color="lightgray")
            # figure7.update_traces(texttemplate='<b>%{label} </b> <br>Değer: %{value:,} <br>TR Payı: %{percentRoot:.2%}<br>İl Payı: %{percentParent:.2%}<br>Seçilen Seviyeye göre Payı: %{percentEntry:.2%}')
            # figure7.update_traces(hovertemplate='<b>%{label} </b> <br>Değer: %{value:,} <br>TR Payı: %{percentRoot:.2%}<br>Bir Üst Seviyeye göre Payı: %{percentParent:.2%}<br>Seçilen Seviyeye göre Payı: %{percentEntry:.2%}')
            # figure7.update_layout(margin = dict(t=50, l=25, r=25, b=25))

            return u'Bu başlıkta {}-{} yılları arasında veri bulunmaktadır'.format(
            ilkYıl,sonYıl),figure1,figure2,
            # fig,figure3,figure4,figure5,figure6,figure7,
                    # dcc.send_data_frame(dff.to_csv, "mydf.csv"),

# if __name__ == '__main__':
#     app.run_server(debug=False)

# %%
