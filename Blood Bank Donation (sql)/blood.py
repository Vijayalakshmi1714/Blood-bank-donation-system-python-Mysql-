import mysql.connector
from datetime import date

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Viji@1724",
        database="blood_bank"
    )

def add_donor(name, age, blood_type, contact_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO donors (name, age, blood_type, contact_number) VALUES (%s, %s, %s, %s)",
                   (name, age, blood_type, contact_number))
    conn.commit()
    cursor.close()
    conn.close()
    print("Donor added successfully.")

def add_donation(donor_id):
    conn = connect_db()
    cursor = conn.cursor()
    donation_date = date.today()
    cursor.execute("INSERT INTO donations (donor_id, donation_date) VALUES (%s, %s)",
                   (donor_id, donation_date))
    conn.commit()
    cursor.close()
    conn.close()
    print("Donation recorded successfully.")

def add_blood_request(blood_type):
    conn = connect_db()
    cursor = conn.cursor()
    request_date = date.today()
    cursor.execute("INSERT INTO blood_requests (blood_type, request_date) VALUES (%s, %s)",
                   (blood_type, request_date))
    conn.commit()
    cursor.close()
    conn.close()
    print("Blood request added successfully.")

def view_donors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()
    cursor.close()
    conn.close()
    
    print("Donors List:")
    for donor in donors:
        print(f"ID: {donor[0]}, Name: {donor[1]}, Age: {donor[2]}, Blood Type: {donor[3]}, Contact: {donor[4]}")

def view_blood_requests():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blood_requests")
    requests = cursor.fetchall()
    cursor.close()
    conn.close()
    
    print("Blood Requests:")
    for request in requests:
        print(f"Request ID: {request[0]}, Blood Type: {request[1]}, Request Date: {request[2]}, Status: {request[3]}")

def fulfill_request(request_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE blood_requests SET status = 'Fulfilled' WHERE request_id = %s", (request_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Blood request fulfilled successfully.")

def main():
    while True:
        print("\nBlood Bank Donation System Menu:")
        print("1. Add Donor")
        print("2. Add Donation")
        print("3. Add Blood Request")
        print("4. View Donors")
        print("5. View Blood Requests")
        print("6. Fulfill Blood Request")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter donor name: ")
            age = int(input("Enter donor age: "))
            blood_type = input("Enter blood type: ")
            contact_number = input("Enter contact number: ")
            add_donor(name, age, blood_type, contact_number)
        elif choice == '2':
            donor_id = int(input("Enter donor ID: "))
            add_donation(donor_id)
        elif choice == '3':
            blood_type = input("Enter blood type needed: ")
            add_blood_request(blood_type)
        elif choice == '4':
            view_donors()
        elif choice == '5':
            view_blood_requests()
        elif choice == '6':
            request_id = int(input("Enter request ID to fulfill: "))
            fulfill_request(request_id)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
