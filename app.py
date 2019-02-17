#Dream Broker Programming Assignment: Text Analyzer
#Assignment done by: Humayun Rashid
#Email: humayun.rashid@tuni.fi

#Structure of the code is mention below.
#A small REST web service in localhost has been implemented, which expose an API endpoint to analyze a given text.
#First, A class has been created to determine string details that will be returned against POST method.
#Next, a rest API based on top of Flask has been implmented.
#Necessary comments has been added for all variables and functions.

class StringDetails:
    """ A class contains different method to determine text length, word count, character count """ 
   
    def __init__(self,data):
        """ Class Constructor """
        
        self.data=data

    def text_length (self,data):
        """ Method to determine text length with and without space"""

        total_alphabet = 0                    #Variable to count total alphabet in the string
        space = 0                             #Variable to count number of spaces in the string

        #Determine total number of strings with and without spaces.
        for alphabet in (str(self.data["text"])):
            if alphabet != " ":
                total_alphabet +=1
            else:
                total_alphabet +=1
                space +=1

        withSpaces = total_alphabet           #Total number of alphabet with space
        withoutSpaces = total_alphabet-space #Total number of alphabet without space

        return withSpaces,withoutSpaces       #Return the values

    def word_count(self,data):
        """ Method to determine total words"""
        
        word_count = 0                        #Variable to count words in the string
        new_string= ""                         #Varaible to store new string after eliminating spcial characters from string
                                   

        #Creating a list of lower cases aplhabets and a single space
        alphabet_list=list()

        #Add lowercase alphabets to the list
        for letter in range(97,123):
            alphabet_list.append(chr(letter))
            
        #Add numerical values to the list
        for numerical in range (10):
            alphabet_list.append (chr(letter))
            
        # A space will be added with the list    
        alphabet_list.append(" ")

        #Compare the characters of the strings with the previous list, remove the special characters , only characters and space will remian
        #and store it to the new string variable.
        for elements in (str(data["text"])):
            if elements or elements.lower() in alphabet_list:
                new_string=new_string +elements
                
        split_string = (new_string).split()   #Split the new strings and make a list 

        #Count the word , store the value in word count and return the value
        for elements in split_string:
            word_count+=1
        return word_count                     #Return the value

    def character_count(self,data):
        """ A method to calculate the characters"""
        
        #Creating a list of lower cases aplhabets
        alphabet_list = list()
        for letter in range(97,123):
            alphabet_list.append(chr(letter))
            
        char_list = [alphabet.lower() for alphabet in (str(data["text"])) if alphabet.lower() in alphabet_list]   #List comprehension to eliminates all special characters and spaces
        char_list.sort()                                                                                          # Sort the list

        #Populate the Character dictionary with characters and count
        char_dict = dict()                              
        for alphabet in char_list:
            if alphabet not in char_dict:
                char_dict[alphabet] =0
            if alphabet in char_dict:
                char_dict[alphabet] = char_dict[alphabet]+1
                
        #Create the final output and return the value
        final_output=list()                     
        for key,value in char_dict.items():
            new_dict= dict()
            new_dict[key]=value
            final_output.append(new_dict)
        return final_output

    
#Create a server with Flask
    
#Import modules
from flask import Flask, jsonify, request

app = Flask(__name__)                #Create the Flask App
app.config['JSON_SORT_KEYS'] = False #Set the sorting value of JSON to false

tasks =list()                        #List to store the data

#Create the specific route and method (Post)
@app.route('/analyze', methods=['POST'])

def post_task():
    """ Defining a function to post new data and recevies expected return values"""

    #Request JSON data from server
    data = {'text': request.json['text']}
    
    #Create object with data to determine string details
    new_data = StringDetails(data)                         #Create new object with StringDetails class
    withSpaces,withoutSpaces = new_data .text_length(data) # Determine Textlength
    total_word = new_data.word_count(data)                 # Determine the wordcount
    total_character= new_data.character_count(data)        #Determine the total characters

    #return the data is JSON format
    return jsonify({"textLength":{"withSpaces":withSpaces,
                                  "withoutSpaces":withoutSpaces},
                    "wordCount":total_word,
                    "characterCount":total_character})

#Run the server
if __name__ == '__main__':
    app.run(debug=True)




