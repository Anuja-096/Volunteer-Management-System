while True:

    print("================================")
    print(" Volunteer Management System ")
    print("================================")

    print("1. Add Volunteer")
    print("2. View Volunteers")
    print("3. Search Volunteer")
    print("4. Generate Report")
    print("5. Delete Volunteer")
    print("6. Update Volunteer")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # 1. Add Volunteer
    if choice == "1":

        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")
        college = input("Enter College Name: ")

        file = open("volunteers.txt", "a")

        file.write(name + "," + email + "," + phone + "," + college + "\n")

        file.close()

        print("Volunteer Added Successfully!")

    # 2. View Volunteers
    elif choice == "2":

        file = open("volunteers.txt", "r")

        lines = file.readlines()

        print("\n===== Volunteer Records =====")
        print("Total Volunteers:", len(lines))
        print()

        count = 1

        for line in lines:

            details = line.strip().split(",")

            print("Volunteer", count)
            print("Name    :", details[0])
            print("Email   :", details[1])
            print("Phone   :", details[2])
            print("College :", details[3])
            print("--------------------------")

            count += 1

        file.close()

    # 3. Search Volunteer
    elif choice == "3":

        search_name = input("Enter volunteer name to search: ")

        file = open("volunteers.txt", "r")

        found = False

        for line in file:

            if search_name.lower() in line.lower():

                details = line.strip().split(",")

                print("\nVolunteer Found:")
                print("Name    :", details[0])
                print("Email   :", details[1])
                print("Phone   :", details[2])
                print("College :", details[3])

                found = True

        file.close()

        if not found:
            print("Volunteer not found.")

    # 4. Generate Report
    elif choice == "4":

        file = open("volunteers.txt", "r")

        volunteers = file.readlines()

        file.close()

        report = open("Volunteer_Report.txt", "w")

        report.write("VOLUNTEER MANAGEMENT REPORT\n")
        report.write("===========================\n\n")

        report.write("Total Volunteers: ")
        report.write(str(len(volunteers)))
        report.write("\n")

        count = 1

        for volunteer in volunteers:

            details = volunteer.strip().split(",")

            report.write("\nVolunteer " + str(count) + "\n")
            report.write("Name    : " + details[0] + "\n")
            report.write("Email   : " + details[1] + "\n")
            report.write("Phone   : " + details[2] + "\n")
            report.write("College : " + details[3] + "\n")
            report.write("--------------------------\n")

            count += 1

        report.close()

        print("Report Generated Successfully!")

    # 5. Delete Volunteer
    elif choice == "5":

        delete_name = input("Enter volunteer name to delete: ")

        file = open("volunteers.txt", "r")

        lines = file.readlines()

        file.close()

        file = open("volunteers.txt", "w")

        found = False

        for line in lines:

            if delete_name.lower() not in line.lower():
                file.write(line)
            else:
                found = True

        file.close()

        if found:
            print("Volunteer deleted successfully!")
        else:
            print("Volunteer not found.")

    # 6. Update Volunteer
    elif choice == "6":

        update_name = input("Enter volunteer name to update: ")

        file = open("volunteers.txt", "r")

        lines = file.readlines()

        file.close()

        file = open("volunteers.txt", "w")

        found = False

        for line in lines:

            details = line.strip().split(",")

            if update_name.lower() == details[0].lower():

                print("\nEnter New Details")

                new_name = input("Enter New Name: ")
                new_email = input("Enter New Email: ")
                new_phone = input("Enter New Phone Number: ")
                new_college = input("Enter New College Name: ")

                file.write(
                    new_name + "," +
                    new_email + "," +
                    new_phone + "," +
                    new_college + "\n"
                )

                found = True

            else:

                file.write(line)

        file.close()

        if found:
            print("Volunteer updated successfully!")
        else:
            print("Volunteer not found.")

    # 7. Exit
    elif choice == "7":

        print("Thank you for using Volunteer Management System!")
        break

    else:

        print("Invalid Choice")