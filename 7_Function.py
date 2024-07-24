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
 

 #TIY 146

def show_messages(msgs):
    for i in msgs:
        print(f"Hello {i}!")
msgs_list=["dgjed",'asjghdq','wdjbkdj']
show_messages(msgs_list)


def print_msgs(msgs):
    sent_messages=[]
    while msgs:
        i=msgs.pop() 
        print(f" Sent message {i}!\n")
        sent_messages.append(i)
    return sent_messages
def show_messages(a,b):        
    print(a)
    print(b)

msgs_list=["how",'hi','hello']
sent_messages=print_msgs(msgs_list)
show_messages(msgs_list,sent_messages)
#to send only copy of list
def print_msgs(msgs):
    sent_messages=[]
    while msgs:
        i=msgs.pop() 
        print(f" Sent message {i}!\n")
        sent_messages.append(i)
    return sent_messages
def show_messages(a,b):        
    print(a)
    print(b)

msgs_list_1=["abc",'pqr','lmn']
sent_messages=print_msgs(msgs_list_1[:])
show_messages(msgs_list_1,sent_messages)

#TIY 149
def make_snadwitch(*arg):
    for i in arg: #arg is tuple by default with one *
        print(f" Making {i} sandwitch now.\n")

make_snadwitch('veg','peas','corn')


def build_profile(f_name,l_name,**info):  #info becomes dictionary  with ** and can have multiple arguments
    info['first_name']=f_name
    info['last_name']=l_name
    return info

abc=build_profile('pallavi', 'bisht',age=30,address='kharadi')
print(abc)


#TIY 154 module

import Print  as p

msgs_list=["how",'hi','hello']
sent_messages=p.print_msgs(msgs_list)
p.show_messages(msgs_list,sent_messages)

from  Print  import print_msgs as p,show_messages as s

msgs_list=["jhs",'wms','wms']
sent_messages=p(msgs_list)
s(msgs_list,sent_messages)







 











