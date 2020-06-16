from tkinter import filedialog
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import random
import artist_list
from dic import dictionary
import alg
import gather_artists
import redditscrape
import random
def start():
    ''' starts the main window for the program'''
# ---------------------------------------------------------------------------------------------------------------------------------- #

    def writer1():

        def go(): 
            index = part1(artist.get(), subr.get())
            if index > 0:
                if index > 0.85:
                    finalmsg = artist.get() + " is very popular at r/" + subr.get() + "!"
                elif index > 0.5:
                    finalmsg = artist.get() + " is pretty popular at r/" + subr.get() + "!"
                else:
                    finalmsg = artist.get() + " is not as popular but generally liked at r/" + subr.get() + "."
            else:
                if index < -0.85:
                    finalmsg = artist.get() + " is widely disliked r/" + subr.get() + "."
                elif index < -0.5:
                    finalmsg = artist.get() + " is not as popular at r/" + subr.get() + "."
                else:
                    finalmsg = artist.get() + " is not as popular but generally disliked at r/" + subr.get() + "."

            msg2 = "Popularity index: " + str(index)
            
            messagebox.showinfo("Final result", finalmsg + "\n"+ msg2)
            root.destroy()
            
        root = Tk()
        root.title("Option 1")
        root.configure(background='powder blue')
        
        l1 = Label(root, text="Check how popular your favorite artist is in a certain subreddit", font="Arial 14")
        l1.grid(sticky="W", row=0, column=1, columnspan=3, pady=10, ipadx=20)
        l1.configure(background='steel blue')
        
        l3 = Label(root, text="Write your artist's full name (i.e., Travis Scott).", font="Arial 12")
        l3.grid(sticky="W", row=2, column=1, pady=10)
        l3.configure(background='powder blue')

        l4 = Label(root, text="Write your subreddit full name (i.e., AskReddit).", font="Arial 12")
        l4.grid(sticky="W", row=3, column=1, pady=10)
        l4.configure(background='powder blue')

        st1 = ""
        artist = Entry(root, width=20, textvariable=st1)
        artist.grid(row=2, column=3, pady=10)

        st2 = ""
        subr = Entry(root, width=20, textvariable=st2)
        subr.grid(row=3, column=3, pady=10)

        b1 = Button(root, text="go!", command=go,font="Arial 14")
        b1.grid(sticky="e", row=4, column=1, pady=10)

# ---------------------------------------------------------------------------------------------------------------------------------- #

    def writer2():

        def go(): 
            index = part2(artist.get())
            if index > 0:
                if index > 0.85:
                    finalmsg = artist.get() + " is very popular on Reddit!" 
                elif index > 0.5:
                    finalmsg = artist.get() + " is pretty popular on Reddit!" 
                else:
                    finalmsg = artist.get() + " is not as popular but generally liked on Reddit." 
            else:
                if index < -0.85:
                    finalmsg = artist.get() + " is widely disliked on Reddit." 
                elif index < -0.5:
                    finalmsg = artist.get() + " is not as popular on Reddit" 
                else:
                    finalmsg = artist.get() + " is not as popular but generally disliked on Reddit." 

            msg2 = "Popularity index: " + str(index)
            
            messagebox.showinfo("Final result", finalmsg + "\n"+ msg2)
            root.destroy()
            
        root = Tk()
        root.title("Option 2")
        root.configure(background='powder blue')
        
        l1 = Label(root, text="Check how popular your favorite artist is throughout Reddit", font="Arial 14")
        l1.grid(sticky="W", row=0, column=1, columnspan=3, pady=10, ipadx=30)
        l1.configure(background='steel blue')
        
        l3 = Label(root, text="Write your artist's full name (i.e., Travis Scott).", font="Arial 12")
        l3.grid(sticky="W", row=2, column=1, pady=10)
        l3.configure(background='powder blue')

        st1 = ""
        artist = Entry(root, width=20, textvariable=st1)
        artist.grid(row=2, column=3, pady=10)

        b1 = Button(root, text="go!", command=go,font="Arial 14")
        b1.grid(sticky="e", row=4, column=1, pady=10)
