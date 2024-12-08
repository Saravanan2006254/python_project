import customtkinter as ctk
from PIL import Image,ImageTk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
def main():
    def logout():
        main_window.destroy() 
        from loginregisteration import welcome_ui 
        welcome_ui() 
    main_window = ctk.CTk()
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    main_window.geometry(f"{screen_width}x{screen_height}+0+0")
    main_window.title("Main Application")
    main_window.grid_rowconfigure(1, weight=1)
    main_window.grid_columnconfigure(1, weight=1)
    class centerframe(ctk.CTkFrame):
        parent = main_window
        frames = []
        def __init__(self):
            super().__init__(centerframe.parent, fg_color="#F3F8F1")
            self.grid(row=1, column=1, sticky="nsew",pady= 5)
            # oo = ctk.CTkLabel(self,text = "", image = centerframe.image)
            # oo.pack()
            if self not in centerframe.frames:
                centerframe.frames.append(self)
        def showframe(self):
            for f in centerframe.frames:
                f.grid_forget()
            self.grid(row=1, column=1, sticky="nsew",pady= 5)  


    #leftframe (will containt stuff like history and cart and stuff)
    leftframe = ctk.CTkFrame(main_window, width=900, fg_color="#FFF4D2")
    leftframe.grid(row=0, column=0, rowspan=2, sticky="ns",padx = 5) 
    home_btn = ctk.CTkButton(leftframe,text = "HOME", command = lambda: welcomepage.showframe())
    home_btn.pack()
    flights_btn = ctk.CTkButton(leftframe, text="Flights", command=lambda: flights.showframe())
    flights_btn.pack()

    car_rentals_btn = ctk.CTkButton(leftframe, text="Car Rentals", command=lambda: car_rentals.showframe())
    car_rentals_btn.pack()

    trains_btn = ctk.CTkButton(leftframe, text="Trains", command=lambda: trains.showframe())
    trains_btn.pack()

    hotel_booking_btn = ctk.CTkButton(leftframe, text="Hotel Booking", command=lambda: hotel_booking.showframe())
    hotel_booking_btn.pack()

    #logout button and logo 
    topframe = ctk.CTkFrame(main_window, fg_color="#CCFFCC", height=150)
    logout_btn = ctk.CTkButton(topframe,width=100,text="LOGOUT",font=("Arial", 14),fg_color = "#FF5C5C",command= lambda: logout())
    logout_btn.pack(side = "right")
    logo_label = ctk.CTkLabel(topframe,text = "WanderEase", font = ("Times new roman", 20,"bold"),text_color = "#333333")
    logo_label.pack(side = "left",padx = 20,pady = 10)
    topframe.grid(row=0, column=1, sticky="ew")
    #welcome page
    welcomepage = centerframe()
    def welcome_page(frame):
        image_path = "welcome.png"
        image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(800, 400))
        welcome_label = ctk.CTkLabel(frame, text="",image = image, font=("Arial", 30))
        frame.grid_rowconfigure(0, weight=0)  
        frame.grid_rowconfigure(1, weight=0)  
        frame.grid_rowconfigure(2, weight=0)  
        frame.grid_rowconfigure(3, weight=0)  
        frame.grid_columnconfigure(0, weight=1)  
        frame.grid_columnconfigure(1, weight=1)  

        welcome_label.grid(row=0, column=0, columnspan=2, pady=15, sticky="nsew")

        
        message = ctk.CTkLabel(frame, text="What will be your next journey?", font=("Arial", 30), text_color="#333333")
        message.grid(row=1, column=0, columnspan=2, pady=5, sticky="nsew")

        
        flights_btn = ctk.CTkButton(frame, text="Flights", command=lambda: flights.showframe(),font = ("arial", 30), width=150, height=80,fg_color = "#3CB6A8")
        flights_btn.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")

        car_rentals_btn = ctk.CTkButton(frame, text="Car Rentals", command=lambda: car_rentals.showframe(),font = ("arial", 30), width=150, height=80, fg_color = "#FF7F50")
        car_rentals_btn.grid(row=2, column=1, padx=20, pady=5, sticky="nsew")

        
        trains_btn = ctk.CTkButton(frame, text="Trains", command=lambda: trains.showframe(),font = ("arial", 30), width=150, height=80, fg_color = "#5CA9E6")
        trains_btn.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

        hotel_booking_btn = ctk.CTkButton(frame, text="Hotel Booking", command=lambda: hotel_booking.showframe(),font = ("arial", 30), width=150, height=80, fg_color = "#4CAF50")
        hotel_booking_btn.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")

        return frame


    welcomepage= welcome_page(welcomepage)
    flights = centerframe()
    def flight_page(frame):
        destination = ctk.CTkEntry(frame, placeholder_text="Enter your destination", font= ("Arial", 20),width = 300)
        destination.pack()
        starting_point = ctk.CTkEntry(frame, placeholder_text= "Enter your starting point", font = ("Arial",20),width = 300)
        starting_point.pack()
        return frame
    flights = flight_page(flights)
    trains = centerframe()
    def train_page(frame):
        destination = ctk.CTkEntry(frame, placeholder_text="Enter your destination", font= ("Arial", 20),width = 300)
        destination.pack()
        starting_point = ctk.CTkEntry(frame, placeholder_text= "Enter your starting point", font = ("Arial",20),width = 300)
        starting_point.pack()
        return frame
    trains = train_page(trains)
    hotel_booking = centerframe()
    def hotel_booking_page(frame):
        pass
    car_rentals = centerframe()
    def car_rental_page(frame):
        destination = ctk.CTkEntry(frame, placeholder_text="Enter the city", font= ("Arial", 20), width = 300)
        destination.pack()
        return frame
    car_rentals = car_rental_page(car_rentals)
    welcomepage.showframe()
    main_window.mainloop()
main()