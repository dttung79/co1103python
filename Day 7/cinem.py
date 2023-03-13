def choose_movie():
    print('Choose a movie: ')
    print('1. The Avengers')
    print('2. The Dark Knight')
    print('3. The Dark Knight Rises')

    choice = int(input('Enter the option: '))
    if choice == 1:
        return 'The Avengers'
    elif choice == 2:
        return 'The Dark Knight'
    elif choice == 3:
        return 'The Dark Knight Rises'
    else:
        return None

def choose_tickets():
    print('Choose seat type:')
    print('1. Normal seat ($2)')
    print('2. VIP seat ($3)')
    print('3. Coupe seat ($8)')
    seat_type = int(input('Enter the option: '))
    n_tickets = int(input('Enter the number of tickets: '))

    return seat_type, n_tickets

def print_receipt(movie, seat_type, n_tickets):
    print('Movie:', movie)
    seat = 'Normal' if seat_type == 1 else 'VIP' if seat_type == 2 else 'Coupe'
    print('Seat:', seat)
    print('Number of tickets:', n_tickets)

    price = 2 if seat_type == 1 else 3 if seat_type == 2 else 8
    total = price * n_tickets
    print('Total payment: $', total)

### Main program starts here
while True:
    movie = choose_movie()
    if movie is None:
        print('Invalid option')
        continue
    seat_type, n_tickets = choose_tickets()
    print_receipt(movie, seat_type, n_tickets)
