import uuid
import hashlib
from datetime import datetime

Table1 = []
Table2 = []
Table3 = []

TimeStamp = datetime.now().isoformat()

Username = input("Enter Username: ")

Password = input("Enter Password: ")

# Generate Unique User ID.
Unique_User_ID = str(uuid.uuid4())

# Choosing the values of which the salt consists off.
Salt_Data = TimeStamp + Username + Unique_User_ID
Salt_Password = hashlib.sha256(Salt_Data.encode("utf-8")).digest()

# Hashing the password only.
Hash_Password = hashlib.sha256(Password.encode("utf-8")).hexdigest()

# Adding the salt to the hashed password using the function (pbkdf2_hmac).
Hashed_Salted_Password = hashlib.pbkdf2_hmac(
    "sha256",
    Password.encode("utf-8"),
    Salt_Password,
    100_000
).hex()

# Adding the necessary details to the tables.
Table1.append(
    {"Username": Username, "Password": Password, "Timestamp": TimeStamp})

Table2.append({"Username": Username, "Unique User ID": Unique_User_ID,
              "Hashed Password": Hash_Password})

Table3.append({"Username": Username, "Unique User ID": Unique_User_ID,
              "Hashed Salted Password": Hashed_Salted_Password})

print("\n=======Table #1=======")

for index1 in Table1:
    print(index1)

print("\n=======Table #2=======")

for index2 in Table2:
    print(index2)

print("\n=======Table #3=======")

for index3 in Table3:
    print(index3)
