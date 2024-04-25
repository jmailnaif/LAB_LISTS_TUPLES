
def sum_of_list(lst):
    return sum(lst)

# Test the function
my_list = [2, 3, 4, 5, 15, 1, 43, 20]
result = sum_of_list(my_list)
print("Sum of all items in the list:", result)
  

def find_largest(lst):
    return max(lst)

# Test the function
my_list = [2, 3, 4, 5, 15, 1, 43, 20]
largest_num = find_largest(my_list)
print("Largest number in the list:", largest_num)



odd_numbers = [num for num in range(1200, 2001, 125) if num % 2 != 0]
print("Odd numbers list:", odd_numbers)


sliced_list = odd_numbers[:5]
print("Sliced list:", sliced_list)



def calculate_average_rating(ratings):
    return sum(ratings) / len(ratings)

def filter_movies(movies_list):
    filtered_movies = []
    for movie in movies_list:
        title, year, ratings = movie
        average_rating = calculate_average_rating(ratings)
        if average_rating >= 6.0:
            filtered_movies.append((title, year, average_rating))
    return filtered_movies

def display_movies(movies_list):
    for idx, movie in enumerate(movies_list, start=1):
        title, year, average_rating = movie
        print(f"{idx}. {title} ({year}) - Average rating: {average_rating:.2f} ★")

# Example input
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# Calculate average ratings and filter movies
filtered_movies = filter_movies(movies)

# Display filtered movies
display_movies(filtered_movies)



