import speech_recognition as sr
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import threading
import chatgpt


# sisi ui tkinter
root = Tk()
root.title("Jenny")
root.geometry('550x675')
root.resizable(False, False)
root.config(bg='#000')


def command():
    def process_command():
        command_val = chatgpt.record_text()
        bot_val = chatgpt.process_command(command_val)
        print(bot_val)
        
        print("TIME")
        text.insert(END, 'User--->'+command_val+"\n")
        if bot_val != None:
            text.insert(END, 'Jenny--->'+str(bot_val)+"\n")

    # Menjalankan proses pengambilan perintah di thread terpisah
    threading.Thread(target=process_command).start()
         


frame = LabelFrame(root, padx=100, pady=7, borderwidth=0, relief="raised")
frame.config(bg="#000")
frame.grid(row=0, column=1, padx=5, pady=10)

text_label = Label(frame, text="Jenny", font=("Comic Sans MS", 14, "bold"))
text_label.grid(row=0, column=0, padx=20, pady=10)

# Membuka gambar GIF dengan Pillow
gif_image = Image.open('jenny.gif')

# Mengambil setiap bingkai dari gambar GIF
frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif_image)]

# Fungsi untuk menampilkan bingkai berikutnya dari gambar GIF
def next_frame(frame_index=0):
    image_label.config(image=frames[frame_index])
    frame_index = (frame_index + 1) % len(frames)
    root.after(100, next_frame, frame_index)

image_label = Label(frame)
image_label.grid(row=1, column=0, padx=20, pady=10)

# Memulai loop untuk menampilkan bingkai GIF secara berurutan
next_frame()

text = Text(root, font=('courier 10 bold'), bg='#fff')
text.grid(row=2, column=0)
text.place(x=90, y=375,width=375, height=100)


# button ask
COMMAND = Button(root, text="Command", bg='#fff', pady=16, padx=40, borderwidth=3, relief=SOLID, command=command)
COMMAND.place(x=190, y=545)

root.mainloop()
