import mysql.connector

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
        print(f"Fruit: {fruit_name}\nCalories: {calories}\nProtein: {protein}\nCarbohydrates: {cabs}\nFiber: {fiber}\nVitamins: {vitamins}\nFat: {fat}\nSugar: {sugar}")
    else:
        print(f"{fruit_name} not found in the database.")


if __name__ == "__main__":

    user_input = input("Enter Fruit Name : ")

    get_fruit_info(user_input)