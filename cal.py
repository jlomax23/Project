import tkinter as tk
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

        # Month and year label
        header = tk.Label(self, text=f"{calendar.month_name[self.month]} {self.year}",
                          font=("Arial", 16, "bold"))
        header.grid(row=0, column=0, columnspan=7, pady=10)

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
                    tk.Button(self, text=str(day), width=4).grid(row=row, column=col)

# Demo
root = tk.Tk()
root.title("Pure Tkinter Calendar")

cal = TkCalendar(root)
cal.pack(padx=20, pady=20)

root.mainloop()

