import customtkinter
from PIL import Image 
from tkinter import filedialog
import pytesseract as tess
import pyperclip

app = customtkinter.CTk()
app.geometry('600x500')
app.title('Optical Character Recognization')

# create frame
frame = customtkinter.CTkFrame(app, corner_radius=20, border_color='#2596be', border_width=2)
frame.pack(padx=20, pady=20, fill='both')

# add text
txt = customtkinter.CTkLabel(frame, text="Extract Text From Image", font=('Arial', 20))
txt.pack(pady=10)

# add image
img = customtkinter.CTkImage(Image.open('29072.png'), size=(42,42))

# function to copy text to clipboard
def copyText():
    text = txt_box.get('1.0', 'end-1c')
    pyperclip.copy(text)
    copy_btn.configure(text='Copied!', state='disabled')

# function to clear textbox
def clearText():
    txt_box.delete('1.0', 'end')
    clear_btn.configure(text='Cleared!', state='disabled')

# function to open Image
def openImage():
    progressbar.set(0)

    filename = filedialog.askopenfilename()
    img1 = Image.open(filename)
    get_txt = tess.image_to_string(img1)
    
    progressbar.start()
    progressbar.set(1)
    
    txt_box.insert('0.0', get_txt)
    app.title(filename)
    progressbar.stop()
    
    # enable copy button and change text
    copy_btn.configure(state='normal', text='Copy Text')
    clear_btn.configure(state='normal', text='Clear Text')

# add btn
btn = customtkinter.CTkButton(frame, text='Add Image',
                    text_color='#FFFFFF',# white color
                    corner_radius=8,
                    image=img,
                    width=200,
                    height=30,
                    compound='right',
                    font=('Arial',20),
                    border_spacing=10,
                    command=openImage,
                    hover_color='#900C3F') 
btn.pack(padx=20,pady=20)   

# add Progressbar
progressbar = customtkinter.CTkProgressBar(frame, progress_color='#900C3F')
progressbar.pack()
progressbar.set(0)

# add textbox
txt_box = customtkinter.CTkTextbox(frame, font=('Arial', 18),
                        width=520,
                        height=350,
                        corner_radius=8)
txt_box.pack(pady=20)

# add button frame
btn_frame = customtkinter.CTkFrame(frame)
btn_frame.pack(pady=10)

# add copy button
copy_btn = customtkinter.CTkButton(btn_frame, text='Copy Text',
    text_color='#FFFFFF',
    corner_radius=8,
    width=200,
    height=30,
    font=('Arial', 20),
    border_spacing=10,
    command=copyText,
    hover_color='#900C3F',
    state='disabled') # initially disabled
copy_btn.pack(side='left', padx=20)

# add clear button
clear_btn = customtkinter.CTkButton(btn_frame, text='Clear Text',
    text_color='#FFFFFF',
    corner_radius=8,
    width=200,
    height=30,
    font=('Arial', 20),
    border_spacing=10,
    command=clearText,
    hover_color='#900C3F',
    state='disabled'
    )
clear_btn.pack(side='left', padx=20)
app.mainloop()

