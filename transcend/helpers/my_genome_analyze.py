import matplotlib.pyplot as plt
import numpy as np  
#import requests
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import json


def trim_genome(genome_path):
    data = pd.read_csv(genome_path, sep='\t', dtype={'rsid':'str', 'chromosome':'object', 'position':'int', 'genotype':'str'}, comment='#')
    df = pd.DataFrame(data)
    #print(df.head())
    #print("that's what the head looks like")
    #clear the rsid messup
    df.rename({' rsid': 'rsid'}, axis='columns', inplace=True)
    #print(df['chromosome'].unique())
    #Change letters to numbers for df ease
    df['chromosome'] = df['chromosome'].apply(lambda x: re.sub(r'X', r'23', x))
    df['chromosome'] = df['chromosome'].apply(lambda x: re.sub(r'Y', r'24', x))
    df['chromosome'] = df['chromosome'].apply(lambda x: re.sub(r'MT', r'25', x))
    df['chromosome'] = df['chromosome'].apply(lambda x: int(x))
    return df

#Cute counting of genes
def gene_counter():
    x = []
    y = []
    chromosome_dict = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'11', 12:'12', 13:'13', 
                    14:'14', 15:'15', 16:'16', 17:'17', 18:'18', 19:'19', 20:'20', 21:'21', 22:'22', 23:'X', 24:'Y', 25:'MT'}
    for k in chromosome_dict:
        x.append(k)
        y.append(len(df[df.chromosome == k]))
    rsid_per_chromosome = dict(zip(x,y))
    if(rsid_per_chromosome[25])>0:
        print("male")
    else:
        print("female")
    rsid_per_chromosome_series = df.groupby('chromosome')['rsid'].count()
    rsid_per_chromosome_series.columns = ['chromosome', 'count']
    #rsid_per_chromosome_series.plot.barh(figsize=(16,9), fontsize=15)
    #plt.show()

def analyze_my_DNA(df):
    snp_df = pd.read_csv(snpedia)
    snp_df['genotype'] = snp_df['Unnamed: 0'].apply(lambda x: re.sub(r'.*([AGCT]);([AGCT])\)', r'\1\2', x))
    new_cols = ['rsid', 'magnitude', 'repute', 'summary', 'genotype']
    snp_df.columns = new_cols
    snp_df['rsid'] = snp_df['rsid'].map(lambda x : x.lower())
    snp_df['rsid'] = snp_df['rsid'].map(lambda x : re.sub(r'([a-z]{1,}[\d]+)\([agct];[agct]\)', r'\1', x))
    null_repute = snp_df[snp_df['repute'].isnull()]
    null_summaries = snp_df[snp_df['summary'].isnull()]
    null_repute_and_summaries = pd.concat([null_repute,null_summaries]).drop_duplicates().reset_index(drop=True)
    snp_df['repute'].fillna(value='Neutral', inplace=True)
    snp_df['summary'].fillna(value='None', inplace=True)
    #print(snp_df.head())
    #Entire data set
    new_df = snp_df.merge(df, how='inner', on=['rsid', 'genotype'], suffixes=('_SNPedia', '_myDNA'))
    print(new_df)
    new_df = new_df.sort_values(by=['magnitude'], ascending=False)
    #new_df = new_df.sort_values(by=['repute'], ascending=False)
    print(new_df)
    json_records = new_df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)


    # Create a DataFrame for some subsets of genes
    #good_genes = new_df[new_df.repute == 'Good']
    #bad_genes = new_df[new_df.repute == 'Bad']
    #interesting_genes = new_df[new_df.magnitude > 4] # 4 is the threshold for "worth your time" given by SNPedia
    return data
    #return data frame

random_lady = r"C:\Users\blake\OneDrive\Desktop\compsci91r\python\Genomes\random lady.txt"
blake_young = r"C:\Users\blake\OneDrive\Desktop\compsci91r\python\Genomes\Blake Young.txt"
snpedia = r"C:\Users\blake\OneDrive\Desktop\compsci91r\python\merged and cleaned final.csv"

#df = trim_genome(blake_young)
df = trim_genome(random_lady)
result = analyze_my_DNA(df)





#print(result)