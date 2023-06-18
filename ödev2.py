
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

follower=" "

root=Tk()
root.geometry("400x400")
root.title("Get Followers")

def GetUsername():
    global follower
    Username=inputusername.get()
    driver=webdriver.Chrome()
    driver.get(f"https://www.instagram.com/{Username}")
    time.sleep(2)
    follower= driver.find_elements(By.CLASS_NAME, "_ac2a")
    follower=follower[1].text
    label2=ttk.Label(frame,text=f"Takipçi Sayısı: {follower}")
    label2.grid(column=1,row=1)
    

inputusername=StringVar()

frame=ttk.Frame(root)
frame.grid()

label=ttk.Label(frame, text="Username")
label.grid(column=0,row=0)

entry=ttk.Entry(frame, textvariable=inputusername)
entry.grid(column=1,row=0)
entry.focus()

button=ttk.Button(frame, text="Follower Count", command=GetUsername)
button.grid(column=2,row=0)

root.mainloop()






