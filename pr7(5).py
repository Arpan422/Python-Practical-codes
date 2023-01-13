capitals = { "Maharashtra": "mumbai", "Delhi" : "new delhi","Uttar pradesh":"lucknow","Tamil Nadu ": "chennai"}
for key, value in capitals.items():
 # ask user to enter capital of state
 capital = input("Enter capital of " + key + ": ")
 # check if it is correct or not
 if capital==value:
    print("Correct")
 else:
    print("Incorrect")