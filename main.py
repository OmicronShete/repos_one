import mysql.connector
import tkinter as tk
from tkinter import filedialog, PhotoImage

# browse image function

def browse_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;")])

    if file_path:
        # Load the selected image
        image = PhotoImage(file=file_path)
        image_button.config(image=image)
        image_button.image = image  # Keep a reference to prevent image from being garbage collected
        print("Selected Image:", file_path)

# get the name of fruit entered by user

def get_name():
    fruit_name = Entry1.get()

    if Entry1 != '':

        Entry1.destroy()
        Label_name.destroy()
        Label_or.destroy()
        Get_Button.destroy()
        image_button.destroy()

        get_fruit_info(fruit_name)

    else:
        print("No Input's Detected !!")


# fruit detection by name 

def get_fruit_info(fruit_name):

    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",  # usually localhost if the database is on your machine
        user="root",
        password="0417",
        database="fruitsdata"
    )

    cursor = connection.cursor()

    query = f"SELECT fruit_name, calories, protein, cabs, fiber, vitamins, fat, sugar FROM nutrition WHERE fruit_name = '{fruit_name}'"
    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        fruit_name, calories, protein, cabs, fiber, vitamins, fat, sugar = result
        # print(f"Fruit: {fruit_name}\nCalories: {calories}\nProtein: {protein}\nCarbohydrates: {cabs}\nFiber: {fiber}\nVitamins: {vitamins}\nFat: {fat}\nSugar: {sugar}")
        label2 = tk.Label(root, bg="dark blue", font=("JetBrains", 20), fg="white",
        text=f"Nutrients: \n\nFruit Name: {fruit_name}\nCalories: {calories}\nProtein: {protein}\nCarbohydrates: {cabs}\nFiber: {fiber}\nVitamins: {vitamins}\nFat: {fat}\nSugar: {sugar}")
        label2.place(x = 480, y = 150)
        # item_found()

    else:
        # print(f"{fruit_name} Not Found !")
        label3 = tk.Label(root, text=f"{fruit_name} Not Found")
        label3.place(x = 50, y = 50)


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

    upload_image = tk.PhotoImage(file='C:\\Users\\Hp\\Downloads\\drop or upload.png')

    image_button = tk.Button(root, image=upload_image, command=browse_image)
    image_button.place(x = 40, y = 150)

    # OR lable

    Label_or = tk.Label(root, text="OR", fg="white", bg="dark blue", font=("Fira code", 25, "bold"))
    Label_or.place(x = 725, y = 300)
    
    root.mainloop()