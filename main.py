import mysql.connector
import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
import easyocr
import os
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
    folder_path = 'E:/Nutrition Web-App/runs/detect/'
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
    suggest_diet_button.destroy()



# get the name of fruit entered by user

def get_name():
    fruit_name1 = Entry1.get()

    if Entry1 != '':

        blast()
        get_fruit_info_name(fruit_name1)

    else:
        print("No Input's Detected !!")



# skinny type 
def skinny():

    # high calorie
    def shigh_calorie():
        
        high_calorie_diet1 = ["Whole grains", "Lean proteins(chicken, fish, tofu)", "Healthy fats(avocado, nuts, olive oil)", "Dairy products", "Fruits and vegetables", "Protein shakes", "Snack on nuts and seeds"]

        label2 = tk.Label(root, text="High Calorie Diet\nFor Skinny Body Type :\n", fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label2.place(x = 900, y = 100)

        
        high_calorie_diet_str = "\n".join(high_calorie_diet1)

        label_high = tk.Label(root, text=high_calorie_diet_str, wraplength=250, justify='left', fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label_high.place(x = 900, y = 150)


    # protein rich
    def sprotein_rich():
        protein_rich_diet1 = ["Lean meats (chicken, turkey, lean beef)", "Fish and seafood", "Eggs", "Dairy products (Greek yogurt, cheese)", "Legumes (beans, lentils)", "Quinoa", "Protein bars"]


        label3 = tk.Label(root, text="Protein Rich Diet\nFor Skinny Body Type :\n", fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label3.place(x = 900, y = 100)

        
        high_calorie_diet_str = "\n".join(protein_rich_diet1)

        label_high = tk.Label(root, text=high_calorie_diet_str, wraplength=250, justify='left', fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label_high.place(x = 900, y = 150)



    # high calorie button
    highcal_button = tk.Button(root, text="High Calorie Diet", fg="yellow", bg="red",
                               command=shigh_calorie,
                                font=("JetBrains Mono", 17), justify="center")
    highcal_button.place(x = 450, y = 180, height=55, width=300)


    # protein rich button
    prorich_button = tk.Button(root, text="Protein Rich Diet", fg="yellow", bg="red",
                               command=sprotein_rich,
                                font=("JetBrains Mono", 17), justify="center")
    prorich_button.place(x = 450, y = 285, height=55, width=300)



# fit type
def fit():

    # high calorie
    def fhigh_calorie():
        
        high_calorie_diet2 = ["Lean meats (chicken, turkey, lean beef)", "Fish and seafood", "Eggs", "Dairy products (Greek yogurt, cheese)", "Whole grains (brown rice, quinoa)", "Healthy fats (avocado, nuts, olive oil)", "Fruits and vegetables", "Protein shakes"]


        label2 = tk.Label(root, text="High Calorie Diet\nFor Fit Body Type :\n", fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label2.place(x = 900, y = 100)

        
        high_calorie_diet_str = "\n".join(high_calorie_diet2)

        label_high = tk.Label(root, text=high_calorie_diet_str, wraplength=250, justify='left', fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label_high.place(x = 900, y = 150)


    # protein rich
    def fprotein_rich():
        protein_rich_diet2 = ["Lean meats (chicken, turkey, lean beef)", "Fish and seafood", "Eggs", "Dairy products (Greek yogurt, cheese)", "Legumes (beans, lentils)", "Quinoa", "Nuts and seeds", "Protein bars"]

        label3 = tk.Label(root, text="Protein Rich Diet\nFor Fit Body Type :\n", fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label3.place(x = 900, y = 100)

        
        fprotein_rich_str = "\n".join(protein_rich_diet2)

        label_high = tk.Label(root, text=fprotein_rich_str, wraplength=250, justify='left', fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label_high.place(x = 900, y = 150)



    # high calorie button
    highcal_button = tk.Button(root, text="High Calorie Diet", fg="yellow", bg="red",
                               command=fhigh_calorie,
                                font=("JetBrains Mono", 17), justify="center")
    highcal_button.place(x = 450, y = 180, height=55, width=300)


    # protein rich button
    prorich_button = tk.Button(root, text="Protein Rich Diet", fg="yellow", bg="red",
                               command=fprotein_rich,
                                font=("JetBrains Mono", 17), justify="center")
    prorich_button.place(x = 450, y = 285, height=55, width=300)



# muscular type
def muscular():
    # high calorie
    def mhigh_calorie():
        
        high_calorie_diet3 = ["Lean meats (chicken, turkey, lean beef)", "Fish and seafood", "Eggs", "Dairy products (Greek yogurt, cheese)", "Whole grains (brown rice, quinoa)", "Healthy fats (avocado, nuts, olive oil)", "Fruits and vegetables", "Protein shakes"]

        label2 = tk.Label(root, text="High Calorie and\nProtein Rich Diet for\nMuscular Body Type :\n", fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label2.place(x = 900, y = 100)

        
        high_calorie_diet_str = "\n".join(high_calorie_diet3)

        label_high = tk.Label(root, text=high_calorie_diet_str, wraplength=250, justify='left', fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label_high.place(x = 900, y = 150)


    # protein rich
    def muscle_building():
        muscle_building_diet = ["High-quality protein sources (chicken, fish, eggs)", "Complex carbohydrates (sweet potatoes, whole grains)", "Healthy fats (olive oil, nuts)", "Vegetables", "Fruits", "Dairy products (Greek yogurt, milk)", "Protein bars"]


        label3 = tk.Label(root, text="Muscle Building Diet\nFor Muscular Body Type :\n", fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label3.place(x = 900, y = 100)

        
        muscle_building_str = "\n".join(muscle_building_diet)

        label_high = tk.Label(root, text=muscle_building_str, wraplength=250, justify='left', fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label_high.place(x = 900, y = 150)



    # high calorie button
    highcal_button = tk.Button(root, text="High Calorie & \nProtein Rich Diet", fg="yellow", bg="red",
                               command=mhigh_calorie,
                                font=("JetBrains Mono", 17), justify="center")
    highcal_button.place(x = 450, y = 180, height=65, width=300)


    # protein rich button
    prorich_button = tk.Button(root, text="Mass Building Diet", fg="yellow", bg="red",
                               command=muscle_building,
                                font=("JetBrains Mono", 17), justify="center")
    prorich_button.place(x = 450, y = 285, height=55, width=300)



# bulk type
def bulk():
    # high calorie
    def bhigh_calorie():
        
        high_calorie_diet4 = ["Lean meats (chicken, turkey, lean beef)", "Fish and seafood", "Eggs", "Dairy products (Greek yogurt, cheese)", "Whole grains (brown rice, quinoa)", "Healthy fats (avocado, nuts, olive oil)", "Fruits and vegetables", "Protein shakes"]

        label2 = tk.Label(root, text="High Calorie Diet\nFor Bulk Body Type :\n", fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label2.place(x = 900, y = 100)

        
        high_calorie_diet_str = "\n".join(high_calorie_diet4)

        label_high = tk.Label(root, text=high_calorie_diet_str, wraplength=250, justify='left', fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label_high.place(x = 900, y = 150)


    # protein rich
    def bmass_building():
        serious_mass_building_diet = ["High-quality protein sources (chicken, fish, eggs)", "Complex carbohydrates (sweet potatoes, whole grains)", "Healthy fats (olive oil, nuts)", "Vegetables", "Fruits", "Dairy products (Greek yogurt, milk)", "Protein bars", "Calorie-dense snacks"]


        label3 = tk.Label(root, text="Serious Mass Building Diet\nFor Bulk Body Type :\n", fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label3.place(x = 900, y = 100)

        
        muscle_building_str = "\n".join(serious_mass_building_diet)

        label_high = tk.Label(root, text=muscle_building_str, wraplength=250, justify='left', fg="black", bg="blue", 
                        font=("JetBrains Mono", 15, "bold"))
        label_high.place(x = 900, y = 150)



    # high calorie button
    highcal_button = tk.Button(root, text="High Calorie Diet", fg="yellow", bg="red",
                               command=bhigh_calorie,
                                font=("JetBrains Mono", 17), justify="center")
    highcal_button.place(x = 450, y = 180, height=55, width=300)


    # protein rich button
    prorich_button = tk.Button(root, text="Protein Rich Diet", fg="yellow", bg="red",
                               command=bmass_building,
                                font=("JetBrains Mono", 17), justify="center")
    prorich_button.place(x = 450, y = 285, height=55, width=300)




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
    n_result = reader.readtext(f'E:\\Nutrition Web-App\\runs\\detect\\predict\\{image_name}',detail=0)
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

    blast()

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
        
        root.config(bg="black")
        label_name_3 = tk.Label(root, text=f"No Fruit found with name : {fruit_name1}", fg="blue", bg="black", font=("JetBrains Mono", 25))
        label_name_3.place(x = 300, y = 300)



# suggest button 
def suggest():
    blast()
    root.config(bg="blue")
    
    suggest_diet_button.destroy()

    # label select body type    
    Label1 = tk.Label(root, text="SELECT YOUR BODY TYPE : ", fg="black", bg="blue", 
                        font=("JetBrains Mono", 17))
    Label1.place(x = 100, y = 100)


    # skinny 
    skinny_button = tk.Button(root, text="SKINNYY", fg="black", bg="skyblue", justify="center",
                              command=skinny,
                                font=("JetBrains Mono", 17))
    skinny_button.place(x = 70, y = 180, height=50, width=250)


    # Fit
    fit_button = tk.Button(root, text="FIT", fg="black", bg="skyblue",
                           command=fit,
                                font=("JetBrains Mono", 17), justify="center")
    fit_button.place(x = 70, y = 260, height=50, width=250)


    # Muscular
    muscular_button = tk.Button(root, text="MUSCULAR", fg="black", bg="skyblue",
                                command=muscular,
                                font=("JetBrains Mono", 17), justify="center")
    muscular_button.place(x = 70, y = 340, height=50, width=250)


    # Bulk
    bulk_button = tk.Button(root, text="BULK", fg="black", bg="skyblue",
                            command=bulk,
                                font=("JetBrains Mono", 17), justify="center")
    bulk_button.place(x = 70, y = 420, height=50, width=250)


    # back_button = tk.Button(root, text="BACK", fg="yellow", bg="red",
    #                         command=suggest_diet_button,
    #                             font=("JetBrains Mono", 17), justify="center")
    # back_button.place(x = 450, y = 285, height=55, width=300)

        

# main 

if __name__ == "__main__":

    # window creation

    root = tk.Tk()
    root.state("zoomed")
    root.title("Nutrition Detection")
    root.config(bg="dark blue")


    # First label

    Label_name = tk.Label(root, text="Fruit Name : ", fg="white", bg="dark blue", font=("Fira code", 25, "bold"))
    Label_name.place(x = 930, y = 155)


    # Input Box

    Entry1 = tk.Entry(root, textvariable=tk.StringVar, bg="sky blue", fg="black", font="JetBrains", justify="center", borderwidth=20, relief="flat")
    Entry1.place(x = 860, y = 240, height=50, width=350)


    # Submit Button

    Get_Button = tk.Button(root, text="SUBMIT", command=get_name, fg="white", bg="blue", font=("JetBrains"), justify="center")
    Get_Button.place(x = 930, y = 365, width=200)


    # image button

    upload_image = tk.PhotoImage(file='C:\\Users\\Hp\\Downloads\\drop or upload.png')

    image_button = tk.Button(root, image=upload_image, command=browse_image)
    image_button.place(x = 40, y =100)


    # OR lable

    Label_or = tk.Label(root, text="OR", fg="white", bg="dark blue", font=("Fira code", 25, "bold"))
    Label_or.place(x = 725, y = 300)


    # suggest diet plan

    suggest_diet_button = tk.Button(root, text="Suggest Me A Diet 😋", fg="black", bg="skyblue",
                                        command=suggest,
                                    font=("JetBrains Mono", 17))
    suggest_diet_button.place(x = 480, y = 550, height=70, width=350)



    root.mainloop()