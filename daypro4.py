# contacts = {
#     "Amit": "9876543210",
#     "Priya": "9123456780",
#     "Rahul": "9988776655"
# }
# contacts["Sneha"] = "9090909090"
# contacts["Priya"] = "9000011111"
# print("Safe Lookups")
# print("----------------")
# print("Amit:", contacts.get("Amit", "Contact not found"))       
# print("Karan:", contacts.get("Karan", "Contact not found"))      
# print("\nAll Contacts")
# print("----------------")
# for name, phone in contacts.items():
#     print(f"Contact: {name} | Phone: {phone}")/

# raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

# unique_users = set(raw_logs)

# print("Is ID05 present?:", "ID05" in unique_users)

# print("\nCounts Comparison")
# print("------------------")
# print("Total log entries:", len(raw_logs))
# print("Unique users:", len(unique_users))
# print("Duplicates removed:", len(raw_logs) - len(unique_users))

# print("\nUnique User IDs:")
# print(unique_users)

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

common_interests = friend_a.intersection(friend_b)
all_interests = friend_a.union(friend_b)

print("Common Interests (Do together):")
print(common_interests)

print("\nAll Interests (Combined list):")
print(all_interests)