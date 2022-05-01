import csv


def write_info_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Name", "Age", "Contact Number", ""])

        writer.writerow(info_list)
        condition = True
        if __name__ == '__main--':
            condition = True
            student_num = 1



        while condition:
          student_info = input("Enter the student details:")
          print("Entered details:" + student_info)

          student_info_list = student_info.split()
          print("Entered split up information is:" + str(student_info_list))

          choice_check = input("Is the entered information correct? (yes/ no):")

          if choice_check =="yes":
              write_info_csv(student_info_list)


             condition_check = input("Do you want to continue\nYes (or) No")

              if condition_check == 'yes':
                condition = True
              else:
                condition = False
          else choice_check == "no":
              print("\nplease reenter the values")

