# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import string
filename = "/home/pari/Flickr8k_text/Flickr8k.token.txt"
file = open(filename, 'r')
doc = file.read()
descriptions = dict()
for line in doc.split('\n') :
    # split line by white space
    if line.isspace():
        print(line)
    tokens = line.split()
    # take the first token as image id, the rest as description
    
    if tokens:
        image_id=tokens[0]
        image_desc=tokens[1:]
    #image_desc=tokens[1:]
    # extract filename from image id
    
        image_id = tokens[0].split('.')[0]
    #print(image_id)
    
    # convert description tokens back to string
        image_desc = ' '.join(image_desc)
        if image_id not in descriptions:
            descriptions[image_id] = list()
        descriptions[image_id].append(image_desc)
    #print("kkk")
for key, desc_list in descriptions.items():
    for i in range(len(desc_list)):
        desc = desc_list[i]
        # tokenize
        desc = desc.split()
        # convert to lower case
        desc = [word.lower() for word in desc]
        # remove punctuation from each token
        desc = [ word  for word in desc if word not in string.punctuation]
        # remove hanging 's' and 'a'
        #desc = [word for word in desc if len(word)>1]
        # remove tokens with numbers in them
        desc = [word for word in desc if word.isalpha()]
        # store as string
        desc_list[i] =  ' '.join(desc)
#print(descriptions)
        f=open("/home/pari/Flickr8k_text/descriptions.txt",'w')
for key,desc_list in descriptions.items():
    f.write(key+" "+str(desc_list)+"\n")
f.close()
