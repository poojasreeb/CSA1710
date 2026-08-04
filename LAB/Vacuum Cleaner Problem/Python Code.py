def vacuum_cleaner(rooms):
    for i in range(len(rooms)):
        print(f"Room {i+1}: {rooms[i]}")

        if rooms[i] == "Dirty":
            print("Action: Clean")
            rooms[i] = "Clean"
        else:
            print("Action: No Cleaning Required")

        print()

    print("Final Room Status:")
    for i in range(len(rooms)):
        print(f"Room {i+1}: {rooms[i]}")

rooms = ["Dirty", "Clean", "Dirty", "Dirty"]

vacuum_cleaner(rooms)
