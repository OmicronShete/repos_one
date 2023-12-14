import mysql.connector

def get_fruit_info(fruit_name):
    # Connect to the database
    connection = mysql.connector.connect(
        host="your_host",  # usually localhost if the database is on your machine
        user="your_username",
        password="your_password",
        database="fruitsdb"
    )