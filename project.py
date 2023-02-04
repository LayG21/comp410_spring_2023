"""
Create a function which inputs a comma separated list of states and returns a dict of states and 
    total number of times each state was seen.

- The keys should be the state abbreviations, the values should be the total count.
- Sort the dictionary alphabetically by state.
- Be sure to handle variable spacing around the comma.
- In the case of an invalid or misspelled state, raise a ValueError exception.

For example:

Input text
text = 'Alaska,North Carolina,  New York , New Jersey, North Carolina, Washington'

Expected results
{'AK': 1, 'NC':2, 'NJ':1, 'NY':1, 'WA':1}

Step 1: Prepping the input (Kamaria P.)
Input is a string
Input needs to be broken up/separated to commas (also worry about spacing; some sort of trimming)
Need a dict of all written out states
A dictionary for each state name and mapping its abbreviation to it State_to_abb_dict
A dictionary for state frequencies (how many times it appears in input) state_freq_dict

Step 2: Iterate through input and check for valid state names (Jalen L.)
For loop to iterate through each state in "text" variable for state in states
    - check if state is in state_to_abb_dict
        -if it is: (meaning its a valid state name)
            check if state abbreviation has been added to frequency dictionary
                - if state_to_abb_dict[state] in state_freq_dict:
                    state_freq_dict[state_to_abb_dict[state]] += 1
                - else
                    state_freq_dict[state_to_abb_dict[state]] = 1
        -if not:
            - raise ValueError exception
return sorted(state_freq_dict)

Import 

Julious H.
Test cases:
- Misspelled state(s) -> Value Error
- Empty list -> ValueError?

Jalen S. (DONE)
- All correct states will produced a abbreviation frequency list (DONE)
    - Input text (DONE)
        text = 'Alaska,North Carolina,  New York , New Jersey, North Carolina, Washington' (DONE)
        Expected results {'AK': 1, 'NC':2, 'NJ':1, 'NY':1, 'WA':1} (DONE)

"""

#Dictionary of States to Abbrev.
state_to_abb_dict = {
  "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",

}

#Get user input (Must have commas separating state names)
states = input("Enter state names: ")

#Iterate through input and replace names with abbreviations
for key in state_to_abb_dict.keys():
    states = states.replace(key, state_to_abb_dict[key])
#Split input by commas and stripped whitespace
states = [x.strip() for x in states.split(",")]
#Sorted the abbreviated states
sorted_states = sorted(states)

state_freq_dict = {}
#iterated over list
for item in sorted_states:
    #checking if item is in dictionary
    if item in state_freq_dict:
        #incrementing if repeated
        state_freq_dict[item] += 1
    else:
        #set to 1 if not repeated
        state_freq_dict[item] = 1

#Print sorted abbreviated list
print(state_freq_dict)

"""Had to comment this out because it was causing an indentation error"""
#if input was empty <--- not too sure if this will work but test is needed
#def get_state_abbrev_freq(text_states: str) -> dict: