import google.generativeai as genai
import os
api_key= "AIzaSyD7AW1SBOgJAXcCeYe8w920U2ChcRoab30"
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content(input())
print(response.text)