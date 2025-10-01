import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Informasi Alumni")
        self.geometry(f"{1100}x{580}")
        self.current_page = None

        # Main window grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Content windows grid
        self.content_frame = ContentFrame(self)
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        # Menu window grid
        self.menu_frame = MenuFrame(self, controller=self)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial page
        self.show_page(DashboardPage)

    def show_page(self, page_class):
        # Clear the current page if it exists
        if self.current_page:
            self.current_page.destroy()

        # Create an instance of the new page and place it
        self.current_page = page_class(self.content_frame)
        self.current_page.grid(row=0, column=0, sticky="nsew")

class ContentFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="#242745")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

class MenuFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, width=250, corner_radius=0, fg_color="#32355e")
        self.grid_rowconfigure(7, weight=1)
        self.controller = controller

        self.frame_title = ctk.CTkFrame(self, corner_radius=10,fg_color="#4d5291")
        self.frame_title.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.frame_title.grid_rowconfigure(0, weight=1)
        self.frame_title.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self.frame_title, text="MENU",
                                   font=ctk.CTkFont(size=20, weight="bold"),)
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        menu_0_btn = ctk.CTkButton(self, text="Dashboard",
                                   font=ctk.CTkFont(weight="bold"), height=35,
                                   command=lambda: self.controller.show_page(DashboardPage))
        menu_0_btn.grid(row=1, column=0, padx=20, pady=10)

        menu_1_btn = ctk.CTkButton(self, text="Tambah Data Alumni",
                                   font=ctk.CTkFont(weight="bold"), height=35,
                                   command=lambda: self.controller.show_page(AddNewAlumniPage))
        menu_1_btn.grid(row=2, column=0, padx=20, pady=10)

        menu_2_btn = ctk.CTkButton(self, text="Lihat Data Alumni",
                                   font=ctk.CTkFont(weight="bold"), height=35)
        menu_2_btn.grid(row=3, column=0, padx=20, pady=10)

        menu_3_btn = ctk.CTkButton(self, text="Cari Data Alumni",
                                   font=ctk.CTkFont(weight="bold"), height=35)
        menu_3_btn.grid(row=4, column=0, padx=20, pady=10)

        menu_4_btn = ctk.CTkButton(self, text="Update Data Alumni",
                                   font=ctk.CTkFont(weight="bold"), height=35)
        menu_4_btn.grid(row=5, column=0, padx=20, pady=10)

        menu_5_btn = ctk.CTkButton(self, text="Hapus Data Alumni",
                                   font=ctk.CTkFont(weight="bold"), height=35)
        menu_5_btn.grid(row=6, column=0, padx=20, pady=10)

        credit_btn = ctk.CTkButton(self,text="Credits",
                                   font=ctk.CTkFont(weight="bold"), height=35,
                                   command=lambda: self.controller.show_page(CreditsPage))
        credit_btn.grid(row=8, column=0, padx=20, pady=10, sticky="s")

class DashboardPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="#242745")

        # --- Main Grid Configuration ---
        # Configure the grid to have 3 equal-width columns for the cards
        self.grid_columnconfigure((0, 1, 2), weight=1)
        # Configure rows to add vertical spacing and center the content
        self.grid_rowconfigure(0, weight=0)  # Row for the title
        self.grid_rowconfigure(1, weight=0)  # Row for the cards
        self.grid_rowconfigure(2, weight=1)  # Empty spacer row at the bottom

        # --- Main Title ---
        self.dashboard_title = ctk.CTkLabel(self, text="Selamat Datang di Sistem Informasi Alumni",
                                            font=ctk.CTkFont(size=28, weight="bold"))
        # The title spans across all 3 columns
        self.dashboard_title.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        # --- Create and Place the Info Cards ---
        # Card 1: Total Alumni
        total_alumni_card = self.create_info_card(title="Total Alumni", value="1,500")
        total_alumni_card.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Card 2: Total Fakultas
        total_faculty_card = self.create_info_card(title="Total Fakultas", value="10")
        total_faculty_card.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        # Card 3: Total Prodi
        total_prodi_card = self.create_info_card(title="Total Prodi", value="25")
        total_prodi_card.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

    def create_info_card(self, title: str, value: str):
        """Helper function to create a styled information card."""

        card_frame = ctk.CTkFrame(self, fg_color="#4d5291", corner_radius=10)

        # Configure the grid inside the card to center the labels
        card_frame.grid_rowconfigure((0, 1), weight=1)
        card_frame.grid_columnconfigure(0, weight=1)

        # Create the title label inside the card
        card_title_label = ctk.CTkLabel(card_frame, text=title,
                                        font=ctk.CTkFont(size=18, weight="bold"))
        card_title_label.grid(row=0, column=0, padx=20, pady=(15, 5))

        # Create the value label inside the card
        card_value_label = ctk.CTkLabel(card_frame, text=value,
                                        font=ctk.CTkFont(size=40, weight="bold"))
        card_value_label.grid(row=1, column=0, padx=20, pady=(5, 15))

        return card_frame

