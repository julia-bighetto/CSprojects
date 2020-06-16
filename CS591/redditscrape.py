import requests
import re
import mwparserfromhell
import json
import csv
import praw
import tkinter
import itertools
from praw.models import MoreComments
#authentication to access reddit api
reddit = praw.Reddit(client_id='5GKSQVWrx-AVdw', client_secret='RLRGubckYtMfLAfVk04BSUvkqHI', user_agent='Artist Popularity', username='wopocopo', password='Killtowin#58')
#only read from reddit
reddit.read_only = True
#genre titles
titles = ["Hip Hop Artists","R&B Musicians","Country Musicians",
          "Heavy Metal Bands","Rock Musicians",
          "Dance Pop Artists","Electro House Artists","Alternative Rock Artists",
          "Indie Pop Artists",
          "Christian Artists",
          "Instrumental Bands","Jazz Musicians",
          "Latin Pop Artists",
          "1950s Music Artists","1960s Music Artists", "Soul Musicians", 
          "Reggae Musicians",
          "Grunge Bands", "Screamo Bands",
          "Gospel Bands"]
# assign relevant music subreddits for each genre, as well as most popular music subreddits
music = [reddit.subreddit('Music'), reddit.subreddit('listentothis'), reddit.subreddit('unheardof'), reddit.subreddit('musicsuggestions')]
hip_hop = [reddit.subreddit('hiphopheads'), reddit.subreddit('Music')]
rb = [reddit.subreddit('rnb'), reddit.subreddit('Music')]
country = [reddit.subreddit('country'), reddit.subreddit('Music')]
heavy_metal = [reddit.subreddit('Metal'),reddit.subreddit('Heavymetal')]
rock_music = [reddit.subreddit('rockmusic'),reddit.subreddit('Music')]
dance_pop = [reddit.subreddit('popheads'), reddit.subreddit('synthpop')]
electro_house = [reddit.subreddit('electrohouse'), reddit.subreddit('Electronic')]
alt_rock = [reddit.subreddit('rockmusic'),reddit.subreddit('Music'), reddit.subreddit('AlternativeRock')]
indie_pop = [reddit.subreddit('indiepop'), reddit.subreddit('popheads')]
christian = [reddit.subreddit('ChristianMusic'), reddit.subreddit('Christianity')]
instrumental = [reddit.subreddit('instrumentalmusic'), reddit.subreddit('Instrumentals')]
jazz = [reddit.subreddit('Jazz'), reddit.subreddit('JazzFusion')]
latin = [reddit.subreddit('Reggaeton'), reddit.subreddit('latinmusic')]
music_1950s = [reddit.subreddit('50sMusic'), reddit.subreddit('Music')]
music_1960s = [reddit.subreddit('60sMusic'), reddit.subreddit('Music')]
soul = [reddit.subreddit('soul'),     
                      reddit.subreddit('Music'),reddit.subreddit('FunkSouMusic')]
reggae =[reddit.subreddit('Reggaeton'), reddit.subreddit('Music'),       
                        reddit.subreddit('reggae')]
grunge = [reddit.subreddit('grunge'), reddit.subreddit('Music')]
screamo = [reddit.subreddit('EmoScreamo'), reddit.subreddit('Screamo')]
gospel = [reddit.subreddit('gospel'), reddit.subreddit('Gospelmusic')]
popular = [reddit.subreddit('popular'), reddit.subreddit('Music')]
#open file of artists

titles_genre = [["Hip Hop Artists", hip_hop],["R&B Musicians", rb],["Country Musicians", country],
          ["Heavy Metal Bands", heavy_metal],["Rock Musicians", rock_music],
          ["Dance Pop Artists", dance_pop],["Electro House Artists",electro_house],
          ["Alternative Rock Artists", alt_rock],
          ["Indie Pop Artists", indie_pop],
          ["Christian Artists", christian],
          ["Instrumental Bands", instrumental],["Jazz Musicians", jazz],
          ["Latin Pop Artists", latin],
          ["1950s Music Artists", music_1950s],["1960s Music Artists", music_1960s], 
          ["Soul Musicians", soul], 
          ["Reggae Musicians", reggae],
          ["Grunge Bands", grunge], ["Screamo Bands", screamo],
          ["Gospel Bands", gospel], ["Popular", popular],["Music",music]]
final = []
with open('updated_artists.csv', 'r', newline='') as csvf:
    re = csv.reader(csvf)
    
    for row in re:
        final += [row]
        #print(row)
# store artists in dictionary by genre inputs a 2d list returns dictionary
def artists_by_genre(artists):
    artists_genre = {}
    for x in range(len(final)):
        artists_genre[titles[x]] = final[x]
    return artists_genre
artists_dict = artists_by_genre(final)

# finds genre of an artists    
def artist_genre(artist,artists_dict):
    for k, v in artists_dict.items():
        if isinstance(v, list) and artist in v:
            return k
    return "Artist is not stored"
# returns subreddits used to scrape for string genre
def genre_subreddit(genre, titles_genre):
    for x in range(len(titles_genre)):
        if genre == titles_genre[x][0]:
            return titles_genre[x][1]
    return "Incorrect Input"
#print(genre_subreddit(artist_genre("Travis Scott")))
# pulling all comments from relevant subreddits
# if name = True, attach name at the front of comments
def pull_comments(genre, artist, nameneed=False):
    all_comments = []
    for x in genre:
        all_id = []
        for y in x.search(artist, limit=None):
            all_id += [y.id]
        print(all_id)
        for y in all_id:
            submissin = reddit.submission(id=y)
            submissin.comments.replace_more(limit=0)
            for comment in range(len(submissin.comments[:100])):
                if isinstance(comment, MoreComments):
                    continue
                get_com = submissin.comments[comment].body
                all_comments += [get_com]
    if nameneed == True:
        return itertools.chain([name], all_comments)
    else:
        return all_comments

#takes a list of comments and returns a list of all words (flatten into a 1d list)
def parse_and_flatten(comments):
    listofstrs = []
    for comment in comments:
        listofstrs += comment.split()
    return listofstrs
        
#print(pull_comments(hip_hop, "Travis Scott", name=True))

#subreddit = reddit.subreddit('Music')
#for submission in subreddit.search("Travis Scott", limit=None):
#    print(submission.title, submission.id)
#print(pull_comments(hip_hop, "Travis Scott"))
#process for key terms only
#create score
#return value