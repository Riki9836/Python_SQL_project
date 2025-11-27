import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # your MySQL username
    password="",# your MySQL password
    database="medical"
)

cursor = conn.cursor()

def doc_database(Doc_Name, Dept, Speciality):
    query = "INSERT INTO Doc (Doc_Name, Dept, Speciality) VALUES (%s, %s, %s)"
    cursor.execute(query, (Doc_Name, Dept, Speciality))
    conn.commit()
    print("Database updated sucessfully")

def check():
    cursor.execute("SELECT * FROM Doc")
    for (id, Doc_Name, Dept, Speciality) in cursor.fetchall():
        print(f"Doctor ID: {id}, Doctor Name: {Doc_Name}, Department: {Dept}, Speciality: {Speciality}")

def modify(Doc_id, Doc_Name, Dept, Speciality):
    query = "UPDATE doc SET Doc_name=%s, Dept=%s, Speciality=%s WHERE id=%s"
    cursor.execute(query, (Doc_Name, Dept, Speciality, Doc_id))
    conn.commit()
    print("Data modified successfully.")

def delete(Doc_id):
    query = "DELETE FROM Doc WHERE id=%s"
    cursor.execute(query, (Doc_id,))
    conn.commit()
    print("Data deleted successfully.")

def appt_data(Patient_Name, Dept, Booking_Time):
    query = "INSERT INTO Booking (Patient_Name, Dept, Booking_Time) VALUES (%s, %s, %s)"
    cursor.execute(query, (Patient_Name, Dept, Booking_Time))
    conn.commit()
    print("Appointment booked sucessfully")

def bookings():
    cursor.execute("SELECT * FROM Booking")
    for (app_id, Patient_Name, Dept, Booking_Time) in cursor.fetchall():
        print(f"Appointment ID: {app_id}, Patient Name: {Patient_Name}, Department: {Dept}, Appointment Time: {Booking_Time}")

def update(app_id, Patient_Name, Dept, Booking_Time):
    query = "UPDATE booking SET Patient_name=%s, Dept=%s, Booking_Time=%s WHERE app_id=%s"
    cursor.execute(query, (Patient_Name, Dept, Booking_Time, app_id))
    conn.commit()
    print("Appointment modified successfully.")

def cancel(app_id):
    query = "DELETE FROM booking WHERE app_id=%s"
    cursor.execute(query, (app_id,))
    conn.commit()
    print("Appointment canceled successfully.")

def doc_search(Doc_id):
    query = "SELECT * FROM Doc WHERE id = %s"
    
    cursor.execute(query, (Doc_id,))      # Execute query first
    result = cursor.fetchone()            # Fetch only one doctor
    
    if result:
        id, Doc_Name, Dept, Speciality = result
        print("Findings:")
        print(f"Doctor ID: {id}")
        print(f"Doctor Name: {Doc_Name}")
        print(f"Department: {Dept}")
        print(f"Speciality: {Speciality}")
    else:
        print("No doctor found with this ID.")

def appt_search(app_id):
    query = "SELECT * FROM booking WHERE app_id = %s"
    
    cursor.execute(query, (app_id,))      # Execute query first
    result = cursor.fetchone()            # Fetch only one doctor
    
    if result:
        app_id, Patient_Name, Dept, Booking_Time = result
        print("Findings:")
        print(f"Appointment ID: {app_id}")
        print(f"Patient Name: {Patient_Name}")
        print(f"Department: {Dept}")
        print(f"Scheduled Time: {Booking_Time}")
    else:
        print("No Appointments found with this ID.")        


def main():
    while True:
        print("\n--- Hospital Site ---")
        print("1. Career")
        print("2. Appointmnts")
        print("X")

        select = input("Enter your preference: ")

        if select == '1':
            while True:
            
                print("\n--- Career ---")
                print("1. New addidtion")
                print("2. Check Database")
                print("3. Modify Database")
                print("4. Delete Data")
                print("5. Search Doctor")
                print("6. Main Menu")

                choice = input("Enter choice: ")

                if choice == '1':
                    Doc_Name = input("Enter Doctor name: ")
                    Dept = input("Enter Department: ")
                    Speciality = input("Enter Speciality: ")
                    doc_database(Doc_Name, Dept, Speciality)
                    
                    
                elif choice == '2':
                    check()
                elif choice == '3':
                    Doc_id = int(input("Enter Doctor ID to update: "))
                    Doc_Name = input("Enter new name(If any): ")
                    Dept = input("Enter new Department(If any): ")
                    Speciality = input("Enter new Speciality(If any): ")
                    modify(Doc_id, Doc_Name, Dept, Speciality)
                elif choice == '4':
                    Doc_id = int(input("Enter Doctor ID to delete: "))
                    delete(Doc_id)
                elif choice =='5':
                    Doc_id = int(input("Enter Doctor ID to search: "))
                    doc_search(Doc_id)
                elif choice == '6':
                    break
                else:
                    print("Invalid choice. Try again.")
        
        elif select == '2':
            while True:
                print("\n ---Appointments---")
                print("1. New Appointments")
                print("2. Check all appointments")
                print("3. Modify appointment")
                print("4. Cancel Appointment")
                print("5. Search Appointments")
                print("6. Main Menu")

                chs = input("Enter choice: ")

                if chs == '1':
                    Patient_Name = input("Enter Patient name: ")
                    Dept = input("Enter Department: ")
                    Booking_Time = input("Enter preferred time: ")
                    appt_data(Patient_Name, Dept, Booking_Time)

                elif chs == '2':
                    bookings()

                elif chs == '3':
                    app_id = int(input("Enter Appointment ID to update: "))
                    Patient_Name = input("Enter new name(If any): ")
                    Dept = input("Enter new Department(If any): ")
                    Booking_Time = input("Enter new Time(If any): ")
                    update(app_id, Patient_Name, Dept, Booking_Time)

                elif chs == '4':
                    app_id = int(input("Enter Appointment ID to delete: "))
                    cancel(app_id)

                elif chs == '5':
                    app_id = int(input("Enter Appointment ID to search: "))
                    appt_search(app_id)                    

                elif chs == '6':
                    break

                else:
                    print("Invalid choice. Try again.")

        elif select == 'X':
            break

        else:
            print("Invalid choice. Try again.")

    cursor.close()
    conn.close()
    
if __name__ == "__main__":
    main()