class AddNewAlumniPage(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="#242745")
        # Add your widgets and layout for the "Add New Alumni" page here

        # Main Frame Config
        self.grid_columnconfigure(0, weight=1) # Center content
        self.grid_rowconfigure((0, 1), weight=0) # Form and Title
        self.grid_rowconfigure(2, weight=1) # Spacer

        # Title
        self.title = ctk.CTkLabel(self, text="Tambah Data Alumni",
                                  font=ctk.CTkFont(size=28, weight="bold"))
        self.title.grid(row=0, column=0, padx=20, pady=20)

        # Form Frame
        self.form_frame = ctk.CTkFrame(self, fg_color="#4d5291", corner_radius=10)
        self.form_frame.grid(row=1, column=0, padx=20, pady=20)

        # Form Frame Config
        self.form_frame.grid_columnconfigure(0, weight=1)

        # Form Entry
        self.name_entry = self.create_label_entry("Nama Mahasiswa", 1, "Masukkan Nama Lengkap")
        self.email_entry = self.create_label_entry("Email", 2, "Masukkan Email")
        self.year_entry = self.create_label_entry("Tahun Lulus", 3, "Masukkan Tahun Lulus")
        self.number = self.create_label_entry("No. Telepon", 4, "Masukkan No. Telepon")

        # Faculty and Prodi
        self.faculty_combo = self.create_combo_box("Fakultas", 5,
                                                   ["Fakultas Teknik", "Fakultas Ekonomi", "Fakultas Hukum"])
        self.prodi_combo = self.create_combo_box("Prodi", 6,
                                                 ["Teknik Informatika", "Sistem Informasi", "Manajemen", "Akuntansi", "Hukum Pidana"])

        # Submit Button
        self.submit_btn = ctk.CTkButton(self.form_frame, text="Submit",
                                        font=ctk.CTkFont(size=16, weight="bold"), height=40,
                                        command=self.submit_form)
        self.submit_btn.grid(row=7, column=0, padx=10, pady=20, sticky="ew")

    # Submit Button Function
    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        year = self.year_entry.get()
        number = self.number.get()
        faculty = self.faculty_combo.get()
        prodi = self.prodi_combo.get()

        print(f"Name: {name}, Email: {email}, Year: {year}, Number: {number}, Faculty: {faculty}, Prodi: {prodi}")

    # Create Combo Box With Label
    def create_combo_box(self, text, row, values):
        # Combo Box Frame
        combo_frame = ctk.CTkFrame(self.form_frame, fg_color="#32355e")
        combo_frame.grid(row=row, column=0, padx=10, pady=10, sticky="nsew")

        # Entry Frame Config
        combo_frame.grid_rowconfigure((0, 1), weight=1)
        combo_frame.grid_columnconfigure(0, weight=1)

        # Label
        label = ctk.CTkLabel(combo_frame, text=text,
                             font=ctk.CTkFont(size=14))
        label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        # Entry
        combo = ctk.CTkComboBox(combo_frame, values=values, width=500, height=35)
        combo.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        return combo

    # Create Entry With Label
    def create_label_entry(self, text, row, placeholder):
        # Entry Frame
        entry_frame = ctk.CTkFrame(self.form_frame, fg_color="#32355e")
        entry_frame.grid(row=row, column=0, padx=10, pady=10, sticky="nsew")

        # Entry Frame Config
        entry_frame.grid_rowconfigure((0, 1), weight=1)
        entry_frame.grid_columnconfigure(0, weight=1)

        # Label
        label = ctk.CTkLabel(entry_frame, text=text,
                             font=ctk.CTkFont(size=14))
        label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        # Entry
        entry = ctk.CTkEntry(entry_frame, width=500, placeholder_text=placeholder)
        entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        return entry

class CreditsPage(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="#242745")

        self.grid_columnconfigure((0, 1, 2), weight=1)

        # --- Main Title ---
        self.credits_label = ctk.CTkLabel(self, text="Credits",
                                          font=ctk.CTkFont(size=28, weight="bold"))
        self.credits_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        credits_text = {
            1: {
                "title": "Project Manager",
                "name": "Ryan Ivan Pratama"
            },
            2: {
                "title": "Lead Developer",
                "name": "Muhammad Dava Syahputra"
            },
            3: {
                "title": "Documentation & Reporting",
                "name": "Muhammad Rafli Rafsanjani"
            },
            4: {
                "title": "UI/UX Designer",
                "name": "Muhammad Dava Syahputra"
            },
            5: {
                "title": "Debugging",
                "name": "Muhammad Dava Syahputra"
            }
            # You can add more people here
        }

        for index, data in enumerate(credits_text.values()):
            column = index % 3
            row = (index // 3) + 1

            card_frame = ctk.CTkFrame(self, fg_color="#4d5291", corner_radius=10)
            card_frame.grid(row=row, column=column, padx=15, pady=15, sticky="nsew")

            card_frame.grid_rowconfigure(0, weight=1)
            card_frame.grid_rowconfigure(1, weight=1)
            card_frame.grid_columnconfigure(0, weight=1)

            title_label = ctk.CTkLabel(card_frame, text=data["title"],
                                       font=ctk.CTkFont(size=16, weight="bold"))
            title_label.grid(row=0, column=0, padx=10, pady=(10, 2))

            name_label = ctk.CTkLabel(card_frame, text=data["name"],
                                      font=ctk.CTkFont(size=14))
            name_label.grid(row=1, column=0, padx=10, pady=(2, 10))

if __name__ == "__main__":
    app = App()
    app.mainloop()