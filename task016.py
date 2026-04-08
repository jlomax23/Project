import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

class TkCalendar(tk.Frame):
    def __init__(self, master=None, year=None, month=None):
        super().__init__(master)
        self.year = year or datetime.now().year
        self.month = month or datetime.now().month

        self.build_calendar()

    def build_calendar(self):
        # Clear previous widgets
        for widget in self.winfo_children():
            widget.destroy()

        # Navigation frame
        nav_frame = tk.Frame(self)
        nav_frame.grid(row=0, column=0, columnspan=7, pady=5)

        tk.Button(nav_frame, text="<", command=self.prev_month).pack(side="left")

        # Month dropdown
        month_names = list(calendar.month_name)[1:]  # Jan–Dec
        self.month_var = tk.StringVar(value=calendar.month_name[self.month])
        month_box = ttk.Combobox(
            nav_frame,
            textvariable=self.month_var,
            values=month_names,
            state="readonly",
            width=10
        )
        month_box.pack(side="left", padx=5)
        month_box.bind("<<ComboboxSelected>>", self.month_changed)

        # Year dropdown
        years = list(range(1900, 2101))
        self.year_var = tk.IntVar(value=self.year)
        year_box = ttk.Combobox(
            nav_frame,
            textvariable=self.year_var,
            values=years,
            state="readonly",
            width=6
        )
        year_box.pack(side="left", padx=5)
        year_box.bind("<<ComboboxSelected>>", self.year_changed)

        tk.Button(nav_frame, text=">", command=self.next_month).pack(side="left")

        # Weekday labels
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            tk.Label(self, text=day, font=("Arial", 12, "bold")).grid(row=1, column=i)

        # Calendar days
        month_days = calendar.monthcalendar(self.year, self.month)
        for row, week in enumerate(month_days, start=2):
            for col, day in enumerate(week):
                if day == 0:
                    tk.Label(self, text="").grid(row=row, column=col)
                else:
                    tk.Button(
                        self,
                        text=str(day),
                        width=4,
                        command=lambda d=day: self.on_day_selected(d)
                    ).grid(row=row, column=col)

    def month_changed(self, event):
        selected = self.month_var.get()
        self.month = list(calendar.month_name).index(selected)
        self.build_calendar()

    def year_changed(self, event):
        self.year = int(self.year_var.get())
        self.build_calendar()

    def prev_month(self):
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1
        self.build_calendar()

    def next_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1
        self.build_calendar()

    def on_day_selected(self, day):
        print(f"Selected date: {self.year}-{self.month}-{day}")

# Demo
root = tk.Tk()
root.title("Tkinter Calendar with Month & Year Dropdowns")

cal = TkCalendar(root)
cal.pack(padx=20, pady=20)

root.mainloop()