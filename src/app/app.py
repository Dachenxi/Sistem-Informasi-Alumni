import re
from tksheet import Sheet
from src.utils import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Informasi Alumni")
        # 1. Define your desired window size
        window_width = 1100
        window_height = 580
        self.geometry(f"{window_width}x{window_height}")
        self.resizable(False, False)
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
        self.current_page = page_class(self.content_frame, controller=self)
        self.current_page.grid(row=0, column=0, sticky="nsew")

    def go_back_to_add_data_page(self):
        self.show_page(AddDataPage)

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

        menu_1_btn = ctk.CTkButton(self, text="Tambah Data",
                                   font=ctk.CTkFont(weight="bold"), height=35,
                                   command=lambda: self.controller.show_page(AddDataPage))
        menu_1_btn.grid(row=2, column=0, padx=20, pady=10)

        menu_2_btn = ctk.CTkButton(self, text="Data Alumni",
                                   font=ctk.CTkFont(weight="bold"), height=35,
                                   command=lambda: self.controller.show_page(DataAlumni))
        menu_2_btn.grid(row=3, column=0, padx=20, pady=10)

        credit_btn = ctk.CTkButton(self,text="Credits",
                                   font=ctk.CTkFont(weight="bold"), height=35,
                                   command=lambda: self.controller.show_page(CreditsPage))
        credit_btn.grid(row=8, column=0, padx=20, pady=10, sticky="s")

class DashboardPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, corner_radius=0, fg_color="#242745")
        self.controller = controller

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

        self.dashboard_data = get_dashboard_data()

        # --- Create and Place the Info Cards ---
        # Card 1: Total Alumni
        total_alumni_card = self.create_info_card(title="Total Alumni", value=self.dashboard_data["total_alumni"])
        total_alumni_card.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Card 2: Total Fakultas
        total_faculty_card = self.create_info_card(title="Total Fakultas", value=self.dashboard_data["total_faculty"])
        total_faculty_card.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        # Card 3: Total Prodi
        total_prodi_card = self.create_info_card(title="Total Prodi", value=self.dashboard_data["total_major"])
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
        card_title_label.grid(row=0, column=0, padx=20, pady=(15, 5), sticky="nsew")

        # Create the value label inside the card
        card_value_label = ctk.CTkLabel(card_frame, text=value,
                                        font=ctk.CTkFont(size=40, weight="bold"))
        card_value_label.grid(row=1, column=0, padx=20, pady=(5, 15), sticky="nsew")

        return card_frame

class AddDataPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, corner_radius=0, fg_color="#242745")
        self.controller = controller

        # Main Frame Config
        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add Data Title
        self.title = ctk.CTkLabel(self, text="Tambah Data",
                                  font=ctk.CTkFont(size=28, weight="bold"))
        self.title.grid(row=0, column=0, padx=20, pady=20)

        # Button Frame
        self.button_frame = ctk.CTkFrame(self, fg_color="#32355e")
        self.button_frame.grid(row=1, column=0)
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # Add Alumni Button
        self.alumni_button = ctk.CTkButton(self.button_frame,
                                           width=250, height=60,
                                           text="Tambah Data Alumni",
                                           font=ctk.CTkFont(size=16, weight="bold"),
                                           command=lambda: self.controller.show_page(AddNewAlumniPage))
        self.alumni_button.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="nsew")

        # Add Faculty Button
        self.faculty_button = ctk.CTkButton(self.button_frame,
                                            width=250, height=60,
                                            text="Tambah Data Fakultas",
                                            font=ctk.CTkFont(size=16, weight="bold"),
                                            command=lambda: self.controller.show_page(AddNewFacultyPage))
        self.faculty_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Add Prodi Button
        self.prodi_button = ctk.CTkButton(self.button_frame,
                                          width=250, height=60,
                                          text="Tambah Data Prodi",
                                          font=ctk.CTkFont(size=16, weight="bold"),
                                          command=lambda: self.controller.show_page(AddNewMajorPage))
        self.prodi_button.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")

class AddNewAlumniPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, corner_radius=0, fg_color="#242745")
        self.controller = controller

        # Main Frame Config
        self.grid_columnconfigure(0, weight=1) # Center content
        self.grid_rowconfigure((0, 1), weight=0) # Form and Title
        self.grid_rowconfigure(2, weight=1) # Spacer

        # Title
        self.title = ctk.CTkLabel(self, text="Tambah Data Alumni",
                                  font=ctk.CTkFont(size=28, weight="bold"))
        self.title.grid(row=0, column=0, padx=20, pady=(20, 0))

        # Form Frame
        self.form_frame = ctk.CTkFrame(self, fg_color="#4d5291", corner_radius=10)
        self.form_frame.grid(row=1, column=0, padx=20, pady=20)

        # Form Frame Config
        self.form_frame.grid_columnconfigure((0, 1), weight=1)

        # Form
        # Name Entry
        name_frame = create_entry_frame(self.form_frame, row=1, column=0)
        self.name_entry_label = ctk.CTkLabel(name_frame, text="Nama Mahasiswa")
        self.name_entry = ctk.CTkEntry(name_frame, width=250, placeholder_text="Example: John Doe")
        self.name_entry_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.name_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        # Email and telephone number Entry
        et_frame = create_dual_frame(self.form_frame, row=2, column=0)

        self.email_entry_label = ctk.CTkLabel(et_frame, text="Email")
        self.email_entry = ctk.CTkEntry(et_frame, width=250, placeholder_text="Example: xxxx@xxx.xxx")
        self.email_entry_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.email_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        self.number_entry_label = ctk.CTkLabel(et_frame, text="No. Telepon")
        self.number_entry = ctk.CTkEntry(et_frame, width=250, placeholder_text="Example: 6208123456")
        self.number_entry_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")
        self.number_entry.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="ew")

        # Year Entry
        year_frame = create_dual_frame(self.form_frame, row=3, column=0)

        self.grad_year_label = ctk.CTkLabel(year_frame, text="Tahun Lulus")
        self.grad_year_entry = ctk.CTkEntry(year_frame, width=250, placeholder_text="Example: 2020")
        self.grad_year_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.grad_year_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        self.year_entry_label = ctk.CTkLabel(year_frame, text="Angkatan")
        self.year_entry = ctk.CTkEntry(year_frame, width=250, placeholder_text="Example: 2020")
        self.year_entry_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")
        self.year_entry.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="ew")

        # Faculty and Prodi
        fp_frame = create_dual_frame(self.form_frame, row=4, column=0)

        self.faculty_list = get_all_faculty()
        self.faculty_dict = {
            faculty.name: faculty.id
            for faculty in self.faculty_list
        }

        self.faculty_combo_label = ctk.CTkLabel(fp_frame, text="Fakultas")
        self.faculty_combo = ctk.CTkComboBox(fp_frame, values=list(self.faculty_dict.keys()), command=self._prodi_update)
        self.faculty_combo.set(value="Pilih Fakultas")
        self.faculty_combo_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.faculty_combo.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        self.prodi_combo_label = ctk.CTkLabel(fp_frame, text="Prodi")
        self.prodi_combo = ctk.CTkComboBox(fp_frame, values=["Pilih Fakultas Dahulu"])
        self.prodi_combo_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")
        self.prodi_combo.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="ew")

        # Back Button
        self.back_btn = ctk.CTkButton(self.form_frame, text="Kembali",
                                      font=ctk.CTkFont(size=16, weight="bold"), height=40,
                                      fg_color="#913030", hover_color="#782828",
                                      command=lambda: self.controller.show_page(AddDataPage))
        self.back_btn.grid(row=7, column=0, padx=10, pady=20, sticky="ew")

        # Submit Button
        self.submit_btn = ctk.CTkButton(self.form_frame, text="Submit",
                                        font=ctk.CTkFont(size=16, weight="bold"), height=40,
                                        fg_color="#309145", hover_color="#287839",
                                        command=self.validate_and_save)
        self.submit_btn.grid(row=7, column=1, padx=10, pady=20, sticky="ew")

    # Prodi Combo Box Update Function
    def _prodi_update(self, selected_faculty_name: str):
        faculty_id = self.faculty_dict.get(selected_faculty_name)
        self.prodi_list = {
            prodi.name: prodi
            for prodi in get_all_prodi(faculty=faculty_id)
        }
        major_name = list(self.prodi_list.keys())
        self.prodi_combo.configure(values=major_name)
        if major_name:
            # Set to the first item only if the list is not empty
            self.prodi_combo.set(major_name[0])
        else:
            # Handle the case where a faculty has no programs
            self.prodi_combo.set("Tidak ada Prodi")

    # Submit Button Function
    def validate_and_save(self):
        # Get values from entry widgets, using .strip() to remove whitespace
        # Get all values first
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        grad_year = self.grad_year_entry.get().strip()
        year = self.year_entry.get().strip()
        number = self.number_entry.get().strip()

        error_messages = []

        # 1. Define all validation rules in one place
        validation_rules = [
            {
                "value": name,
                "name": "Nama",
                "rules": [
                    {"rule": lambda v: v, "message": "wajib diisi."}  # Checks if not empty
                ]
            },
            {
                "value": email,
                "name": "Email",
                "rules": [
                    {"rule": lambda v: v, "message": "wajib diisi."},
                    {"rule": lambda v: re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", v),
                     "message": "format tidak valid."}
                ]
            },
            {
                "value": grad_year,
                "name": "Angkatan",
                "rules": [
                    {"rule": lambda v: v, "message": "wajib diisi."},
                    {"rule": lambda v: v.isdigit(), "message": "harus berupa angka."}
                ]
            },
            {
                "value": year,
                "name": "Tahun lulus",
                "rules": [
                    {"rule": lambda v: v, "message": "wajib diisi."},
                    {"rule": lambda v: v.isdigit(), "message": "harus berupa angka."}
                ]
            },
            {
                "value": number,
                "name": "Nomor telepon",
                "rules": [
                    {"rule": lambda v: v, "message": "wajib diisi."},
                    {"rule": lambda v: v.isdigit(), "message": "harus berupa angka."}
                ]
            }
        ]

        # 2. A single loop to process all rules
        for item in validation_rules:
            value_to_check = item["value"]
            field_name = item["name"]

            for validation in item["rules"]:
                rule = validation["rule"]
                message = validation["message"]

                # Apply the rule. If it fails, add error message and stop checking this item.
                if not rule(value_to_check):
                    error_messages.append(f"• {field_name} {message}")
                    break  # Go to the next field (e.g., if email is empty, don't check its format)

        # 3. Show errors if any
        if error_messages:
            full_error_message = "Harap perbaiki kesalahan berikut:\n\n" + "\n".join(error_messages)
            MessageBox("Input Tidak Valid", message=full_error_message)
            return

        # 4. If all validations pass, proceed to save the data
        selected_prodi_name = self.prodi_combo.get()
        selected_major_object = self.prodi_list.get(selected_prodi_name)
        nim = f"{selected_major_object.code}{year}{get_last_nim(selected_major_object.id, year) + 1:03}"
        confirmation_text = (f"NIM          : {nim}\n"
                             f"Nama         : {name}\n"
                             f"Email        : {email}\n"
                             f"No. Telepon  : {number}\n"
                             f"Tahun Lulus  : {grad_year}\n"
                             f"Angkatan     : {year}\n"
                             f"Fakultas     : {self.faculty_combo.get()}\n"
                             f"Prodi        : {selected_prodi_name}")

        test = ConfirmationWindow(message = confirmation_text)

        self.wait_window(test)
        if test.result:
            add_alumni(nim=nim,
                       nama=name,
                       tahun_lulus=int(grad_year),
                       email=email,
                       nomor_telepon=int(number),
                       id_prodi=selected_major_object.id,
                       angkatan=year)

            self.name_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.grad_year_entry.delete(0, "end")
            self.year_entry.delete(0, "end")
            self.number_entry.delete(0, "end")
            self.faculty_combo.set("Pilih Fakultas")
            self.prodi_combo.set("Pilih Fakultas Dahulu")

class AddNewFacultyPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, corner_radius=0, fg_color="#242745")
        self.controller = controller

        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self, text="Tambah Data Fakultas",
                                  font=ctk.CTkFont(size=28, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # Form Frame
        self.form_frame = ctk.CTkFrame(self, fg_color="#4d5291", corner_radius=10)
        self.form_frame.grid(row=1, column=0, padx=20, pady=20)

        # Form Frame Config
        self.form_frame.grid_columnconfigure((0, 1), weight=1)

        # Name Entry
        name_frame = create_entry_frame(self.form_frame, row=1, column=0)
        self.name_entry_label = ctk.CTkLabel(name_frame, text="Nama Fakultas")
        self.name_entry = ctk.CTkEntry(name_frame, width=250, placeholder_text="Example: Fakultas Teknik")
        self.name_entry_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.name_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        # Back Button
        self.back_btn = ctk.CTkButton(self.form_frame, text="Kembali",
                                      font=ctk.CTkFont(size=16, weight="bold"), height=40,
                                      fg_color="#913030", hover_color="#782828",
                                      command=lambda: self.controller.show_page(AddDataPage))
        self.back_btn.grid(row=7, column=0, padx=10, pady=20, sticky="ew")

        # Submit Button
        self.submit_btn = ctk.CTkButton(self.form_frame, text="Submit",
                                        font=ctk.CTkFont(size=16, weight="bold"), height=40,
                                        fg_color="#309145", hover_color="#287839",
                                        command=self._save_data)
        self.submit_btn.grid(row=7, column=1, padx=10, pady=20, sticky="ew")

    def _save_data(self):
        # Check if their numeric in the name entry
        faculty_name = self.name_entry.get()
        if any(char.isdigit() for char in faculty_name):
            MessageBox("Input Tidak Valid", message="Nama fakultas tidak boleh mengandung angka.")
            return

        status = add_faculty(nama_fakultas=faculty_name)
        if status:
            MessageBox("Sukses", message="Data fakultas berhasil ditambahkan.")
            self.name_entry.delete(0, "end")
        else:
            MessageBox("Gagal", message="Data Fakultas bertabrakan dengan \ndata yang sudah ada.")

class AddNewMajorPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, corner_radius=0, fg_color="#242745")
        self.controller = controller

        # Main Frame Config
        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Title
        self.label = ctk.CTkLabel(self, text="Tambah Data Prodi",
                                  font=ctk.CTkFont(size=28, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # Form Frame
        self.form_frame = ctk.CTkFrame(self, fg_color="#4d5291", corner_radius=10)
        self.form_frame.grid(row=1, column=0, padx=20, pady=20)

        # Form Frame Config
        self.form_frame.grid_columnconfigure((0, 1), weight=1)

        # Name Entry
        name_frame = create_entry_frame(self.form_frame, row=1, column=0)
        self.name_entry_label = ctk.CTkLabel(name_frame, text="Nama Prodi")
        self.name_entry = ctk.CTkEntry(name_frame, width=250, placeholder_text="Example: Teknik Informatika")
        self.name_entry_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.name_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        # Major Code and Accreditation
        self.ma_frame = create_entry_frame(self.form_frame, row=2, column=0)

        # Faculty Combo Box
        self.faculty_combo_label = ctk.CTkLabel(self.ma_frame, text="Fakultas")
        self.faculty_combo_box = ctk.CTkComboBox(self.ma_frame, values=[faculty.name for faculty in get_all_faculty()])
        self.faculty_combo_box.set(value="Pilih Fakultas")
        self.faculty_combo_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.faculty_combo_box.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        # Major Code
        self.code_entry_label = ctk.CTkLabel(self.ma_frame, text="Kode Prodi")
        self.code_entry = ctk.CTkEntry(self.ma_frame, width=200, placeholder_text="Example: TI")
        self.code_entry_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")
        self.code_entry.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="ew")

        # Akreditasi Entry
        self.akreditasi_entry_label = ctk.CTkLabel(self.ma_frame, text="Akreditasi")
        self.akreditasi_entry = ctk.CTkEntry(self.ma_frame, width=200, placeholder_text="Example: A")
        self.akreditasi_entry_label.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="w")
        self.akreditasi_entry.grid(row=1, column=2, padx=10, pady=(0, 10), sticky="ew")

        # Back Button
        self.back_btn = ctk.CTkButton(self.form_frame, text="Kembali",
                                      font=ctk.CTkFont(size=16, weight="bold"), height=40,
                                      fg_color="#913030", hover_color="#782828",
                                      command=lambda: self.controller.show_page(AddDataPage))
        self.back_btn.grid(row=7, column=0, padx=10, pady=20, sticky="ew")

        # Submit Button
        self.submit_btn = ctk.CTkButton(self.form_frame, text="Submit",
                                        font=ctk.CTkFont(size=16, weight="bold"), height=40,
                                        fg_color="#309145", hover_color="#287839",
                                        command=self._save_data)
        self.submit_btn.grid(row=7, column=1, padx=10, pady=20, sticky="ew")

    def _save_data(self):
        # Check if their numeric in the name entry
        major_name = self.name_entry.get()
        if any(char.isdigit() for char in major_name):
            MessageBox("Input Tidak Valid", message="Nama prodi tidak boleh mengandung angka.")
            return

        status = add_major(nama_prodi=major_name,
                           kode_prodi=self.code_entry.get(),
                           akreditasi=self.akreditasi_entry.get(),
                           fakultas=self.faculty_combo_box.get())
        if status:
            MessageBox("Sukses", message="Data prodi berhasil ditambahkan.")
            self.name_entry.delete(0, "end")
            self.code_entry.delete(0, "end")
            self.akreditasi_entry.delete(0, "end")
            self.faculty_combo_box.set("Pilih Fakultas")
        else:
            MessageBox("Gagal", message="Data Prodi bertabrakan dengan \ndata yang sudah ada.")

