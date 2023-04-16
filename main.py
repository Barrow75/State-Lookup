print("Welcome to the State Information Finder!")
print('\n')

# state user wants to look up
user = input("Enter a State: ")

# list of states
Enter_State = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
               "Florida",
               "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
               "Maryland"
    , "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
               "New Hampshire",
               "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
               "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
               "Vermont",
               "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# lists of capitals
Capital = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee",
           "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort",
           "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "St.Paul", "Jackson", "Jefferson City", "Helena",
           "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus",
           "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin",
           "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]

# list of when each state joined the union
Joined = ['22nd', '49th', '48th', '25th', '31st', '38th', '5th', '1st', '27th', '4th', '50th', '43rd', '21st', '19th',
          '29th', '34th', '15th', '18th', '23rd', '7th', '6th', '26th', '32nd', '20th', '24th', '41st', '37th', '36th',
          '9th', '3rd', '47th', '11th', '12th', '39th', '17th', '46th', '33rd', '2nd', '13th', '8th', '40th', '16th',
          '28th', '45th', '14th', '10th', '42nd', '35th', '30th', '44th']

# list of congressional districts per state
District = [7, 1, 9, 4, 53, 7, 5, 1, 14, 27, 2, 2, 18, 9, 4, 4, 6, 6, 2, 8, 9, 14, 8, 4, 8, 1, 3, 4, 2, 12, 3, 27, 13,
            1, 16, 5, 5, 18, 2, 7, 1, 9, 36, 4, 1, 11, 10, 3, 8, 1]

# indexing position per state to find it on the list
position = Enter_State.index(user)

# checks to see if the state is in the list and prints out the position and information for each selected state
if user in Enter_State:
    print("\n")
    user == position
    print("The capital of the state of", user, "is", Capital[position], ", it has", District[position],
          "congressional districts and was the", Joined[position], " state to join the union")
