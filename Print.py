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
