import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


result =r"C:\Users\blake\OneDrive\Desktop\compsci91r\python\merged and cleaned final.csv"
random_lady = r"C:\Users\blake\OneDrive\Desktop\compsci91r\python\Genomes\random lady.txt"
#genome = r"C:\Users\blake\OneDrive\Desktop\compsci91r\python\Blake Young.txt"
blake_young = r"C:\Users\blake\OneDrive\Desktop\compsci91r\python\Genomes\Blake Young.txt"


def trim_genome(genome_path):
    data = pd.read_csv(genome_path, sep='\t', dtype={'rsid':'str', 'chromosome':'object', 'position':'int', 'genotype':'str'}, comment='#')
    df = pd.DataFrame(data)

    #clear the rsid messup
    df.rename({' rsid': 'rsid'}, axis='columns', inplace=True)

    #Change letters to numbers for df ease
    df['chromosome'] = df['chromosome'].apply(lambda x: re.sub(r'X', r'23', x))
    df['chromosome'] = df['chromosome'].apply(lambda x: re.sub(r'Y', r'24', x))
    df['chromosome'] = df['chromosome'].apply(lambda x: re.sub(r'MT', r'25', x))
    df['chromosome'] = df['chromosome'].apply(lambda x: int(x))

    chromosome_dict = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'11', 12:'12', 13:'13', 
                    14:'14', 15:'15', 16:'16', 17:'17', 18:'18', 19:'19', 20:'20', 21:'21', 22:'22', 23:'X', 24:'Y', 25:'MT'}
    return df

match_genome = trim_genome(random_lady)
host_genome = trim_genome(blake_young)

genomes = [match_genome,host_genome]

rsid_list = ['rs713598']
correct = "GG"
#get genotype of trait 1 in match
new_df = match_genome.loc[match_genome['rsid'].isin(rsid_list)]
genotype_match = new_df['genotype'].values[0]
print(new_df)

#search genomes for allele at rsid
for genome in genomes:
    #search for rsid
    # Get genomes data frame
    #Get genotype of trait 1 in host
    new_df = genome.loc[genome['rsid'].isin(rsid_list)]
    ranked= new_df['genotype'].values[0]
    if ranked == correct:
        #Send this to be returned
        print("good")
    else:
        print("bad")
        #send to not be returned
    #search for genotype

#if they have it then return them

#if they have it give them one point



