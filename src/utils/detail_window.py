import customtkinter as ctk
import pathlib
from PIL import Image

root_path = pathlib.Path(__file__).parent.parent.parent.absolute()

class DetailWindow(ctk.CTkToplevel):
    def __init__(self, message: str):
        super().__init__(fg_color="#242745")

        # Configure the window
        self.title("Detail Alumni")
        self.geometry("690x450")
        self.resizable(False, False)

        # Main frame config
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure((0, 2), weight=0)

        # Title Label
        self.info = ctk.CTkLabel(self, text="Detail Alumni", font=ctk.CTkFont(size=20, weight="bold"))
        self.info.grid(row=0, column=0, padx=10, pady=10)

        # Detail frame
        self.detail_frame = ctk.CTkFrame(self, fg_color="#4d5291")
        self.detail_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.detail_frame.grid_columnconfigure(0, weight=0)
        self.detail_frame.grid_columnconfigure(1, weight=1)
        self.detail_frame.grid_rowconfigure(0, weight=1)

        # Profile Picture
        self.profile_pic = ctk.CTkImage(light_image=Image.open(str(root_path / "image" / "user.png")),
                                        size=(100, 100))
        self.profile_pic_frame = ctk.CTkLabel(self.detail_frame, image=self.profile_pic, text="")
        self.profile_pic_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Detail Label
        self.detail_label = ctk.CTkLabel(self.detail_frame, text=message, justify="left",
                                         font=ctk.CTkFont(family="Consolas", size=16))
        self.detail_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Button
        # Back Button
        self.close_button = ctk.CTkButton(self, text="Kembali", command=self.destroy)
        self.close_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")