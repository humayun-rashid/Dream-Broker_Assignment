#Test file to check the functinality of the app.py
#Developed by: Humayun Rashid
#Email: humayun.rashid@tuni.fi

#Import the modules
import unittest
import requests
import json
import app

class DbAppTest(unittest.TestCase):
    """Create a class for testing"""
    def test(self):
        #A test data to check the different functions and method 
        test_data = {"text":"This TEXT contain CAPITAL, small   AlPhaBEts with Numerics 1, 2, 3 and Special characters ! ! !* * * for Testin purposes"}

        #server url for local Host
        server_url='http://127.0.0.1:5000/analyze'

        #Request for POST operation from server
        test_case = requests.post(server_url,headers={'Content-Type': 'application/json'}, data=json.dumps(test_data))

        #Get header information
        header_dict = test_case.headers

        #Compare status ode if it is 200 or something else. 200 means server is working fine
        self.assertEqual(test_case.status_code, 200)

        #Create a object from the class of main app.py file to test various string operation.
        new_data = app.StringDetails(test_data )

        #Get Text length with and without spaces
        withSpaces,withoutSpaces = new_data .text_length(test_data)

        #Get total word ciuts 
        total_word = new_data.word_count(test_data )

        #Get total characters amount in list 
        total_character= new_data.character_count(test_data )

        #Compare with the pretested result
        self.assertEqual(withSpaces,120)         #Check text length with spaces
        self.assertEqual(withoutSpaces,97)       #Check text length without spaces
        self.assertEqual(total_word,22)          #Check total word count 
        self.assertEqual(len(total_character),19)#Check the length of the list that contains total word count 

#Run the program        
if __name__ == '__main__':
    unittest.main()
