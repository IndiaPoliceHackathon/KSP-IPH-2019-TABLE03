__author__ = 'sanganak'

from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import os
from face_match_v3 import match_faces

#os.environ["CUDA_VISIBLE_DEVICES"]="-1"
import torch
from bs4 import BeautifulSoup
import requests
import os.path
my_path = os.path.abspath(os.path.dirname(__file__))
import shutil

k = 3.1416
# globals image_query, url_val
#print(my_path)
#path = my_path + '\data\\01_data_mars_opposition.csv'

def url_val_get_files():
    print("The web url being searched is:\n")
    print(url_val.get())
    print(web_destination_folder)
    content = requests.get(url_val.get()).content
    soup = BeautifulSoup(content,'lxml') # choose lxml parser
    image_tags = soup.findAll('img') # find the tag : <img ... >
# print out image urls
    count=1
    for image_tag in image_tags:
        local_image_filename = os.path.join(web_destination_folder ,str(count) + '.jpg')
        print(local_image_filename)
        print(image_tag.get('src'))
        image_url=image_tag.get('src')
        response = requests.get(image_url, stream=True)
        f=open(local_image_filename,'w+')
        with open(local_image_filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        count = count+1
    f.close()

    k=3.1416
    Label(welcome_frame,text="Select the Destination for Storing the Matching Images" + str(k), fg="red",font=("Helvetica", 12, "bold")).pack()
    match_destination_folder = filedialog.askdirectory()
    print("The matching images will be stored at:",match_destination_folder)
    Label(op_frame,text="The Number of Matches Found" + str(k), fg="brown",font=("Helvetica", 12, "bold")).pack()


def select_query_image():
    global image_query
    image_query = filedialog.askopenfile()
    print("The queried image to be searched is: \n",image_query.name)
# image_query.name stores the path of queried image


#autoimatically opens for destination folder and prompts user to enter URL
def web_search():
   global url_val                            #url
   global web_destination_folder             #web destination
   next_frame = Frame(root)
   next_frame.pack(side=LEFT)
   Label(welcome_frame,text="Select the Destination Folder to Download all Images from Website",fg="brown",font=("Helvetica", 12, "bold")).pack()
   web_destination_folder = filedialog.askdirectory()
   Label(next_frame,text="Enter URL",fg="blue",font=("Helvetica", 12, "bold")).pack()
   url_val=StringVar()
   Entry(next_frame,textvariable=url_val).pack()
   Button(text="CLICK TO DOWNLOAD FROM URL",fg="red",font=("Helvetica", 12, "bold"),command=url_val_get_files).pack(side=LEFT,pady=12)
   print("The destination folder for web Images is : \n",web_destination_folder)
#   web_scrape(url_val,web_destination_folder)

"""
def web_scrape(url,image_folder):
   content = requests.get(url).content
   soup = BeautifulSoup(content,'lxml') # choose lxml parser
# find the tag : <img ... >
   image_tags = soup.findAll('img')
# print out image urls
   count=1
   for image_tag in image_tags:
        local_image_filename = image_folder + '\\IMDB\\'+ str(count) + '.jpg'
        print(local_image_filename)
        print(image_tag.get('src'))
        image_url=image_tag.get('src')
        response = requests.get(image_url, stream=True)
        f=open(local_image_filename,'w+')
        with open(local_image_filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        count = count+1
        f.close()
        return
"""
def database_search():
    Label(welcome_frame,text="Select the Folder where matching Images are Stored",fg="brown",font=("Helvetica", 12, "bold")).pack()
    image_database = filedialog.askdirectory()
    print("The matching images will be searched in : \n",image_database)

    Label(welcome_frame,text="Select the Destination for Storing the Matching Images", fg="brown",font=("Helvetica", 12, "bold")).pack()
    match_destination_folder = filedialog.askdirectory()

    _,_a,mm,meow=match_faces(query_folder,image_database,match_destination_folder)
    
    print("The matching images will be stored at:",match_destination_folder)
    Label(op_frame,text="The Number of Matches Found / Unfound is : " + str(meow[0])+ " / "+ str(meow[1]), fg="brown",font=("Helvetica", 12, "bold")).pack()


def gen_all_image():
    Label(welcome_frame,text="Select the Folder to store all Synthetically Generated Images",fg="brown",font=("Helvetica", 12, "bold")).pack()
    output_image_database = filedialog.askdirectory()
    print("All generated images of the queried person will be stored in : \n",output_image_database)

def video_search():
    Label(welcome_frame,text="Select the Video File",fg="brown",font=("Helvetica", 12, "bold")).pack()
    video_query = filedialog.askopenfile()
    print("The queried image will be searched in this Video File: \n",video_query.name)
    Label(welcome_frame,text="Matching Frames will be stored at",fg="red",font=("Helvetica", 12, "bold")).pack()
    match_destination_folder = filedialog.askdirectory()
    print("The matching frames will be stored at:",match_destination_folder)
    Label(op_frame,text="The Matches Found at" + str(k) + "minutes", fg="brown",font=("Helvetica", 12, "bold")).pack()


f = 3.1412
dis=None
def sys_config():
    global dis
    #Label(diagnostic_frame,text="Computational Complexity is" ,fg="brown",font=("Helvetica", 12, "bold")).pack()
    choice=var_radio.get()
    if dis is None:
        if choice == 1:
            print("GPU")
            dis=Label(diagnostic_frame,text="Using GPU -- Complexity is "+str(k) ,fg="brown",font=("Helvetica", 12, "bold")).pack()
        elif choice == 2:
            print("CPU")
            dis=Label(diagnostic_frame,text="Using CPU -- Complexity is "+str(k) ,fg="brown",font=("Helvetica", 12, "bold")).pack()
    else:
        print('here')
        if choice == 1:
            print("GPU")
            dis.configure(text="Using GPU -- Complexity is "+str(k))
        elif choice == 2:
            print("CPU")
            dis.configure(text="Using CPU -- Complexity is "+str(k))
 
def anthropometry():
    print("anthropometry")
    Label(op_frame,text="Age is "+str(k) ,fg="brown",font=("Helvetica", 12, "bold")).pack(side=RIGHT)


def search_in_live_stream():
    stream_url=live_stream_url.get()
    print(stream_url)

def live_streaming():
   global live_stream_url
   next_frame = Frame(root)
   next_frame.pack(side=LEFT)
   Label(next_frame,text="Enter Live Stream URL",fg="blue",font=("Helvetica", 12, "bold")).pack()
   live_stream_url=StringVar()
   Entry(next_frame,textvariable=live_stream_url).pack()
   Button(text="SEARCH",fg="red",font=("Helvetica", 12, "bold"),command=search_in_live_stream).pack(side=LEFT)

query_folder=None
def select_query_folder():
    global query_folder
    query_folder = filedialog.askdirectory()
    print("The folder of images to be searched is : \n",query_folder)
   
def reset():
    root.destroy()

root = Tk()

root.title("Sarvatra_IISc")
root.geometry("1200x650") # width x height
root.minsize(1200,650) #width, hieght    #bare minimum canvas size
root.maxsize(1200,650)#maximum canvas size

# welcome Frame and labels
welcome_frame = Frame(root)
welcome_frame.pack(side=TOP)

iisc_logo = PhotoImage(file='media/iisc_logo.png')
banner_logo = Label(welcome_frame,image=iisc_logo,bg="blue")
banner_logo.pack(side='top')
#banner_logo_right.pack(anchor='ne',side='top',fill='x')

banner_message = Label(welcome_frame,text="Image Analytics Software by Team Sarvatra (IISc)",fg="red",font=("Helvetica", 20, "bold"))
banner_message.pack(side=TOP)

# Diagnostic frame
diagnostic_frame= Frame(root,borderwidth=12,bg="white",relief="ridge")
diagnostic_frame.pack(side=LEFT)
#diagnostic_frame.grid(rows=1,columns=2)
if torch.cuda.is_available():
    
    var_radio=IntVar()
    Label(diagnostic_frame,text="System Configuration",font=("Helvetica", 12, "bold"),fg="blue").pack(side=TOP)
    radio=Radiobutton(diagnostic_frame,text='GPU',font=("Helvetica", 12, "bold"),variable=var_radio,value=1,command=sys_config).pack(side=TOP)
    radio=Radiobutton(diagnostic_frame,text='CPU',font=("Helvetica", 12, "bold"),variable=var_radio,value=2,command=sys_config).pack(side=TOP)
else:
    
    var_radio=IntVar()
    Label(diagnostic_frame,text="System Configuration",font=("Helvetica", 12, "bold"),fg="blue").pack(side=TOP)
    radio=Radiobutton(diagnostic_frame,text='CPU',font=("Helvetica", 12, "bold"),variable=var_radio,value=2,command=sys_config).pack(side=TOP)

#operational frame

oprnl_frame= Frame(root,borderwidth=12,bg="yellow",relief="ridge")
oprnl_frame.pack(side=LEFT)

Button(oprnl_frame,text="Web Search",fg="blue",font=("Helvetica", 12, "bold"),command=web_search).pack(pady=12)
Button(oprnl_frame,text="Search in Data Base",fg="blue",font=("Helvetica", 12, "bold"),command=database_search).pack(pady=12)
Button(oprnl_frame,text="Generate All Images",fg="blue",font=("Helvetica", 12, "bold"),command=gen_all_image).pack(pady=12)
Button(oprnl_frame,text="Search in a Video",fg="blue",font=("Helvetica", 12, "bold"),command=video_search).pack(pady=12)
Button(oprnl_frame,text="Live Streaming",fg="blue",font=("Helvetica", 12, "bold"),command=live_streaming).pack(pady=12)
Button(oprnl_frame,text="Anthropometry",fg="blue",font=("Helvetica", 12, "bold"),command=anthropometry).pack(pady=12)

Button(welcome_frame,text="Click Here to Select Query Image First",fg="green",font=("Helvetica", 12, "bold"),command=select_query_image).pack(pady=10)
Button(welcome_frame,text="Click Here to Select a Folder of Images",fg="orange",font=("Helvetica", 12, "bold"),command=select_query_folder).pack(pady=10)
Button(welcome_frame,text="Reset",fg="red",font=("Helvetica", 12, "bold"),command=reset).pack(pady=10)
#Button(diagnostic_frame,text="Select",fg="blue",font=("Helvetica", 12, "bold"),Command=sys_config).pack()

#print(var.get())

#output frame
op_frame= Frame(root,borderwidth=12,bg="orange",relief="ridge")
op_frame.pack(side=RIGHT)




root.mainloop()


