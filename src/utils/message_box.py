import customtkinter as ctk

class MessageBox(ctk.CTkToplevel):
    def __init__(self, title: str, message: str):
        super().__init__()

        # Main Window Config
        self.title(title)
        self.geometry("300x200")

        self.resizable(False, False)

        # Make the window modal and cannot interact with the main window
        self.grab_set()
        self.lift()

        # Main Window Grid Config
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Main Frame for better padding and background color
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#242745")
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Configure the grid inside the main frame
        self.main_frame.grid_rowconfigure(0, weight=1)  # Message row will expand
        self.main_frame.grid_rowconfigure(1, weight=0)  # Button row will not expand
        self.main_frame.grid_columnconfigure(0, weight=1)  # The single column will expand

        # Label in Main Frame
        message_label = ctk.CTkLabel(self.main_frame,
                                     text=message,
                                     font=ctk.CTkFont(size=14),
                                     wraplength=300,  # Adjusted for new width
                                     justify="left")
        message_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # OK Button in Main Frame
        ok_button = ctk.CTkButton(self.main_frame, text="OK", command=self.destroy, width=100)
        ok_button.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="e")
