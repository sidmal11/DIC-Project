#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy


# In[2]:


from tweepy.auth import OAuthHandler


# In[3]:


from tweepy import Stream


# In[4]:


from tweepy.streaming import StreamListener


# In[5]:


import socket


# In[6]:


import json


# In[7]:


# Set up your credentials from http://apps.twitter.com
consumer_key    = 'JLaJKA8CdU38Wo67R2yMZwPJF'
consumer_secret = 'iEN9Nxewd3vW2kGfED2cYmhWVHXZuKEEgrSK9WeYzcpVdXi3hW'
access_token    = '1440784724-chPD5AZ1HWZUMuVuUXL9d02U0MCTF4057UjaQst'
access_secret   = '2ZID8wItc2GAYB3YxCgGnDYmIE8m5f124zKbXMQp3Vf7w'
bearer_token    = 'AAAAAAAAAAAAAAAAAAAAAOyrIAEAAAAANGi6pc74armMILy%2FvxMyE828V2w%3DiLF3g0hLLm9gV4FVzYRDZhUr287VgxDuScd7l4fujoQxjnxf7E'


# In[8]:


class TweetsListener(StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            msg = json.loads( data )
            print( msg['text'].encode('utf-8') )
            self.client_socket.send( msg['text'].encode('utf-8') )
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


# In[9]:


def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track=['football'])


# In[10]:


if __name__ == "__main__":
    s = socket.socket()         # Create a socket object
    host = "127.0.0.1"     # Get local machine name
    port = 5555                 # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    print("Listening on port: %s" % str(port))

    s.listen(5)                 # Now wait for client connection.
    c, addr = s.accept()        # Establish connection with client.

    print("Received request from: " + str(addr))

    sendData(c)


# In[ ]:




