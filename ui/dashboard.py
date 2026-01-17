import tkinter as tk
from core.orchestrator import Orchestrator
from core.memory import Memory

class Dashboard:
    def __init__(self):
        self.memory = Memory()
        self.orchestrator = Orchestrator(self.memory)

        self.root = tk.Tk()
        self.root.title("Synthetic Intelligence Platform")

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()

        self.button = tk.Button(
            self.root,
            text="Create Full Course",
            command=self.run
        )
        self.button.pack()

        self.output = tk.Text(self.root, height=20, width=80)
        self.output.pack()

        self.root.mainloop()

    def run(self):
        domain = self.entry.get()
        result = self.orchestrator.create_course(domain)
        self.output.insert(tk.END, str(result))
