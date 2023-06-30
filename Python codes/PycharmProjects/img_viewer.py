from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')


img1=ImageTk.PhotoImage(Image.open('eagle.png'))
img2=ImageTk.PhotoImage(Image.open('smoke.png'))
img3=ImageTk.PhotoImage(Image.open('flowers.png'))
img4=ImageTk.PhotoImage(Image.open('tree.png'))
img5=ImageTk.PhotoImage(Image.open('lion.png'))
img6=ImageTk.PhotoImage(Image.open('cloud.png'))
img7=ImageTk.PhotoImage(Image.open('waterdrop.png'))
img8=ImageTk.PhotoImage(Image.open('dog.png'))


img_list=[img1, img2, img3, img4, img5, img6, img7, img8]

label=Label(image=img1)
label.grid(row=0, column=0, columnspan=3)

def forward(img_num):
    global label
    global next_img
    global prev_img
    
    label.grid_forget()
    label=Label(image=img_list[img_num-1])
    
    next_img= Button(root, text=">>", command=lambda: forward(img_num +1))
    prev_img= Button(root, text="<<", command=lambda: back(img_num -1))
    
    if img_num==8:
        next_img= Button(root, text='>>', state= DISABLED)
    
    label.grid(row=0, column=0, columnspan=3)
    prev_img.grid(row=1, column=0)
    next_img.grid(row=1, column=2)
    
def back(img_num):
    global label
    global next_img
    global prev_img
    
    label.grid_forget()
    label=Label(image=img_list[img_num-1])
    
    next_img= Button(root, text=">>", command=lambda: forward(img_num +1))
    prev_img= Button(root, text="<<", command=lambda: back(img_num -1))
    
    if img_num==1:
        prev_img= Button(root, text='<<', state= DISABLED)
    
    label.grid(row=0, column=0, columnspan=3)
    prev_img.grid(row=1, column=0)
    next_img.grid(row=1, column=2)
    
prev_img= Button(root, text='<<', command=back, state=DISABLED)
exit_button= Button(root, text='Quit', command=root.quit)
next_img= Button(root, text='>>', command=lambda: forward(2))


prev_img.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
next_img.grid(row=1, column=2)

#label.pack()
root.mainloop()