import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Perbaikan Citra")
        self.master.geometry("500x500")
        
        # membuat tombol untuk memilih citra
        self.btn_buka = tk.Button(self.master, text="Buka Citra", command=self.buka_citra)
        self.btn_buka.pack()
        
        # membuat canvas untuk menampilkan citra
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        
        # membuat tombol untuk melakukan perbaikan citra
        self.btn_perbaiki = tk.Button(self.master, text="Perbaiki Citra", command=self.perbaiki_citra, state="disabled")
        self.btn_perbaiki.pack()
        
    def buka_citra(self):
        # membuka dialog untuk memilih file citra
        self.file_path = filedialog.askopenfilename()
        
        # membaca citra dan menampilkan di canvas
        img = Image.open(self.file_path)
        img = img.resize((400, 400))
        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
        
        # mengaktifkan tombol untuk melakukan perbaikan citra
        self.btn_perbaiki["state"] = "normal"
    
    def perbaiki_citra(self):
        # membaca citra dengan OpenCV
        img = cv2.imread(self.file_path)
        
        # melakukan penyesuaian warna
        alpha = 1.2 # faktor brightness
        beta = 30 # faktor contrast
        img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
        
        # menyimpan citra yang telah diperbaiki
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(img)
        im.save('citra_setelah_diperbaiki.jpg')
        
        # membaca citra yang telah diperbaiki dan menampilkan di canvas
        img = Image.open('citra_setelah_diperbaiki.jpg')
        img = img.resize((400, 400))
        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
