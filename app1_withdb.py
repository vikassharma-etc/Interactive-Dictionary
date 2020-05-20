#"python script for app1"
import mysql.connector
from difflib import SequenceMatcher
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter word: ")

query = cursor.execute("select * from Dictionary where Expression = '{0}'".format(word))
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No words found")