class DataAlumni(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, corner_radius=0, fg_color="#242745")
        self.controller = controller

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)

        # Filter Frame
        self.filter_frame = ctk.CTkFrame(self, fg_color="#4d5291", corner_radius=10)
        self.filter_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,0), sticky="ew")
        self.filter_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.filter_frame.grid_rowconfigure(0, weight=1)

        # Search
        self.search_label = ctk.CTkLabel(self.filter_frame, text="Filter")
        self.search_entry = ctk.CTkEntry(self.filter_frame, width=500, placeholder_text="Filter Entry")
        self.search_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Filter Combo Box
        self.filter_combo_box = ctk.CTkComboBox(self.filter_frame,
                                                values=["Nim", "Nama", "Fakultas", "Prodi"])
        self.filter_combo_box.set(value="Pilih Filter")
        self.filter_combo_box.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        # Search Button
        self.search_button = ctk.CTkButton(self.filter_frame, text="Search", width=100,
                                           command=self._filter_data)
        self.search_button.grid(row=0, column=3, padx=10, pady=10, sticky="e")

        # Table
        self.table = Sheet(self, table_wrap="w")
        self.table.headers(['Nim', 'Nama', 'Tahun Lulus', 'Angkatan', 'Email', 'No. Telepon', 'Prodi', 'Fakultas'])
        self.table.column_width(column="all", width=150)
        self.table.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.table.set_options(table_font=("Roboto", 15, 'normal'),
                               header_font=("Roboto", 16, 'bold'),
                               index_font=("Roboto", 16, 'bold'))

        self.table.enable_bindings('single_select', 'ctrl_click_select', 'copy', 'sort_columns')

        # Button Frame
        self.button_frame = ctk.CTkFrame(self, fg_color="#4d5291", corner_radius=10)
        self.button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="ew")
        self.button_frame.grid_columnconfigure((0, 1), weight=1)

        # Button
        delete_data = ctk.CTkButton(self.button_frame, text="Delete Data")
        check_data = ctk.CTkButton(self.button_frame, text="Detail Aumni",
                                   command=self._detail_alumni)
        delete_data.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        check_data.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Get Alumni data
        self._load_data(get_all_alumni())

    def check_data(self):
        row_data = self.table.get_currently_selected().row
        data_list = list(self.table.get_row_data(row_data))
        print(data_list)

    def _load_data(self, data: list[Alumni]):
        self.data_list = [
            [alumnus.nim, alumnus.name, alumnus.graduation_year, alumnus.entry_year, alumnus.email,
             alumnus.phone_number, alumnus.major.name, alumnus.faculty.name]
            for alumnus in data
        ]
        self.table.set_sheet_data(self.data_list)
        self.table.set_all_cell_sizes_to_text()

    def _detail_alumni(self):
        row_data = self.table.get_currently_selected()
        if not row_data:
            return
        data_list = list(self.table.get_row_data(row_data.row))
        data = get_alumni_by_nim(data_list[0])

        detail_message = (f"NIM          : {data.nim}\n"
                          f"Nama         : {data.name}\n"
                          f"Email        : {data.email}\n"
                          f"No. Telepon  : {data.phone_number}\n"
                          f"Tahun Lulus  : {data.graduation_year}\n"
                          f"Angkatan     : {data.entry_year}\n"
                          f"Fakultas     : {data.faculty.name}\n"
                          f"Prodi        : {data.major.name}\n"
                          f"Kode Prodi   : {data.major.code}\n"
                          f"Akreditasi   : {data.major.acreditation}")

        DetailWindow(message=detail_message)

    def _filter_data(self):
        filter_condition = self.filter_combo_box.get()
        filter_value = self.search_entry.get()

        if "Pilih Filter" in filter_condition and not filter_value == "":
            MessageBox("Filter Tidak Valid", message="Silakan pilih kondisi filter terlebih dahulu.")
            return

        if filter_value:
            data = filter_alumni(filter_condition, filter_value)
            self._load_data(data)
        else:
            self._load_data(get_all_alumni())

class CreditsPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, corner_radius=0, fg_color="#242745")
        self.controller = controller

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