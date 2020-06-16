import requests
import re
import mwparserfromhell
import json
import csv

titles = ["List_of_hip_hop_musicians","List_of_R%26B_musicians","List_of_country_music_performers",
          "List_of_heavy_metal_bands","List_of_rock_music_performers",
          "List_of_dance-pop_artists","List_of_electro_house_artists","List_of_alternative_rock_artists",
          "List_of_indie_pop_artists",
          "List_of_Christian_worship_music_artists",
          "List_of_instrumental_bands","List_of_jazz_musicians",
          "List_of_Latin_pop_artists",
          "List_of_1950s_musical_artists","List_of_1960s_musical_artists", "List_of_soul_musicians", 
          "List_of_reggae_musicians",
          "List_of_grunge_bands", "List_of_screamo_bands",
          "List_of_gospel_musicians"]

def get_info(text_list):
    intro = "https://en.wikipedia.org/w/api.php?action=query&format=json&titles="
    closer = "&prop=extracts&exintro&explaintext"
    return_info = []
    for x in titles:
        
        response = requests.get(
     intro + x + closer,
     params={
         'action': 'query',
         'format': 'json',
         
         'prop': 'revisions',
         'rvprop': 'content',
     }
 ).json()
        page = next(iter(response['query']['pages'].values()))
        wikicode = page['revisions'][0]['*']
        parsed_wikicode = mwparserfromhell.parse(wikicode)
        list_vals = parsed_wikicode.split("*")
        listToStr = ' '.join(map(str, list_vals)) 
        list_vals2 = listToStr.split("\n")
        new_list = []
        for y in list_vals2:
            new_list += [re.sub(r'\W+', '', y)]
        new_set = {h.replace('rapper', '').replace('refname', '').replace('Rap', '').replace('entertainer','').replace('recordproducer','').replace('musician','').replace('Whatever', '').replace('band', '') for h in new_list}
        new_set2 = []
        for z in new_set:
            new_set2 += [re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', z)]
        return_info += [new_set2]
        
       
        
    return return_info
answer = get_info(titles)
# pull website

#response = requests.get(
#     "https://en.wikipedia.org/w/api.php?action=query&format=json&titles=List_of_hip_hop_musicians&prop=extracts&exintro&explaintext",
#     params={
#         'action': 'query',
#         'format': 'json',
#         'titles': 'List of hip hop musicians',
#         'prop': 'revisions',
#         'rvprop': 'content',
#     }
# ).json()
#response2 = requests.get(
#     "https://en.wikipedia.org/w/api.php?action=query&format=json&titles=List_of_R%26B_musicians&prop=extracts&exintro&explaintext",
#     params={
#         'action': 'query',
#         'format': 'json',
#         'titles': 'List of R&B musicians',
#         'prop': 'revisions',
#         'rvprop': 'content',
#     }
# ).json()
# cleaning up the file into a string
#page = next(iter(response['query']['pages'].values()))
#wikicode = page['revisions'][0]['*']
#parsed_wikicode = mwparserfromhell.parse(wikicode)
#print(parsed_wikicode.strip_code())
# split by bullet
#list_vals = parsed_wikicode.split("*")
#print(list_vals)
# turn to list
#listToStr = ' '.join(map(str, list_vals)) 
# split by new line
#list_vals2 = listToStr.split("\n")
#print(list_vals2)
# get rid of all random characters
#new_string = ""
#new_list = []
#for x in list_vals2:
#    new_list += [re.sub(r'\W+', '', x)]
#print(new_list)
#new_list2 = []
# strip of certain phrases we don't use
#new_set = {x.replace('rapper', '').replace('refname', '').replace('Rap', '').replace('entertainer','').replace('recordproducer','').replace('musician','') for x in new_list}
#print(new_set)
#new_set2 = []
#for x in new_set:
#    new_set2 += [re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', x)]
#print(new_set2)


# ok time to get serious, we are gonna export and clean up this bad boy



with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(answer)


#with open('out.csv', 'r', newline='') as csvf:
#    re = csv.reader(csvf)
#    final = []
#    for row in re:
#        final += [row]
        #print(row)

#print("output: ", final)