# ---------------------------------------------------------------------------------------------------------------------------------- #

    def writer3():

        def go():
            artists = part3(subr.get(), genre.get())
            finalmsg = "The top 10 " + genre.get() + " artists at " + subr.get() + " are: \n" + artists
            messagebox.showinfo("Final result", finalmsg)
            root.destroy()
            
        root = Tk()
        root.title("Option 3")
        root.configure(background="powder blue")
        
        l1 = Label(root, text="Choose a genre and see the top 10 artists at a subreddit", font="Arial 14")
        l1.grid(sticky="W", row=0, column=1, pady=10, columnspan=3, ipadx=60)
        l1.configure(background="steel blue")

        l2 = Label(root, text="Choose your genre.", font="Arial 12")
        l2.grid(sticky="W", row=1, column=1, pady=10)
        l2.configure(background="powder blue")
        
        l3 = Label(root, text="Write your subreddit full name (i.e., AskReddit).", font="Arial 12")
        l3.grid(sticky="W", row=3, column=1, pady=10)
        l3.configure(background="powder blue")

        genre = ttk.Combobox(root, values="Hip Hop Artists","R&B Musicians","Country Musicians",
                                            "Heavy Metal Bands","Rock Musicians","Dance Pop Artists",
                                            "Electro House Artists","Alternative Rock Artists","Indie Pop Artists",
                                            "Christian Artists", "Instrumental Bands","Jazz Musicians", "Latin Pop Artists",
                                            "1950s Music Artists","1960s Music Artists", "Soul Musicians", 
                                            "Reggae Musicians", "Grunge Bands", "Screamo Bands", "Gospel Bands"])
        genre.grid(row=1, column=3, pady=10)

        st2 = ""
        subr = Entry(root, width=20, textvariable=st2)
        subr.grid(row=3, column=3, pady=10)

        b1 = Button(root, text="go!", command=go,font="Arial 14")
        b1.grid(sticky="W", row=4, column=2, pady=10)

# ---------------------------------------------------------------------------------------------------------------------------------- #

    def writer4():

        def go():
            artists = part4(genre.get())
            finalmsg = "The top 10 " + genre.get() + " artists in Reddit are: \n " + artists
            messagebox.showinfo("Final result", finalmsg)
            root.destroy()
            
        root = Tk()
        root.title("Option 3")
        root.configure(background="powder blue")
        
        l1 = Label(root, text="Choose a genre and see the top 10 artists throughout Reddit", font="Arial 14")
        l1.grid(sticky="W", row=0, column=1, pady=10, columnspan=3, ipadx=60)
        l1.configure(background="steel blue")

        l2 = Label(root, text="Choose your genre.", font="Arial 12")
        l2.grid(sticky="W", row=1, column=1, pady=10, ipadx=50)
        l2.configure(background="powder blue")

        genre = ttk.Combobox(root, values="Hip Hop Artists","R&B Musicians","Country Musicians",
                                            "Heavy Metal Bands","Rock Musicians","Dance Pop Artists",
                                            "Electro House Artists","Alternative Rock Artists","Indie Pop Artists",
                                            "Christian Artists", "Instrumental Bands","Jazz Musicians", "Latin Pop Artists",
                                            "1950s Music Artists","1960s Music Artists", "Soul Musicians", 
                                            "Reggae Musicians", "Grunge Bands", "Screamo Bands", "Gospel Bands"])
        genre.grid(row=1, column=3, pady=10)

        b1 = Button(root, text="go!", command=go,font="Arial 14")
        b1.grid(sticky="W", row=4, column=2, pady=10)

    def a():
        artist_list.ls()      

# ---------------------------------------------------------------------------------------------------------------------------------- #

    main = Tk()
    main.title("final project 591")
    
    main.configure(background='powder blue')
    
    l1 = Label(main, text="Checking your artist's popularity", font="Arial 20")
    l1.grid(sticky="W", row=0, column=1, columnspan=2, ipadx=110, ipady=5, pady=10)
    l1.configure(bg = "steel blue")
    
    l2 = Label(main, text="Please choose your option:", font="Arial 14")
    l2.grid(sticky="W", row=2, column=1, ipady=5)
    l2.configure(bg = "powder blue")

    b1 = Button(main, text="I want to choose an artist and see his/her popularity in a certain subreddit.", command=writer1)
    b1.grid(sticky="EW", row=3, column=1, ipadx=10, ipady=5, pady=10)
    
    b2 = Button(main, text="I want to choose an artist and see his/her popularity overall in Reddit.", command=writer2)
    b2.grid(sticky="EW", row=4, column=1, ipadx=27, ipady=5, pady=10)
    
    b3 = Button(main, text="I want to find the top 10 artists in a certain genre in a certain subreddit.", command=writer3)
    b3.grid(sticky="EW", row=5, column=1, ipadx=19, ipady=5, pady=10)
    
    b4 = Button(main, text="I want to find the top 10 artists in a certain genre overall in Reddit.", command=writer4)
    b4.grid(sticky="EW", row=6, column=1, ipadx=35, ipady=5, pady=10)

    b5 = Button(main, text="See our list of artists", command=a)
    b5.grid(sticky="N", row=7, column=1, ipadx=10, ipady=5, pady=10)
    
    mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------- #

