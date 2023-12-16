import mysql.connector
import tkinter as tk
from tkinter import filedialog, PhotoImage
from ultralytics import YOLO
import easyocr
import os
import re
import shutil


# model 
model = YOLO("yolov8s.pt","v8")


# browse image function & take file path
def browse_image():
    global image_path
    image_path = filedialog.askopenfilename()
    print("Selected Image:", image_path)
        
    extract_image_name(image_path)



# Extract Image name
def extract_image_name(image_path):

    global image_name
    image_name = os.path.basename(image_path)
    print(image_name)
    get_fruit_info_img(image_name, image_path)


# delete predict folders

def delete_all_folders():
    folder_path = 'D:/Personal Projects/Nutrition Web-App/runs/detect/'
    items = os.listdir(folder_path)

    # Iterate through each item
    for item in items:
        item_path = os.path.join(folder_path, item)

        # Check if the item is a folder
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"Deleted folder: {item_path}")



# destroy imagebutton, entry, labels, button, etc.
 
def blast():
    Entry1.destroy()
    Label_name.destroy()
    Label_or.destroy()
    Get_Button.destroy()
    image_button.destroy()



# get the name of fruit entered by user

def get_name():
    fruit_name1 = Entry1.get()

    if Entry1 != '':

        blast()
        get_fruit_info_name(fruit_name1)

    else:
        print("No Input's Detected !!")



# fruit detection by image
        
def get_fruit_info_img(image_name, image_path):
    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0417",
        database="fruitsdata"
    )

    cursor = connection.cursor()


    # detecting 
    detect_o = model.predict(source=image_path,conf=0.25,save=True)

    print(detect_o)
    print(detect_o[0])

    reader = easyocr.Reader(['en'])
    n_result = reader.readtext(f'D:\\Personal Projects\\Nutrition Web-App\\runs\\detect\\predict\\{image_name}',detail=0)
    name = n_result[0][:-4]

    alpha_name = ''.join(char for char in name if char.isalpha())

    print(alpha_name)

    print(name)

    query = f"SELECT fruit_name, calories, protein, cabs, fiber, vitamins, fat, sugar FROM nutrition WHERE fruit_name = '{alpha_name}'; "
    cursor.execute(query)

    cur_result = cursor.fetchone()
    cursor.close()
    connection.close()

    print("Cursor Result", cur_result)
    

    if cur_result:

        blast()

        fruit_name2, calories, protein, cabs, fiber, vitamins, fat, sugar = cur_result

        label_img_2 = tk.Label(root, bg="dark blue", font=("JetBrains", 20), fg="white",
        text=f"Nutrients: \n\nFruit Name: {fruit_name2}\nCalories: {calories}\nProtein: {protein}\nCarbohydrates: {cabs}\nFiber: {fiber}\nVitamins: {vitamins}\nFat: {fat}\nSugar: {sugar}")
        label_img_2.place(x = 480, y = 150)


        # item_found()

    else:
        label_img_3 = tk.Label(root, text=f"{name} Not Found")
        label_img_3.place(x = 50, y = 50)

    delete_all_folders()



# fruit detection by name 

def get_fruit_info_name(fruit_name1):

    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",  # usually localhost if the database is on your machine
        user="root",
        password="0417",
        database="fruitsdata"
    )

    cursor = connection.cursor()

    query = f"SELECT fruit_name, calories, protein, cabs, fiber, vitamins, fat, sugar FROM nutrition WHERE fruit_name = '{fruit_name1}'"
    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        fruit_name, calories, protein, cabs, fiber, vitamins, fat, sugar = result
        # print(f"Fruit: {fruit_name}\nCalories: {calories}\nProtein: {protein}\nCarbohydrates: {cabs}\nFiber: {fiber}\nVitamins: {vitamins}\nFat: {fat}\nSugar: {sugar}")
        label_name_2 = tk.Label(root, bg="dark blue", font=("JetBrains", 20), fg="white",
        text=f"Nutrients: \n\nFruit Name: {fruit_name}\nCalories: {calories}\nProtein: {protein}\nCarbohydrates: {cabs}\nFiber: {fiber}\nVitamins: {vitamins}\nFat: {fat}\nSugar: {sugar}")
        label_name_2.place(x = 480, y = 150)
        # item_found()

    else:
        # print(f"{fruit_name} Not Found !")
        label_name_3 = tk.Label(root, text=f"{fruit_name1} Not Found")
        label_name_3.place(x = 50, y = 50)



# main 

if __name__ == "__main__":

    # window creation

    root = tk.Tk()
    root.state("zoomed")
    root.title("Nutrition Detection")
    root.config(bg="dark blue")


    # First label

    Label_name = tk.Label(root, text="Fruit Name : ", fg="white", bg="dark blue", font=("Fira code", 25, "bold"))
    Label_name.place(x = 930, y = 205)


    # Input Box

    Entry1 = tk.Entry(root, textvariable=tk.StringVar, bg="sky blue", fg="black", font="JetBrains", justify="center", borderwidth=20, relief="flat")
    Entry1.place(x = 860, y = 290, height=50, width=350)


    # Submit Button

    Get_Button = tk.Button(root, text="SUBMIT", command=get_name, fg="white", bg="blue", font=("JetBrains"), justify="center")
    Get_Button.place(x = 930, y = 415, width=200)


    # image button

    upload_image = tk.PhotoImage(file='C:\\Users\\Hp\\Downloads\\drop or upload.png')

    image_button = tk.Button(root, image=upload_image, command=browse_image)
    image_button.place(x = 40, y = 150)


    # OR lable

    Label_or = tk.Label(root, text="OR", fg="white", bg="dark blue", font=("Fira code", 25, "bold"))
    Label_or.place(x = 725, y = 300)


    root.mainloop()