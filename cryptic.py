# import customtkinter as ctk
import os
import unicodedata as uni


class Encryption:
    """
    encrypt
    """

    def __init__(self, master, path: str, key: str):
        # MASTER FRAME
        self.master = master
        # INPUT
        self.input_path = path
        self.input_txt = ""
        self.key = key
        # OUTPUT
        self.output_path = ""
        self.output_txt = ""

        self.state = False
        self.set_text()

    def configure(self, **kwargs):
        if "input_path" in kwargs:
            self.input_path = kwargs["input_path"]
            self.set_text()
        if "key" in kwargs:
            self.key = kwargs["key"]
            self.set_text()
        if "output_path" in kwargs:
            self.output_path = kwargs["output_path"]

    def set_text(self):
        if os.path.exists(self.input_path):
            with open(self.input_path, "r", encoding="utf-8") as f:
                self.input_txt = f.read()

    def strip_accents(self):

        """
        remove accents from text
        """
        text = self.input_txt
        try:
            text = unicode(text, 'utf-8')
        except NameError:  # unicode is a default on python 3
            pass

        text = uni.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
        return str(text)

    def encryption(self, reverse=False):
        """
        crypt texte file using key
        return encrypted text
        """
        # check if work with non alphabetic characters in key
        text = self.strip_accents()
        up_txt = text.upper()
        ck = self.key.upper()

        # for every character in input text
        for i in range(len(up_txt)):
            j = i % len(ck)  # enable loop on key character
            # if character is a letter
            if up_txt[i].isalpha():
                # decrypt
                if reverse:
                    cp_char = chr(65 + (ord(up_txt[i]) - ord(self.key[j])) % 26)
                # encrypt
                else:
                    cp_char = chr(65 + (ord(up_txt[i]) + ord(self.key[j])) % 26)

                # encryption in upper or lower
                if self.input_txt[i].isupper():
                    self.output_txt += cp_char.upper()
                else:
                    self.output_txt += cp_char.lower()
            # don't change character if it's not a letter
            else:
                self.output_txt += up_txt[i]
        self.state = True
        return self.output_txt

    def generate_output_path(self, encrypt=True):
        if encrypt:
            # si _decrypted.txt → _encrypted.txt
            if self.input_path.endswith("_decrypted.txt"):
                self.output_path = self.input_path.replace("_decrypted.txt", "_encrypted.txt")

            # si _encrypted.txt → todo popup "deja crypter ?"
            elif self.input_path.endswith("_encrypted.txt"):
                print("le fichier semble DEJA crypter ?")
                self.output_path = self.rename_file(self.input_path)

            # si .txt → _encrypted.txt
            elif self.input_path.endswith(".txt"):
                self.output_path = self.input_path.replace(".txt", "_encrypted.txt")

        else:
            # si _encrypted.txt → _decrypted.txt
            if self.input_path.endswith("_encrypted.txt"):
                self.output_path = self.input_path.replace("_encrypted.txt", "_decrypted.txt")

            # si _decrypted.txt → _decrypted(X).txt todo popup "fichier semble deja decrypter ! = cryptage inverse"
            elif self.input_path.endswith("_decrypted.txt"):
                print("le fichier semble DEJA decrypter! = cryptage inverse")
                self.output_path = self.rename_file(self.input_path)

            # si .txt → todo popup "ficher ne semble pas crypter ? = cryptage inverse !"
            elif self.input_path.endswith(".txt"):
                print("le fichier ne semble PAS crypter ? = cryptage inverse !")
                self.output_path = self.input_path.replace(".txt", "_decrypted.txt")

        self.output_path = self.rename_file(self.output_path)
        return self.output_path

    @staticmethod
    def rename_file(pth_file: str):
        """
        if path already exist
        add: (x) at end of file path
        """
        npf = pth_file
        i = 0
        while os.path.exists(npf):
            i += 1
            npf = "{}({}).txt".format(pth_file.split(".")[0], i)
        return npf

    def save(self):
        path = self.output_path
        path_key = self.output_path.replace(".txt", "_key.txt")
        with open(path, "w", encoding="utf-8") as new_file:
            new_file.write(self.output_txt)
        with open(path_key, "w", encoding="utf-8") as key:
            key.write(self.key)
