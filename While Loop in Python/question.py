"""
#1) Add the activity details.
   #a) Mention the activity name as "ATM Cash Dispenser".
   #b) Introduce the program as a cash dispensing and daily report system.

#2) Display the welcome message.
   a) Print the ATM title.
   b) Add a blank line for neat output.

3) Create tracking variables.
   a) Create separate counters for each note value.
   b) Create `customers_served` to count total customers.
   c) Create `total_dispensed` to track total cash withdrawn.

4) Use the outer while loop.
   a) Use `serving = True` to keep the ATM running.
   b) Ask for the customer name.
   c) Ask for the withdrawal amount.
   d) Use `continue` if the amount is invalid.

5) Break the amount into notes.
   a) Store the withdrawal amount in `remaining`.
   b) Use an inner while loop to check six note types.
   c) Use `if-elif-else` to choose the note value.
   d) Use floor division `//` to calculate how many notes are needed.
   e) Subtract the dispensed value from the remaining amount.

6) Update note counters.
   a) Add the note count to the correct total note variable.
   b) Track notes such as 100, 50, 20, 10, 5, and 1.
   c) Print the note breakdown for the customer.

7) Update customer records.
   a) Increase `customers_served` by 1.
   b) Add the withdrawal amount to `total_dispensed`.
   c) Print a transaction complete message.

8) Ask for the next customer.
   a) Ask whether another customer should be served.
   b) Stop the while loop if the answer is not "yes".

9) Create the daily denomination report.
   a) Use a for loop to go through each note slot.
   b) Use `if-elif-else` to match each slot with a note value and total.
   c) Print only the note types that were used.

10) Show note symbols.
   a) Use an inner for loop to print one `=` symbol for each note.
   b) Keep the symbols on the same line using `end=""`.

11) Print the final summary.
   a) Print the total number of customers served.
   b) Print the total amount dispensed.
   c) Print the ATM session closing message.
"""