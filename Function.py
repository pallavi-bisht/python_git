#TIY 131

def display_message():
    print("I am reading function chapter in python.")

display_message()

def favorite_book(title):
    print(f"MY favorite book is {title}")

favorite_book("Maths")    

#TIY 136

def make_shirt(size,msg):
    print(f"The size of short is {size} and message is {msg}")

make_shirt(34,'I am a liver')    
make_shirt(size=32,msg='I am a pancreas')

def make_shirt_2(size='L' , msg='I love python'):
    print(f"The size of short is {size} and message is {msg}")

make_shirt_2(size='M')
make_shirt_2()
make_shirt_2(msg='I love Tableau')

#TIY 141
def make_album(artist_name,album_name,no_of_songs=None):
    album={}
    if no_of_songs:
        album['artist name']=artist_name
        album['album name']=album_name
        album['count of songs']= no_of_songs

        #OR album={'artist name':artist_name,'album name':album_name,'count of songs': no_of_songs}
    else:
        album['artist name']=artist_name
        album['album name']=album_name
      
    return album    

#New_album= make_album('pallavi','Good lives',20)
#print(New_album)
#New_album_2= make_album('Gulnaar','Life lessons')
#print(New_album_2)

while True:
 artist_name=input("Enter artist name\n(Enter q if want to quit)\n")
 if artist_name=='q':
    break
 album_name=input("Enter album name\n(Enter q if want to quit)\n")
 if album_name=='q':
    break
 
 New_album_3=make_album(artist_name,album_name)
 print(New_album_3)
 
 











