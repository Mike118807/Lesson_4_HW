

# lesson 4 task 1

# List of the days of the week
days_in_week =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]

# Print days on even indices
for index in ('days_in_week'):
    
    if index% 2 == 0:
        
        print(day)
        

# Task 1: Meal Planner Simulate a meal planner that picks a random meal from a meal list for breakfast lunch and dinner for each day of the week.
#   Use nested loops to implement this:the outer loop should iterate over the days, and the inner loop should iterate over the meals of the day.
#   For each time, randomly select a meal from a predefined list and print it. 

#Output: ..."Tuesday for Breakfast I'm having Yogurt" "Tuesday for Lunch I'm having Chicken" 
# "Tuesday for Dinner I'm having Pizza" "Wednesday for Breakfast I'm having Tacos" ...


# List of meals and each time of meals

meals = {'Breakfast': ['Yogurt', 'Oatmeal', 'Scrambled Eggs', 'Pancakes', 'Fruit Salad'], 'Lunch': ['Chicken', 'Salad', 'Sandwich', 'Soup', 'Pasta'], 'Dinner': ['Pizza', 'Tacos', 'Stir Fry', 'Fish', 'Burger']}

# Days

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Outer loop for days

for day, in days_of_week:['random']
    
    # Inner loop for meals
    
for meal_time, meal_options in meals.items():
        
        chosen_meal = (meal_options)
        
        print(f"{day} for {meal_time} I'm having {chosen_meal}")
