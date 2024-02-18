# Ask user to input the number of books purchased for the month
books_purchased = int(input("Enter the number of books purchased this month: "))

# Calculate the number of points awarded
if books_purchased <= 1:
    book_club_points = 0
elif books_purchased <= 3:
    book_club_points = 5
elif books_purchased <= 5:
    book_club_points = 15
elif books_purchased <= 7:
    book_club_points = 30
elif books_purchased >= 8:
    book_club_points = 60

# Print the number of points awarded
print(f"Book club points awarded: {book_club_points}")