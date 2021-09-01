import pandas as pd 
import csv

df = pd.read_csv("total_stars.csv")

del df["Luminosity"]

a = df.dropna(axis="columns", how="any")

df.to_csv('main.csv')