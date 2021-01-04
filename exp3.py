#adding the location of images to directory/path
import os
path =r'C:\Users\Vasu\Desktop\FAI\EXP3'
os.environ['PATH'] += ':'+path

# importing deepFace module for analysis
from deepface import DeepFace

nCustomers=0
nMale=0
nFemale=0
nHappy=0
nSad=0


#taking image input
image_path=['image1.jpeg', 'image2.jpeg', 'image3.jpeg', 'image4.jpeg', 'image5.jpeg', 'image6.jpeg']

for imgPath in image_path:
    data = DeepFace.analyze(imgPath)
    if (data["gender"]=='Man'):
        nMale+=1
    elif (data["gender"]=='Woman'):
        nFemale+=1
        
    if (data["dominant_emotion"]=='happy'):
        nHappy+=1
    elif (data["dominant_emotion"]=='sad'):
        nSad+=1
    nCustomers+=1
    
print("\nNumber of customers visited:", nCustomers)
print("Number of males customer:", nMale)
print("Number of females customer:", nFemale)
print("Number of happy customer:", nHappy)
print("Number of sad customer:", nSad)
