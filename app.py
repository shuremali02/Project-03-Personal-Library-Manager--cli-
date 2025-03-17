from library_manager import *
def main():
    load_library()
    while True:
        display_menu()
        choice=int(input("Enter your choice: ").strip())

        if choice == 1:
            add_book()
        elif choice == 2:
            remove_book()
        elif choice == 3:
            search_book()        
        elif choice ==4 :
            display_book()  
        elif choice == 5:
            display_statistics()     
        elif choice == 6:
            save_library()
            print("Good Bye.... ") 
            break   

        else:
            print("Invalid choice, please try again.")    




main()  