# actual code starts now! 

def part1(name, subr):
    ''' input: artist name and subreddit name
        output: a number
    '''
    subred = redditscrape.reddit.subreddit(subr)
    comments = redditscrape.pull_comments([subred], name, nameneed = False)
    # you need to put HERE the code that will get all of the comments. By the end you should have something
    # (maybe a list) of comments so you can do a for loop and run the algortithm in each comment. Since you
    # will have a list with all the right comments (aka for the right person), we don't need to check if the
    # comments are right for each artist. Therefore we'll only pass the comments.
    # this is an example of how things would look like:
    #comments = ["I think 21 Pilots is awful and offensive",
    #            "I think 21 Pilots is amazing and brilliant",
    #            "I think 21 Pilots is upbeat but inconsistent."]
    # you will put the entire list on the algorithm. It will do the job for you.
    index = alg.artist_alg(comments)
    return round(index, 2)

def part2(name):
    ''' input: artist name
        output: a number
    '''
    genre = redditscrape.artist_genre(name, redditscrape.artists_dict)
    genre2 = redditscrape.genre_subreddit(genre, redditscrape.titles_genre)
    comments = redditscrape.pull_comments(genre2, name, nameneed=False)
    # you need to put HERE the code that will get all of the comments. By the end you should have something
    # (maybe a list) of comments so you can do a for loop and run the algortithm in each comment. Since you
    # will have a list with all the right comments (aka for the right person), we don't need to check if the
    # comments are right for each artist. Therefore we'll only pass the comments.
    # this is an example of how things would look like:
    #comments = ["I think 21 Pilots is awful and offensive",
    #            "I think 21 Pilots is amazing and brilliant",
    #            "I think 21 Pilots is upbeat but inconsistent."]

    # you will put the entire list on the algorithm. It will do the job for you.
    index = alg.artist_alg(comments)
    return round(index, 2)

def part3(genre, subr):
    ''' input: chosen genre and subreddit name.
        output: a string containing the names of top 10 artists
    '''
    artists = scrapereddit.artists_dict[genre]
    sample_artists = random.sample(artists, 20)
    list_of_list = []
    for x in sample_artists:
        list_of_list += redditscrape.pull_comments([subr], x, nameneed=True)
    # for each genre, you will have to grab a certain amount of artists (cap it at 20 i guess) (decide them at your will)
    # and run the artist algorithm for each one of them. I am treating this as if you would have
    # a list of lists (so it would look something like this:)
    list_of_lists = [["21 Pilots", "I think 21 Pilots is awful and offensive", "I think 21 Pilots is amazing and brilliant"],
                   ["Taylor Swift", "Taylor Swift's songs are cool!", "I hate Taylor Swift"],
                   ["Bob Marley", "Bob Marley's songs are so calm", "Bob Marley seems unkind"]]
    # you will have to change this accordingly (aka if you don't use a list of lists).
    # but REMEMBER: part 1 takes a list of comments (and it NEEDS TO HAVE THE ARTIST'S NAME AS FIRST ITEM ON EACH ROW).
    # if you want to send something else you will have to change part 1 as well!

    s = alg.genre_alg(list_of_list)
    return(s)

def part4(genre):
    ''' input: chosen genre.
        output: a string containing the names of top 10 artists
    '''
    artists = scrapereddit.artists_dict[genre]
    sample_artists = random.sample(artists, 20)
    list_of_list = []
    genre2 = redditscrape.genre_subreddit(genre, redditscrape.titles_genre)
    for x in sample_artists:
        list_of_list += redditscrape.pull_comments(genre2, x, nameneed=True)
    # for each genre, you will have to grab a certain amount of artists (cap it at 20 i guess) (decide them at your will)
    # and run the artist algorithm for each one of them. I am treating this as if you would have
    # a list of lists (so it would look something like this:)
    list_of_lists = [["21 Pilots", "I think 21 Pilots is awful and offensive", "I think 21 Pilots is amazing and brilliant"],
                   ["Taylor Swift", "Taylor Swift's songs are cool!", "I hate Taylor Swift"],
                   ["Bob Marley", "Bob Marley's songs are so calm", "Bob Marley seems unkind"]]
    # you will have to change this accordingly (aka if you don't use a list of lists).
    # but REMEMBER: part 1 takes a list of comments (and it NEEDS TO HAVE THE ARTIST'S NAME AS FIRST ITEM ON EACH ROW).
    # if you want to send something else you will have to change part 1 as well!

    s = alg.genre_alg(list_of_list)
    return(s)


start()
