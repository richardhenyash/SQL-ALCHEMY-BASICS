from models import (
    Base, session,
    Book, engine)

# main menu - add, search, analysis, exit, view
# add books to the database
# edit books
# delete books
# search books
# data cleaning
# loop runs program

def menu():
    while True:
        print(
            '''
            \nPROGRAMMING BOOKS
            \r1) Add book
            \r2) View all books
            \r3) Search for book
            \r4) Book analysis
            \r5) Exit
            ''')
        choice = input('What would you like to do? ')
        if choice in ('1', '2', '3', '4', '5'):
            return choice
        else:
            input (
                '''
                \rPlease choose one of the options above.
                \rA number from 1 to 5.
                \rPress enter to try again.
                '''
                )

def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add book
            pass
        elif choice =='2':
            # view books
            pass
        elif choice =='3':
            # search for book
            pass
        elif choice =='4':
            # book analysis
            pass
        else:
            print('GOODBYE')
            app_running = False



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()