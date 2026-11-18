# Class List Manager - Group 7
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====
# Written by: Nourah (Task 1)
def count_names(names):
    return len(names)

# Written by: Lena (Task 2)
def sort_names(names):
    return sorted(names)

# Written by: Joury (Task 3)
def to_upper(names):

    return [name.upper() for name in names]
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Sorted names:", sort_names(names))
    print("Names in uppercase:", to_upper(names))
main()
