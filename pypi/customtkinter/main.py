import customtkinter

def button_callback():
    print("Oi esther")

app = customtkinter.CTk()
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="Oi esther", command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()