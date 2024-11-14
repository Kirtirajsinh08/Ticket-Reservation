import mysql.connector
import random

class RailwayTicketReservation:
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost",user="root",passwd="",database="railway_ticket")
        self.cursor = self.db.cursor()

    def user_login(self):
        while True:
            print("PRESS 1: TO REGISTER YOUR EMAIL ADDRESS")
            print("PRESS 2: TO LOGIN YOUR EMAIL ADDRESS")
            choice = int(input("Enter choice please : "))

            if choice == 1:
                user_id = int(input("ENTER AN UNIQUE USER ID OF 5 DIGITS: "))
                check = False

                # Check if user exists in database
                self.cursor.execute("SELECT user_id FROM user")
                result = self.cursor.fetchall()

                for row in result:
                    if row[0] == user_id:
                        check = True
                        break

                if check:
                    print("USER ID ALREADY EXISTS")
                else:
                    user_name = input("ENTER YOUR USER NAME: ")
                    password = input("SET YOUR PASSWORD: ")
                    phone_num = input("ENTER YOUR PHONE NUMBER: ")
                    email = input("ENTER YOUR EMAIL ADDRESS: ")

                    # Insert details of new users
                    sql = "INSERT INTO user (user_id, user_name, password, phone_num, email) VALUES (%s, %s, %s, %s, %s)"
                    val = (user_id, user_name, password, phone_num, email)
                    self.cursor.execute(sql, val)
                    self.db.commit()
                    print("YOU HAVE SUCCESSFULLY REGISTERED")
                    break

            elif choice == 2:
                user_id = int(input("ENTER YOUR USER ID FOR LOGIN: "))
                password = input("ENTER YOUR PASSWORD: ")
                login_check = False

                # Code if the user id and password matches in database
                self.cursor.execute("SELECT user_id, password FROM user")
                result = self.cursor.fetchall()

                for row in result:
                    if row[0] == user_id and row[1] == password:
                        login_check = True
                        break

                if not login_check:
                    print("YOU HAVE ENTERED EITHER WRONG USER ID OR PASSWORD, PLEASE TRY AGAIN")
                else:
                    print("YOU HAVE SUCCESSFULLY LOGGED IN")
                    break

            else:
                print("ENTER A VALID CHOICE")


    def train_details(self, src, dest):
        sql = "SELECT * FROM train WHERE source LIKE %s AND destination LIKE %s"
        self.cursor.execute(sql, ('%' + src + '%', '%' + dest + '%'))
        result = self.cursor.fetchall()

        train_check = False

        for row in result:
            train_check = True
            train_no = row[0]
            train_name = row[1]
            source = row[2]
            destination = row[3]
            departure = row[4]
            arrival = row[5]
            duration = row[6]
            ss_avail = row[7]
            cc_avail = row[8]

            print("--------------------------------------------------------------")
            print(f"{train_name} ({train_no})")
            print("RUNNING ON MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY\n")
            print(f"{source}\t\t------------->\t\t{destination}")
            print(f"{departure}\t\t\t\t{duration}\t\t\t{arrival}")
            print("TICKETS AVAILABLE:")
            print(f"SECOND SEATING (2S): {ss_avail}")
            print(f"CHAIR CAR (CC): {cc_avail}")
            print("--------------------------------------------------------------\n")

        if not train_check:
            print(f"NO TRAINS AVAILABLE FROM {src} TO {dest}")

    def book_train(self):
        src = input("ENTER SOURCE STATION: ")
        dest = input("ENTER DESTINATION STATION: ")
        self.train_details(src, dest)

        if input("Do you want to book this train? (yes/no): ").lower() == "yes":
            self.ticket_type(src, dest)

    def generate_ticket(self, seat_avail, seat_price, train_no, choice):
        ticket_details = []
        update_seats = []

        seat_book = int(input("ENTER HOW MANY PASSENGER SEATS YOU WANT TO BOOK: "))
        total_price = seat_book * seat_price

        if seat_book <= seat_avail:
            seat_left = seat_avail - seat_book

            if choice == 1:
                update_train_seat = f"UPDATE train SET cc_avail = {seat_left} WHERE train_no = {train_no}"
            else:
                update_train_seat = f"UPDATE train SET 2s_avail = {seat_left} WHERE train_no = {train_no}"

            update_seats.append(update_train_seat)

            passenger_details = []

            passenger = 1

            while seat_book > 0:
                name = input(f"ENTER PASSENGER {passenger} NAME: ")
                gender = input("ENTER PASSENGER GENDER: ")
                age = int(input("ENTER PASSENGER AGE: "))

                seat_alpha = random.choice(["A", "B", "C", "D"])
                seat_no = random.randint(1, 100)

                current_status = f"{seat_alpha}{seat_no}"

                # To give PNR number to the passangers
                pnr = random.randint(10000000, 99999999)
                ticket_details.append((name, gender, age, seat_price, current_status, train_no, pnr))

                passenger_details.append({
                    "Name": name,
                    "Gender": gender,
                    "Age": age,
                    "Seat": current_status,
                    "PNR": pnr 
                })

                seat_book -= 1
                passenger += 1

            print("PAYMENT DETAILS:")
            print(f"TOTAL TICKET PRICE: {total_price}")
            print("PAYMENT METHODS:")
            print("1. Credit Card")
            print("2. Debit Card")
            print("3. Net Banking")
            payment_method = int(input("SELECT PAYMENT METHOD (1/2/3): "))

            # Generate OTP
            otp = random.randint(1000, 9999)
            print(f"OTP for transaction: {otp}")

            # Validate OTP
            entered_otp = int(input("ENTER OTP TO COMPLETE TRANSACTION: "))
            if entered_otp != otp:
                print("INVALID OTP. TRANSACTION FAILED.")
                return

            # Generation of ticket in text file format
            transaction_id = random.randint(100000, 999999)

            with open("ticket.txt", "w") as file:
                file.write("-----Welcome To Indian Railways-----\n")
                file.write("-----------TICKET DETAILS-----------\n\n")
                for passenger_data in passenger_details:
                    file.write(f"Passenger Details:\n")
                    for key, value in passenger_data.items():
                        file.write(f"{key}: {value}\n")
                    file.write("\n")
                file.write(f"Train Details:\n")
                train_sql = f"SELECT * FROM train WHERE train_no = {train_no}"
                self.cursor.execute(train_sql)
                train_result = self.cursor.fetchone()
                file.write(f"Train Number: {train_result[0]}\n")
                file.write(f"Train Name: {train_result[1]}\n")
                file.write(f"Source: {train_result[2]}\n")
                file.write(f"Destination: {train_result[3]}\n")
                file.write(f"Departure Time: {train_result[4]}\n")
                file.write(f"Arrival Time: {train_result[5]}\n")
                file.write(f"Duration: {train_result[6]}\n")
                file.write("\n")
                file.write(f"Total Fare: {total_price}\n")
                file.write(f"Payment Mode: {'Credit Card' if payment_method == 1 else 'Debit Card' if payment_method == 2 else 'Net Banking'}\n")
                file.write(f"Transaction ID: {transaction_id}\n\n\n")
                file.write(" ")
                file.write("-Prescribed Original ID proofs are:- Voter Identity Card / Passport / PAN Card / Driving License / Photo ID card issued by\n")
                file.write("Central / State Govt. / Public Sector \n")
                file.write("Undertakings of State / Central Government ,District Administrations , Municipal bodies and Panchayat Administrations which\n")
                file.write("are having serial number /\n")
                file.write("Cards issued by Banks with laminated photograph/Unique Identification Card 'Aadhaar', m-Aadhaar, e-Aadhaar. /Passenger showing /\n")
                file.write("the Aadhaar/Driving /\n")
                file.write("Licence from the 'Issued Document'section by logging into his/her DigiLocker account considered as valid proof of identity. /\n")
                

            print("PAYMENT DONE SUCCESSFULLY.")
            print("YOUR TICKET IS BOOKED SUCCESSFULLY. HAPPY JOURNEY!")

            # Adding passengers' bookings to the database
            sql = "INSERT INTO bookings (name, gender, age, price, current_status, train_no, pnr) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.cursor.executemany(sql, ticket_details)
            self.db.commit()

            for t in update_seats:
                self.cursor.execute(t)

            self.db.commit()

        else:
            print("THE NUMBER OF PASSENGER SEATS YOU HAVE ENTERED ARE NOT AVAILABLE. PLEASE TRY OTHER SEATS")



    def ticket_type(self, src, dest):
        train_name = input("ENTER TRAIN NAME IN WHICH YOU WANT TO TRAVEL: ")

        src = f"'{src}%'"
        dest = f"'{dest}%'"
        sql = f"SELECT * FROM train WHERE source LIKE {src} AND destination LIKE {dest}"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        train_check = False

        for row in result:
            if row[1].lower() == train_name.lower():
                train_check = True
                train_no = row[0]
                ss_avail = row[7]
                cc_avail = row[8]
                ss_price = row[9]
                cc_price = row[10]

                while True:
                    print("ENTER 1: TO BOOK CHAIR CAR")
                    print("ENTER 2: TO BOOK SECOND SEATING")

                    choice = int(input())

                    if choice == 1:
                        self.generate_ticket(cc_avail, cc_price, train_no, choice)
                        break
                    elif choice == 2:
                        self.generate_ticket(ss_avail, ss_price, train_no, choice)
                        break
                    else:
                        print("ENTER VALID CHOICE")

        if not train_check:
            print(f"TRAIN {train_name} NOT FOUND")

        # 
    def search_ticket(self):
        pnr = int(input("ENTER PNR NUMBER TO SEARCH YOUR TICKET: "))

        sql = f"SELECT * FROM bookings WHERE pnr = {pnr}"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        pnr_check = False

        for row in result:
            pnr_check = True
            print("--------------------------------------------------------------")
            print("PASSENGER DETAILS")
            print(f"PNR: {row[5]}")
            print(f"NAME: {row[0]}")
            print(f"AGE: {row[2]}")
            print(f"GENDER: {row[1]}")
            print(f"CURRENT STATUS: {row[4]}")
            print("--------------------------------------------------------------")

            train_sql = f"SELECT * FROM train WHERE train_no = {row[6]}"
            self.cursor.execute(train_sql)
            train_result = self.cursor.fetchall()

            for train_row in train_result:
                print(f"{train_row[1]} ({train_row[0]})")
                print(f"{train_row[2]}\t\t------------->\t\t{train_row[3]}")
                print(f"{train_row[4]}\t\t\t\t{train_row[6]}\t\t\t{train_row[5]}")
                print("--------------------------------------------------------------")

        if not pnr_check:
            print(f"NO TICKET FOUND FOR PNR {pnr}")

    def cancel_booking(self):
        pnr = int(input("ENTER PNR NUMBER TO CANCEL YOUR BOOKING: "))

        sql_select = f"SELECT * FROM bookings WHERE pnr = {pnr}"
        self.cursor.execute(sql_select)
        result = self.cursor.fetchone()

        if result:
            train_no = result[6]

            sql_delete = f"DELETE FROM bookings WHERE pnr = {pnr}"
            self.cursor.execute(sql_delete)
            self.db.commit()

            if train_no:
                sql_update = f"UPDATE train SET cc_avail = cc_avail + 1 WHERE train_no = {train_no}"
                self.cursor.execute(sql_update)
                self.db.commit()

            print("TICKET BOOKING IS CANCELLED SUCCESSFULLY, YOUR MONEY WILL BE REFUNDED SOON")
        else:
            print(f"PNR {pnr} NOT FOUND")

def main():
    print("<*^*><*^*><*^*><*^*><*^*><*^*><*^*> WELCOME TO TICKET VIESTA <*^*><*^*><*^*><*^*><*^*><*^*><*^*>\n")

    r = RailwayTicketReservation()
    r.user_login()

    print("\n\t****************************************************\n\t******************  TICKET VIESTA  ********************\n\t****************************************************\n")

    while True:
        print("ENTER 1: TO GET TRAIN DETAILS")
        print("ENTER 2: TO BOOK TRAIN TICKETS")
        print("ENTER 3: TO SEARCH YOUR TICKETS")
        print("ENTER 4: TO CANCEL BOOKING")
        print("ENTER 5: TO EXIT FROM TICKET VIESTA")

        choice = int(input())

        if choice == 1:
            src = input("ENTER SOURCE STATION: ")
            dest = input("ENTER DESTINATION STATION: ")
            r.train_details(src, dest)
        elif choice == 2:
            r.book_train()
        elif choice == 3:
            r.search_ticket()
        elif choice == 4:
            r.cancel_booking()
        elif choice == 5:
            print("THANK YOU FOR VISITING TICKET VIESTA SITE, SEE YOU SOON")
            break
        else:
            print("ENTER VALID CHOICE")

main()