"""
A group of friends is planning movie night and needs to organize votes. Write a program that:
1. Ask for the name of the person hosting (a string)
2. Use a while loop to let the user add movie votes one at a time. After each vote, ask
"Add another vote? (yes/no)". Stop when the user types "no".
3. For each vote, collect:
• Voter name (a string)
• Movie title (a string)
• Genre: "action", "comedy", "horror", or "drama" (a string)
4. Clean each vote's data before storing:
• Voter name should be converted to title case (e.g., "jane doe" → "Jane Doe")
• Movie title should be converted to title case
• Genre should be converted to lowercase and stripped of whitespace
5. Store each vote as a dictionary in a list with keys: "voter", "movie", "genre"
6. After voting closes, produce a report:
• Total number of votes
• Number of comedy votes and number of non-comedy votes (use an accumulator or
counter)
• A numbered list of all votes showing voter, movie, and genre (use a for loop with the
index)
• If more than half the votes are for comedy, print: "Looks like a comedy night!"

"""

host = input("Who's hosting? ")
movies = []
add_vote = "yes"
while add_vote == "yes":
    voter = input("What is your name? ").title()
    title = input("What movie do you want to vote for? ").title()
    genre = input("What genre is it? ").lower().strip()
    movies.append({"voter": voter, "title": title, "genre": genre})
    add_vote = input("Would you like to add another vote? yes/no ").lower()

#accumulate votes
total_votes = 0
for movie in movies:
    total_votes += 1

comedy_votes = 0
for movie in movies:
    if movie["genre"] == "comedy":
        comedy_votes += 1

print(f"Total votes: {total_votes}")
print(f"Comedy votes: {comedy_votes}")
non_comedy_votes = total_votes - comedy_votes
print(f"Non-comedy votes: {non_comedy_votes}")

for movie in enumerate(movies, start = 1):
    print(movie)

if total_votes/2 < comedy_votes:
    print("Looks like a comedy night!")