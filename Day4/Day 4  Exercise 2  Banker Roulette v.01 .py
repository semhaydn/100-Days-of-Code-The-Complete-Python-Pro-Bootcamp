import random
import tkinter as tk
from tkinter import messagebox

def pick_person_to_pay(names):
    if not names:
        return None

    # Randomly select a person from the list of names
    selected_person = random.choice(names)

    return selected_person

def get_names_from_user():
    names_in_bowl = []
    num_names = int(entry_participants.get())

    for i in range(num_names):
        name = entry_name_list[i].get()
        names_in_bowl.append(name)

    return names_in_bowl

def pick_winner():
    names_in_bowl = get_names_from_user()
    person_to_pay = pick_person_to_pay(names_in_bowl)

    if person_to_pay is not None:
        label_result.config(text=f"The person who will pay for the meal is: {person_to_pay}")
    else:
        messagebox.showwarning("Warning", "Please enter at least one name.")

def main():
    root = tk.Tk()
    root.title("London Banker's Meal Payment Game")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    label_instruction = tk.Label(frame, text="Enter the number of participants and their names:")
    label_instruction.grid(row=0, columnspan=2)

    label_participants = tk.Label(frame, text="Number of participants:")
    label_participants.grid(row=1, column=0, padx=5, pady=5)

    global entry_participants
    entry_participants = tk.Entry(frame)
    entry_participants.grid(row=1, column=1, padx=5, pady=5)
    entry_participants.focus_set()

    global entry_name_list
    entry_name_list = []
    for i in range(5):  # Limiting to 5 participants for simplicity
        label_name = tk.Label(frame, text=f"Name of person {i + 1}:")
        label_name.grid(row=i + 2, column=0, padx=5, pady=5)

        entry_name = tk.Entry(frame)
        entry_name.grid(row=i + 2, column=1, padx=5, pady=5)
        entry_name_list.append(entry_name)

    btn_pick_winner = tk.Button(frame, text="Pick Winner", command=pick_winner)
    btn_pick_winner.grid(row=7, columnspan=2, pady=10)

    global label_result
    label_result = tk.Label(frame, text="")
    label_result.grid(row=8, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
