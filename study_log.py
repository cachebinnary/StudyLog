import json

from datetime import date

def log_entry():
    print("--- Log Today's Progress ---")

    hours = float(input("Hours studied today: "))
    focus = float(input("Rate your focus (1-10): "))
    satisfaction = float(input("Rate your satisfaction (1-10): "))
    comment = input("Any comment? = ")
    today = str(date.today())

    entry = {
        "date": today,
        "hours": hours,
        "focus": focus,
        "satisfaction": satisfaction,
        "comment": comment
    }

    try:
        with open("tracker.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(entry)
    with open("tracker.json", "w") as f:
        json.dump(data, f, indent=4)

    print("\nEntry saved.")
    print(entry)

    while input("Enter '0' to go back to menu: ").strip() != "0":
        print("Invalid input. Press '0' to go back.")


def view_history():
    print("--- Your Progress History ---")

    try:
        with open("tracker.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No entries yet")
        while input("Enter '0' to go back to menu: ").strip() != "0":
            print("Invalid input. Press '0' to go back.")
        return
    
    for entry in data:
        print(f"📅 {entry['date']}")
        print(f"   Hours studied: {entry['hours']}")
        print(f"   Focus: {entry['focus']}")
        print(f"   Satisfaction: {entry['satisfaction']}")
        print(f"   Comment: {entry['comment']}")
        print()

    while input("Enter '0' to go back to menu: ").strip() != "0":
            print("Invalid input. Press '0' to go back.")

def show_summary():
    print("--- Your Summary Progress ---")

    try:
        with open("tracker.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No entries yet")
        while input("Enter '0' to go back to menu: ").strip() != "0":
            print("Invalid input. Press '0' to go back.")
        return
    
    total_entries = len(data)
    total_hours = sum(entry["hours"] for entry in data)
    avg_focus = sum(entry["focus"] for entry in data) / total_entries
    avg_satisfaction = sum(entry["satisfaction"] for entry in data) / total_entries

    print(f" Total days logged    :  {total_entries}")
    print(f" Total hours studied  :  {total_hours}")
    print(f" Average Focus        :  {avg_focus:.1f}")
    print(f" Average Satisfaction :  {avg_satisfaction:.1f}")

    while input("Enter '0' to go back to menu: ").strip() != "0":
            print("Invalid input. Press '0' to go back.")

def main():
    while True:
        print("\n--- Progress Tracker ---")
        
        print("1. Log Today's Entry")
        print("2. View History")
        print("3. Show Summary")
        print("4. Quit")

        choice = input("\nChoose an Option: ").strip()

        if choice == "1":
            log_entry()
        elif choice == "2":
            view_history()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")
        

main()
