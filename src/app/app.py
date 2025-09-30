import customtkinter as ctk
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Informasi Alumni")
        self.geometry("800x600")

        self.menu_frame = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#14213d")
        self.menu_frame.pack(side="left", fill="y")

        self.title_menu_frame = ctk.CTkFrame(self.menu_frame, width=200,
                                             corner_radius=5, fg_color="#0c1324")
        self.title_menu_frame.pack(side="top", fill="x", padx=10, pady=10)

        self.content_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#1d2f57")
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.menu_label = ctk.CTkLabel(self.title_menu_frame, text="Sistem Informasi Alumni",
                                                                              font=("Segoe UI", 20, "bold"), text_color="#E5E5E5")
        self.menu_label.pack(side="top", fill="x", pady=10, padx=10)
        self.start_label_caption = ctk.CTkLabel(self.content_frame, text="Sistem Informasi Alumni",
                                        font=("Segoe UI", 30, "bold"))
        self.start_label_caption.pack(side="top", padx=10, expand=True)


        self.credits = ctk.CTkLabel(self.content_frame, text="\nCredits:"
                                                                         "\n1. Muhammad Dava Syahputra"
                                                                         "\n2. Ryan Ivan Pratama"
                                                                         "\n3. Muhammad Rafli Rafsanjani",
                                        font=("Segoe UI", 12), justify="left")
        self.credits.pack(side="left", pady=10, padx=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()