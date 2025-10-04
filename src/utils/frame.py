import customtkinter as ctk

# Dual Frame Function
def create_dual_frame(form_frame: ctk.CTkFrame, row: int, column: int):
    frame = ctk.CTkFrame(form_frame, fg_color="#32355e")
    frame.grid(row=row, column=column, columnspan=2, padx=10, pady=10, sticky="nsew")

    frame.grid_rowconfigure((0, 1), weight=1)
    frame.grid_columnconfigure((0, 1), weight=1)

    return frame

def create_triple_frame(form_frame: ctk.CTkFrame, row: int, column: int):
    frame = ctk.CTkFrame(form_frame, fg_color="#32355e")
    frame.grid(row=row, column=column, columnspan=2, padx=10, pady=10, sticky="nsew")

    frame.grid_rowconfigure((0, 1, 2), weight=1)
    frame.grid_columnconfigure((0, 1, 2), weight=1)

    return frame


# Entry Frame Function
def create_entry_frame(form_frame: ctk.CTkFrame, row: int, column: int):
    frame = ctk.CTkFrame(form_frame, fg_color="#32355e")
    frame.grid(row=row, column=column, columnspan=2, padx=10, pady=10, sticky="nsew")

    frame.grid_rowconfigure((0, 1), weight=1)
    frame.grid_columnconfigure(0, weight=1)

    return frame
