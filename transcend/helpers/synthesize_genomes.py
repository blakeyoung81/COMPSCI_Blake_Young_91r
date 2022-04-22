import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import datetime

	
def get_all_combinations(parent): # Finds all possible combinations of alleles a parent can pass on to their offspring, assuming independen assortment.
	if len(parent) == 1:
		return [parent[0][0], parent[0][1]]
	else:
		genlist = []
		for x in get_all_combinations(parent[1:]):
			genlist.append(parent[0][0] + x)
			genlist.append(parent[0][1] + x)
		return genlist

def make_row(genotype, allele):
	row = []
	for a in genotype:
		row.append(a + allele)
	return row

def make_table(parent1, parent2):
	table = []
	for a in parent1:
		table.append(make_row(parent2, a))
	return table

def print_table(table, c1, c2): # formats and prints Punnett square
	latextable = []
	divlength = (len(c1[0])*2+4)*2**(len(c1[0]))
	print('')
	print('', end=' ')
	for a in c2:
		print(' '*(len(c1[0])+3) + a + '', end=' ')
		latextable.append('& ' + a + ' ')
	print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
	latextable.append('\\\ \n\\hline\n')
	
	for i, row in enumerate(table):
		print(c1[table.index(row)], end=' ')
		latextable.append(c1[table.index(row)] + ' & ')
		print('|', end=' ')
		for j, cell in enumerate(row):
			print(cell + ' | ', end=' ')
			if j != len(row)-1:
				latextable.append(cell + ' & ')
			else:
				latextable.append(cell + ' ')
		print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
		if i != len(table)-1:
			latextable.append('\\\ \n')	
	return latextable		
	
def make_dictionary(table): # calculates frequencies for each genotype present in table
	freqtable = []
	GeneDict = {}
	freqtable.append('\n')
	calculated = []
	genotypes = [a for b in table for a in b]
	for k, x in enumerate(genotypes):
		count = 0
		for y in genotypes:
			if sorted(x) == sorted(y):
				count += 1
		if sorted(x) not in calculated:
			GeneDict[x] = str(float(count)/float((len(genotypes)))*100) + "%."
			freqtable.append(x + ' & ' + str(float(count)/float((len(genotypes)))*100) + '\\% \\\ \\hline \n')	
		calculated.append(sorted(x))
	return GeneDict

def make_sqaures(genoset1, genoset2):
	p1 = genoset1.split(' ')
	p2 = genoset2.split(' ')
	c1 = get_all_combinations(p1)
	c2 = get_all_combinations(p2)
	a = make_table(c1, c2)
	GeneDicitionary = make_dictionary(a)
	return GeneDicitionary

#get the file
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
# Get genomes data frame
rsid_list = ['rs713598']
#Get genotype of trait 1 in host
new_df = host_genome.loc[host_genome['rsid'].isin(rsid_list)]
genotype_host= new_df['genotype'].values[0]
print(new_df)
#get genotype of trait 1 in match
new_df = match_genome.loc[match_genome['rsid'].isin(rsid_list)]
genotype_match = new_df['genotype'].values[0]
print(new_df)

print(make_sqaures(genotype_host,genotype_match))
        #query for value rsid and return row
        #get rsid location and    #Check allele
    #get P(offspring) given personal genome
    #add probablity value to list
