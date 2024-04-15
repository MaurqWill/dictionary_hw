# Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
# Add a new category called "Beverages" with at least two items.
# Update the price of "Steak" to 17.99.
# Remove "Bruschetta" from "Starters".

restaurant_menu["Beverages"] = {"Lemonade": 1.99, "Wine": 4.50}
restaurant_menu["Main Course"]["Steak"] = 14.99
restaurant_menu["Starters"].pop("Bruschetta")
print(restaurant_menu)

print("====================================================================================")

# Develop a program that:

# Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
# Implement functions to:
# Book a room (mark as booked and assign to a customer).
# Check-out a customer (mark room as available and remove customer name).
# Display the status of all rooms.


hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}


def book_room(room_number, customer_name):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "available":
            hotel_rooms[room_number]["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print(f"Room {room_number} has been booked for {customer_name}.")
        else:
            print(f"Room {room_number} is already booked.")
    else:
        print(f"Room {room_number} does not exist.")
# book_room("102", "Jovon")

def checkout(room_number):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "booked":
            customer_name = hotel_rooms[room_number]["customer"]
            hotel_rooms[room_number]["status"] = "available"
            hotel_rooms[room_number]["customer"] = ""

def display_rooms():
    print("Room Status:")
    for room_number, details in hotel_rooms.items():
        print(f"Room {room_number}: {details['status']} - {details['customer']}")

display_rooms()
display_rooms()
book_room("103", "Alecia")
book_room("102", "Jovon")
book_room("101", "Jovon")
display_rooms()
checkout("101")
display_rooms()

print("==============================================================================")

# Create a system that:

# Holds a dictionary of products where each product has attributes like name, category, and price.
# Implement a search function that allows searching for products by name, 
# # returning a list of matching products (case-insensitive search).
# Handle cases where no matches are found.
# Example product dictionary:

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}

def product_search(products, product_name):
    for product, product_info in products.items():
        if product_info["name"].lower() == product_name.lower():
            return product_info
        else:
            print("No matches found")
# product_search(products, laptop)
print(product_search(products, "Laptop"))
print(product_search(products, "knife"))

print("=============================================================================")


# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_new_service_ticket(ticket_id, customer_name, issue):
    if ticket_id in service_tickets:
        print("Ticket ID already in service tickets")
    else:
        service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue, "Status": 'open'}
        print(f"Ticket {ticket_id} opened successfully.")

open_new_service_ticket('Ticket003', 'Robert', 'login_problem')
print(open_new_service_ticket('Ticket003', 'Robert', 'login_problem'))

def update_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Status of {ticket_id} updated to {status}.")

update_status('Ticket003', 'in review')

def display_tickets(status=None):
        # print(f"All service tickets: {ticket_id}{service_tickets}")

        # for ticket_id, ticket_info in service_tickets.items():
        #         print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")

# display_tickets(service_tickets,'ticket001')
    if status:
            status_tickets = {key: value for key, value in service_tickets.items() if value["Status"] == status}
            if status_tickets:
                print(f"Tickets with status: {status}")
                for ticket_id, ticket_info in status_tickets.items():
                    print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")
            else:
                print("No tickets found with that status")
    else:
        print("All service tickets:")
        for ticket_id, ticket_info in service_tickets.items():
                print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")


open_new_service_ticket('Ticket003', 'Robert', 'login_problem')
open_new_service_ticket('Ticket004', 'Dame', 'login_problem')
update_status('Ticket001', 'closed')
display_tickets("open")
display_tickets("closed")
display_tickets("in review")
update_status('Ticket001', 'closed')
display_tickets("closed")
display_tickets()


print("===================================================================================")

# You have a dictionary representing weekly sales data for a store. 
# Your task is to create a deep copy of this data and update the sales figures for a specific week.

# Given Sales Data:

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}
# Create a deep copy of weekly_sales.
# Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data.

copy_of_weekly_sales = weekly_sales.copy()
print(copy_of_weekly_sales)
copy_of_weekly_sales["Week 2"]['Groceries'] = '18000'
print(copy_of_weekly_sales)







