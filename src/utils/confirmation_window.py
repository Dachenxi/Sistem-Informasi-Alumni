import customtkinter as ctk

class ConfirmationWindow(ctk.CTkToplevel):
    def __init__(self, message: str):
        super().__init__(fg_color="#242745")

        self.result = False

        # Configure the window
        self.title("Confirmation Window")
        self.geometry("550x300")
        self.resizable(False, False)

        # Make the windows modal and always on top
        self.grab_set()
        self.lift()

        # Main frame config
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure((0,1), weight=1)

        # Confirmation Info
        self.info = ctk.CTkLabel(self, text="Konfirmasi Ulang Data", font=ctk.CTkFont(size=20, weight="bold"))
        self.info.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Message Label
        self.message_frame = ctk.CTkFrame(self, fg_color="#4d5291")
        self.message_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.message = ctk.CTkLabel(self.message_frame, text=message, justify="left",
                                    font=ctk.CTkFont(family="Consolas",size=16), wraplength=400)
        self.message.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Button
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.cancel,
                                           fg_color="#913030", hover_color="#782828")
        self.cancel_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.confirm_button = ctk.CTkButton(self, text="Confirm", command=self.confirm,
                                            fg_color="#309145", hover_color="#287839",)
        self.confirm_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.confirm_button.focus()
        self.bind("<Return>", lambda event: self.confirm())

    def cancel(self):
        self.result = False
        self.destroy()

    def confirm(self):
        self.result = True
        self.destroy()