# Trial Script to get Pokemon in Table from Bulbapedia
# using Pandas

# Link: https://bulbapedia.bulbagarden.net/wiki/
#				List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number

import requests
import pandas as pd
import numpy as np

print('Reading National Pokedex')

def getPokemonFromBulba():
	url = 'https://bulbapedia.bulbagarden.net/wiki/' + \
 		'List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'

 	# Act like a browser to access the website
	header = {
	  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)" +
	  					" AppleWebKit/537.36 (KHTML, like Gecko)" + 
	  					" Chrome/50.0.2661.75 Safari/537.36",
	  "X-Requested-With": "XMLHttpRequest"
	}

	r = requests.get(url, headers=header)
	dfs = pd.read_html(r.text)

	return dfs



def changeValToInt(dexFrame, col):
	'''Ex: Changes #001 to 1'''
	numRows = len(dexFrame.index)

	for row in range(numRows):
		if isinstance(dexFrame.at[row, col], str):
			if dexFrame.at[row, col][0] == '#':
				# Cell needs to be changed
				dexFrame.at[row, col] = int(dexFrame.at[row, col][1:])



def formatRegionalDex(dexFrame, verbose = False):
	'''Takes the HTML version and makes a useable form of the regional
	pokedex.'''
	# Rename the dual type to 'Type 2'
	dexFrame.at[0, 5] = 'Type 2'

	# Change the format of the dex numbering
	changeValToInt(dexFrame, 1) # National pokedex (Ndex)
	changeValToInt(dexFrame, 0) # Regional pokedex (e.g. Kdex for kanto)

	# Remove inrelevant or incorrect rows
	dexFrame = dexFrame.dropna(subset = [0])

	if verbose:
		print('New Head is ', dexFrame.head(25))

	# Set the column labels to the first row, namely:
	# 'Kdex', 'Ndex', 'Pokemon', 'Type', 'Type 2'
	dexFrame.columns = dexFrame.loc[0]

	# Now that the columns are relabelled, drop the duplicate row
	dexFrame = dexFrame.drop(0)

	# No need to include the 'MS' Column (saved for pictures)
	dexFrame = dexFrame.drop('MS', axis = 1)

	# Set the frame to beindexed by the national index
	dexFrame.set_index('Ndex', inplace = True)

	if verbose:
		# Print the head
		print(dexFrame.head())

	return dexFrame




def main():
	'''Gets the national pokedex, formats each regional dex, and appends them
	into a single pokedex.'''
	dfs = getPokemonFromBulba()

	kanto = formatRegionalDex(dfs[1])
	johto = formatRegionalDex(dfs[2])
	hoenn = formatRegionalDex(dfs[3])
	sinnoh = formatRegionalDex(dfs[4])

	national = pd.concat([kanto, johto, hoenn, sinnoh], sort = 'False')
	natCols = ['Kdex', 'Jdex', 'Hdex', 'Sdex', 'Pokémon', 'Type', 'Type 2']
	national = national[natCols]

	print(national)

if __name__ == '__main__':
	main()