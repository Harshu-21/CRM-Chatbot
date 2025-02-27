import pandas as pd

# Load or create the employee database (CSV file)
def load_database():
    try:
        data = pd.read_csv("employees.csv", dtype=str)
    except FileNotFoundError:
        data = pd.DataFrame(columns=["ID", "Name", "Department", "Designation", "Tasks", "Task Status", "Status"])
        data.to_csv("employees.csv", index=False)
    return data

# Save the database
def save_database(data):
    data.to_csv("employees.csv", index=False)

# Display all employees
def view_employees(data):
    if data.empty:
        print("\n⚠ No employees found in the database.")
    else:
        print("\n📋 Employee List:")
        print(data[["ID", "Name", "Department", "Designation", "Status"]].to_string(index=False))

# Add a new employee
def add_employee(data):
    emp_id = input("🔹 Enter Employee ID: ").strip()
    if emp_id in data["ID"].values:
        print("\n⚠ Employee ID already exists!")
        return data

    name = input("🔹 Enter Name: ").strip()
    department = input("🔹 Enter Department: ").strip()
    designation = input("🔹 Enter Designation: ").strip()

    new_entry = pd.DataFrame([{
        "ID": emp_id,
        "Name": name,
        "Department": department,
        "Designation": designation,
        "Tasks": "None",
        "Task Status": "Not Assigned",
        "Status": "Active"
    }])

    data = pd.concat([data, new_entry], ignore_index=True)
    print("\n✅ Employee added successfully!")
    return data

# Assign a task to an employee
def assign_task(data):
    emp_id = input("🔹 Enter Employee ID to assign task: ").strip()
    if emp_id not in data["ID"].values:
        print("\n⚠ Employee not found!")
        return data

    task = input("🔹 Enter the task to assign: ").strip()
    data.loc[data["ID"] == emp_id, "Tasks"] = task
    data.loc[data["ID"] == emp_id, "Task Status"] = "In Progress"
    print("\n✅ Task assigned successfully!")
    return data

# Update task status
def update_task_status(data):
    emp_id = input("🔹 Enter Employee ID to update task status: ").strip()
    if emp_id not in data["ID"].values:
        print("\n⚠ Employee not found!")
        return data

    status = input("🔹 Enter new task status (In Progress / Completed): ").strip().title()
    if status not in ["In Progress", "Completed"]:
        print("\n⚠ Invalid status! Please enter 'In Progress' or 'Completed'.")
        return data

    data.loc[data["ID"] == emp_id, "Task Status"] = status
    print("\n✅ Task status updated successfully!")
    return data

# View assigned tasks
def view_tasks(data):
    tasks = data[data["Tasks"] != "None"]
    if tasks.empty:
        print("\n⚠ No tasks assigned yet.")
    else:
        print("\n📝 Assigned Tasks:")
        print(tasks[["ID", "Name", "Tasks", "Task Status"]].to_string(index=False))

# Remove an employee
def remove_employee(data):
    emp_id = input("🔹 Enter Employee ID to remove: ").strip()
    if emp_id not in data["ID"].values:
        print("\n⚠ Employee not found!")
        return data

    data = data[data["ID"] != emp_id]
    print("\n✅ Employee removed successfully!")
    return data

# Search for an employee
def search_employee(data):
    search_term = input("🔹 Enter Employee ID or Name to search: ").strip()
    result = data[(data["ID"] == search_term) | (data["Name"].str.contains(search_term, case=False, na=False))]
    
    if result.empty:
        print("\n⚠ No matching employee found!")
    else:
        print("\n🔍 Employee Found:")
        print(result.to_string(index=False))

# Main chatbot menu
def chatbot():
    data = load_database()
    while True:
        print("\n--- 🏢 Employee CRM Chatbot Menu ---")
        print("1️⃣ View Employees")
        print("2️⃣ Add New Employee")
        print("3️⃣ Assign Task to Employee")
        print("4️⃣ Update Task Status")
        print("5️⃣ View Assigned Tasks")
        print("6️⃣ Search Employee")
        print("7️⃣ Remove Employee")
        print("8️⃣ Exit")
        choice = input("\n💡 Enter your choice: ").strip()

        if choice == "1":
            view_employees(data)
        elif choice == "2":
            data = add_employee(data)
            save_database(data)
        elif choice == "3":
            data = assign_task(data)
            save_database(data)
        elif choice == "4":
            data = update_task_status(data)
            save_database(data)
        elif choice == "5":
            view_tasks(data)
        elif choice == "6":
            search_employee(data)
        elif choice == "7":
            data = remove_employee(data)
            save_database(data)
        elif choice == "8":
            print("\n👋 Exiting Employee CRM Chatbot. Have a great day!")
            break
        else:
            print("\n⚠ Invalid choice. Please try again.")

# Run the chatbot
chatbot()
