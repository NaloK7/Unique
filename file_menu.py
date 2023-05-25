import customtkinter as ctk


class FileMenu:
    """
    Menu "Fichier"
    """

    def __init__(self, master, height):
        # menu frame
        self.menu_frame = ctk.CTkFrame(master,
                                       height=height,
                                       corner_radius=0,
                                       fg_color=("white", "black"))
        self.menu_frame.place(x=0,
                              y=0,
                              relwidth=1)

        # inside menu
        self.options = ctk.CTkOptionMenu(self.menu_frame,
                                         width=85,
                                         height=20,
                                         corner_radius=0,
                                         values=["Aide"],
                                         text_color="white",
                                         )  # put self.options.set("   Fichier") in callback function
        self.options.place(x=0,
                           y=0,
                           )
        # "title" menu
        self.options.set("   Fichier")

        # appearance menu
        self.appearance_option = ctk.CTkOptionMenu(self.menu_frame,
                                                   width=90,
                                                   height=20,
                                                   corner_radius=0,
                                                   values=["Light", "Dark"],
                                                   text_color=("black", "white"),
                                                   fg_color=("white", "black"),
                                                   button_color=("white", "black"),
                                                   button_hover_color=("white", "black"),
                                                   command=self.optionmenu_callback,
                                                   )
        self.appearance_option.place(x=66,
                                     y=0,
                                     )
        self.appearance_option.set("   Apparence")

        # menu frame
        self.menu_frame = ctk.CTkFrame(self.menu_frame,
                                       height=20,
                                       corner_radius=0,
                                       fg_color=("white", "black"))
        self.menu_frame.place(x=145,
                              y=0,
                              relwidth=1)

    def optionmenu_callback(self, choice):
        if choice == "Light" or "Dark":
            self.change_appearance_to_light(choice)

    def change_appearance_to_light(self, choice):
        ctk.set_appearance_mode(choice)
        self.appearance_option.set("   Apparence")
