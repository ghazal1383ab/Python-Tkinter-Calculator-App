#programming a calculater
import tkinter

#making the buttens
butten_value=[
    ["AC","+/-","%","÷"],
    ["1","2","3","×"],
    ["4","5","6","-"],
    ["7","8","9","+"],
    [".","0","√","="]
]

top_symbols=["AC","+/-","%"]
right_symbols=["÷","×","-","+","="]

raw_number=len(butten_value)
calum_number=len(butten_value[0])


# diffrent colors for using in the project
dark_blue="#212f3d"
gray="#717d7e"
black="#000000"
numbers_gray="#909497"
white="#f4f6f7"
grayer="#566573"
back_color="#212121"

#making the window
window=tkinter.Tk()
window.title("calculator")             
window.resizable(False, False)
frame=tkinter.Frame(window)
label = tkinter.Label(
    frame,
    text="0",
    font=("Arial", 40),
    background=back_color,
    foreground=numbers_gray,
    anchor="w",
    width=calum_number
)
label.grid(row=0,column=0, columnspan=calum_number,sticky="we")

#giving value to the bottens
for raw in range(raw_number):
    for colum in range(calum_number):
        value=butten_value[raw][colum]
        butten=tkinter.Button(frame,text=value,font=("Arial", 25), width=calum_number-1 ,
                              height=1 , command=lambda value=value : butten_clicked(value))
        butten.grid(row=raw+1, column=colum)
        
        if value in right_symbols:
            butten.config(foreground=white, background=dark_blue)
        elif value in top_symbols:
            butten.config(foreground=white, background=gray)
        else:
            butten.config(foreground=white, background=grayer)
frame.pack()

A=0
operater=None
B=None
def clear_all():
    global A, B, operater
    A = 0
    B = None
    operater = None


def clear_zeros(num):
    if num%1==0:
        num = int (num)
    return str(num)
    

#giving the action of pressing 
def butten_clicked(value):
    global right_symbols,top_symbols,label,A, B , operater
    if value in right_symbols:
        if value=="=":
            if A is not None and operater is not None:
                B=label["text"]
                num1=float(A)
                num2=float(B)
                
                if operater=="+":
                    label["text"]=clear_zeros(num1+num2)
                if operater=="-":
                    label["text"]=clear_zeros(num1-num2)
                if operater=="÷" :
                    label["text"]=clear_zeros(num1/num2)   
                if operater=="×":
                    label["text"]=clear_zeros(num1*num2)
                clear_all()        
                    
        if value in "÷×-+":
            if operater==None:
                A=label["text"]
                label["text"]="0"
                B="0"
            operater=value
            
    if value in top_symbols:
        if value =="AC":
             A=0
             operater=None
             B=None
             label["text"]="0"
        if value=="+/-":
            result=float(label["text"])* -1
            label["text"]=clear_zeros(result)
        if value=="%":
            result=float(label["text"]) /100
            label["text"]=clear_zeros(result)
    else:
        if value ==".":
            if value not in label["text"]:
                label['text']+=value
        elif value in "0123456789":
            if label["text"]=="0":
                label["text"]=value
            else:
                label["text"]+= value       
    
    
    
    
#centering the window on the screen 
window.update_idletasks()  # آپدیت ابعاد داخلی ویجت‌ها
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"+{x}+{y}")





window.mainloop() 

