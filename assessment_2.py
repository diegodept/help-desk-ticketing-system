
class Ticket:
    
    ticket_counter = 2000

    def __init__(self, staff_id, name, email, problem, status="open"):
        self.staff_id = Ticket.ticket_counter  # Assign the ticket number
        Ticket.ticket_counter += 1  # Increment the ticket counter
        self.name = name
        self.email = email
        self.problem = problem
        self.status = status

ticket_list = []

def main_menu():    
    print("Select from the following options: ")
    print("0: Exit")
    print("1: Submit helpdesk ticket")
    print("2: Show all tickets")
    print("3: Respond to ticket by number")
    print("4: Re-open resolved ticket")
    print("5: Display ticket status")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        submit_ticket()
    elif choice == '2':
        show_all_tickets()
    elif choice == '3':
        respond_to_ticket()
    elif choice == '4':
        reopen_ticket()
    elif choice == '5':
        display_ticket_status()
    elif choice == '0':
        print("Exiting the program.")
        exit()
    else:
        print("Invalid choice. Please enter a number between 0 and 5")
        main_menu()  

def submit_ticket():
    staff_id = input("Enter your staff ID: ")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    print("If you require a new password, type: password change")
    problem = input("Enter description of the problem: ")
    
    status = "open"

    id_part = staff_id[:2]  # Get the first 2 characters of staff_id
    name_part = name[:3]    # Get the first 3 characters of name

    new_password = ''.join([id_part, name_part])
    
    if problem.lower() == "password change":
        print(f"Your new password is: {new_password}")
        status = "closed"
    else:
        print("Ticket submitted with the problem description.")
    
    ticket_obj = Ticket(staff_id, name, email, problem, status)
    ticket_list.append(ticket_obj)

    another_problem = input("Do you have another problem to submit? (Y/N) ")

    if another_problem.lower() == "y":
        submit_ticket()
    elif another_problem.lower() == "n":
        main_menu()
    else:
        print("Invalid input. Returning to main menu.")
        main_menu()

def show_all_tickets():
    if not ticket_list:
        print("No tickets available.")
    else:
        for ticket in ticket_list:
            print(f"Ticket Number: {ticket.staff_id}, Name: {ticket.name}, Email: {ticket.email}, Problem: {ticket.problem}, Status: {ticket.status}")

    input("Press Enter to return to the main menu...")
    main_menu()

def respond_to_ticket():
    ticket_id = int(input("Enter the ticket number you want to respond to: "))
    found = False
    
    for ticket in ticket_list:
        if ticket.staff_id == ticket_id:
            found = True
            response = input("Enter your response: ")
            print(f"Response to ticket {ticket_id}: {response}")
            ticket.status = "responded" 
            print("Response recorded.")
            break
    
    if not found:
        print("Ticket not found.")

    input("Press Enter to return to the main menu...")
    main_menu()

def reopen_ticket():
    ticket_id = int(input("Enter the ticket number you want to reopen: "))
    found = False
    
    for ticket in ticket_list:
        if ticket.staff_id == ticket_id and ticket.status == "closed":
            found = True
            ticket.status = "open"
            print(f"Ticket {ticket_id} has been reopened.")
            break
    
    if not found:
        print("Ticket not found or is already open.")

    input("Press Enter to return to the main menu...")
    main_menu()

def display_ticket_status():
    total_tickets = len(ticket_list)
    open_tickets = sum(1 for ticket in ticket_list if ticket.status == "open")
    resolved_tickets = sum(1 for ticket in ticket_list if ticket.status == "closed")
    
    print(f"Total submitted tickets: {total_tickets}")
    print(f"Open tickets: {open_tickets}")
    print(f"Resolved tickets: {resolved_tickets}")

    input("Press Enter to return to the main menu...")
    main_menu()

# Start the program
print('IT5016D Helpdesk Ticket System:')
print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
main_menu()
