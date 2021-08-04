import json
import csv
import pandas as pd
from collections import OrderedDict


injured_or_dead_people=[]
not_related_or_irrelevant=[]
other_useful_information=[]
displaced_people_and_evacuations=[]
donation_needs_or_offers_or_volunteering_services=[]
infrastructure_and_utilities_damage=[]
caution_and_advice=[]
sympathy_and_emotional_support=[]
missing_trapped_or_found_people=[]

df= pd.read_csv("2014_pakistan_floods_cf_labels.csv", header=0)
j=-1
for i in df['choose_one_category']:
	j=j+1
	if i == 'injured_or_dead_people':
		injured_or_dead_people.append(df['tweet_text'][j])	

	if i == 'not_related_or_irrelevant':
		not_related_or_irrelevant.append(df['tweet_text'][j])

	if i == 'other_useful_information':
		other_useful_information.append(df['tweet_text'][j])

	if i == 'displaced_people_and_evacuations':
		displaced_people_and_evacuations.append(df['tweet_text'][j])

	if i == 'donation_needs_or_offers_or_volunteering_services':
		donation_needs_or_offers_or_volunteering_services.append(df['tweet_text'][j])

	if i == 'infrastructure_and_utilities_damage':
		infrastructure_and_utilities_damage.append(df['tweet_text'][j])

	if i == 'caution_and_advice':
		caution_and_advice.append(df['tweet_text'][j])

	if i == 'sympathy_and_emotional_support':
		sympathy_and_emotional_support.append(df['tweet_text'][j])

	if i == 'missing_trapped_or_found_people':
		missing_trapped_or_found_people.append(df['tweet_text'][j])

final = {"injured_or_dead_people" : injured_or_dead_people, "not_related_or_irrelevant":not_related_or_irrelevant, 
"other_useful_information":other_useful_information, "displaced_people_and_evacuations":displaced_people_and_evacuations,
 "donation_needs_or_offers_or_volunteering_services":donation_needs_or_offers_or_volunteering_services, 
 "infrastructure_and_utilities_damage":infrastructure_and_utilities_damage, "caution_and_advice":caution_and_advice, 
 "sympathy_and_emotional_support":sympathy_and_emotional_support, "missing_trapped_or_found_people":missing_trapped_or_found_people}
print(final)
print(json.dumps(final,indent=2))

with open('jso.json', 'w') as outfile:
	outfile.write(json.dumps(final,indent=2))














