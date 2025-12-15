import tkinter as tk
import json 
import os

# planet class 
class Planet:
    def __init__(self, name, mass, distance, moons):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.moons = moons

#all main information of a planet as a string
    def info(self):
        text  = f"Name: {self.name}\n"
        text += f"Mass: {self.mass}\n"
        text += f"Distance from Sun: {self.distance}\n"
        text += f"Moons: {', '.join(self.moons) if self.moons else 'None'}\n"
        return text

#load JSON data
def load_planet_data(filename):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, filename)

    with open(file_path, "r") as file:
        data = json.load(file)

    planet_objects = {}
    for name, info in data.items():
        planet_objects[name] = Planet(
            name,
            info["mass"],
            info["distance"],
            info["moons"]
        )
    return planet_objects

planets = load_planet_data("planet.json")

def show_planet(name):
    planet = planets[name]
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, planet.info())

root = tk.Tk()

root.geometry("800x800")
root.title("Solar System final assignment")

label = tk.Label(root, text="Final Assignment Solar System", font=('Times New Roman', 35))
label.pack (padx=20, pady=20)

textbox = tk.Text (root, height=5, font=('Times New Roman', 25))
textbox.pack()


#box for questions

question_entry = tk.Entry(root, font=("Times New Roman", 20))
question_entry.pack(pady=10)

ask_button = tk.Button(root, text="Ask a Question!", font=("Times New Roman", 20),
                       command=lambda: answer_question(question_entry.get()))
ask_button.pack(pady=10)

def answer_question(question):
    q = question.strip().lower() #https://realpython.com/python-strip/#:~:text=strip()%20With%20Other%20String%20Methods,-In%20real%2Dworld&text=In%20this%20example%2C%20.,converting%20text%20to%20lowercase%2C%20and%20.


    if not q:
        textbox.delete ("1.0", tk.END)
        textbox.insert(tk.END, "Please ask a question about the solar system.")
        return

#answer questions about pluto
    if "pluto" in q:
        textbox.delete(1.0, tk.END)
        textbox.insert(
            tk.END,
            "Pluto is not in the list of planets because it is classified as a dwarf planet."
        )
        return
    
 #find all mentioned planets   
    found_planets = []
    for planet_name, planet_obj in planets.items():
        if planet_name.lower() in q:
            found_planets.append(planet_obj)
            

    if not found_planets:
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, "I could not find a planet in your question.")
        return
    
    answer = []
    
 # detect what is being asked
    for planet in found_planets: 
        if "moon" in q or "moons" in q:
            num_moons =len(planet.moons)
            moons_text = ",".join(planet.moons) if planet.moons else "None"
            if num_moons == 1:
                answer.append(f"{planet.name} has 1 moon.\nIt is: {moons_text}")
            elif num_moons == 0:
                answer.append(f"{planet.name} has no moons.")
            else: 
                answer.append(f"{planet.name} has {len(planet.moons)} moons.\nThey are: {moons_text}")
        elif "distance" in q or "far" in q:
            answer.append (f"{planet.name} is {planet.distance} from the Sun.")
        elif "mass" in q or "massive" in q or "heavy" in q or "big" in q:
            answer.append (f"The mass of {planet.name} is {planet.mass}.")
        elif "everything" in q or "all" in q:
            answer.append (planet.info())
        else:
            answer.append (f"I understood the planet but not what information you want.")

    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END,"\n\n".join(answer))

#buttons 
#code inspired by "Tkinter Beginner Course - Python GUI Development" on YT
buttonframe = tk.Frame(root)
buttonframe.pack(pady=20) 

#make 3x3 buttons of the planets
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)
buttonframe.columnconfigure(4, weight=1)
buttonframe.columnconfigure(5, weight=1)
buttonframe.columnconfigure(6, weight=1)
buttonframe.columnconfigure(7, weight=1)

btn1 =tk.Button(buttonframe, text="Mercury", font=('Times New Roman', 18),command=lambda: show_planet("Mercury")) #https://www.tutorialspoint.com/tkinter-button-commands-with-lambda-in-python this helped with linking the buttons to the planets
btn1.grid(row=0,column=0, sticky=tk.W+tk.E)

btn2 =tk.Button(buttonframe, text="Venus", font=('Times New Roman', 18),command=lambda: show_planet("Venus"))
btn2.grid(row=0,column=1, sticky=tk.W+tk.E)


btn3 =tk.Button(buttonframe, text="Earth", font=('Times New Roman', 18),command=lambda: show_planet("Earth"))
btn3.grid(row=0,column=2, sticky=tk.W+tk.E)


btn4 =tk.Button(buttonframe, text="Mars", font=('Times New Roman', 18),command=lambda: show_planet("Mars"))
btn4.grid(row=1,column=0, sticky=tk.W+tk.E)


btn5 =tk.Button(buttonframe, text="Jupiter", font=('Times New Roman', 18),command=lambda: show_planet("Jupiter"))
btn5.grid(row=1,column=1, sticky=tk.W+tk.E)


btn6 =tk.Button(buttonframe, text="Saturn", font=('Times New Roman', 18),command=lambda: show_planet("Saturn"))
btn6.grid(row=1,column=2, sticky=tk.W+tk.E)


btn7 =tk.Button(buttonframe, text="Uranus", font=('Times New Roman', 18),command=lambda: show_planet("Uranus"))
btn7.grid(row=2,column=0, sticky=tk.W+tk.E)


btn8 =tk.Button(buttonframe, text="Neptune", font=('Times New Roman', 18),command=lambda: show_planet("Neptune"))
btn8.grid(row=2,column=1, sticky=tk.W+tk.E)


root.mainloop()

