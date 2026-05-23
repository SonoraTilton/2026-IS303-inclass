"""
A college student wants to track their weekly study sessions. Write a program that:

Ask the user how many study sessions to log (a number)
For each session, ask for:

Subject name (a string) — e.g., Math, History, Biology
Duration in minutes (a number)
Whether they used flashcards: yes or no (a string)


Store each session as a dictionary in a list. Each dictionary should have keys: "subject", "minutes", and "flashcards" (True or False)
After all sessions are entered, calculate and display:

Total minutes (sum of all session durations). Use the accumulator pattern.
Longest session (the subject name and duration of the longest single session). Use the min/max pattern. If no sessions were entered, print "No sessions logged."
Flashcard sessions (a list of subject names where flashcards were used). Use the filter pattern. If none used flashcards, print "No flashcard sessions this week."


Print a formatted summary:
"""

num_sessions = int(input("How many study sessions do you want to log? "))
if num_sessions > 0:
    sessions = []
    for session in range(num_sessions):
        subject = input("What subject? ").title()
        minutes = int(input("How long was your study session in minutes? "))
        flashcards = input("Did you use flashcards? yes/no ").lower().strip()
        sessions.append({"subject": subject, "minutes": minutes, "flashcards": flashcards == "yes"})

    #accumulate minutes
    total_minutes = 0
    for session in sessions:
        total_minutes += session["minutes"]

    #max session
    longest_session = sessions[0]
    for session in sessions:
        if session["minutes"] > longest_session["minutes"]:
            longest_session = session

    #filter
    flashcards_list = []
    for session in sessions:
        if session["flashcards"]:
            flashcards_list.append(session["subject"])

    print("--- Weekly Study Summary ---")
    print(f"Total minutes: {total_minutes} minutes")
    print(f"Longest session: {longest_session["subject"]} ({longest_session["minutes"]} minutes)")
    print(f"Subject with Flashcards: {", ".join(flashcards_list)}")
else:
    print("No study sessions entered.")