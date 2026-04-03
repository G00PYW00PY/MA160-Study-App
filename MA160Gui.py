
#Written by Lee Roby - please credit me when using!!
#
import tkinter as tk
from tkinter import messagebox
from ProblemBankMA160 import ProblemBank


class StudyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MA 166 Study App")
        self.root.geometry("600x500")

        #DARK MODE
        self.bg_color = "#1e1e1e"
        self.fg_color = "#ffffff"
        self.button_color = "#2d2d2d"
        self.accent = "#4cc9f0"

        self.root.configure(bg=self.bg_color)

        self.bank = ProblemBank()

        #TITLE
        tk.Label(
            root,
            text="Select Exam",
            font=("Arial", 18, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        ).pack(pady=10)

        #EXAM BUTTONS
        button_frame = tk.Frame(root, bg=self.bg_color)
        button_frame.pack(pady=10)

        exams = ["Exam 1", "Exam 2", "Exam 3", "Final"]

        for exam in exams:
            tk.Button(
                button_frame,
                text=exam,
                width=10,
                bg=self.button_color,
                fg=self.fg_color,
                activebackground=self.accent,
                command=lambda e=exam: self.start_session(e)
            ).pack(side="left", padx=5)

        #PROBLEM DISPLAY
        self.problem_label = tk.Label(
            root,
            text="",
            font=("Arial", 22),
            bg=self.bg_color,
            fg=self.accent
        )
        self.problem_label.pack(pady=30)

        #PROGRESS
        self.progress_label = tk.Label(
            root,
            text="",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.fg_color
        )
        self.progress_label.pack(pady=10)

        #ACTION BUTTONS
        action_frame = tk.Frame(root, bg=self.bg_color)
        action_frame.pack(pady=20)

        tk.Button(
            action_frame,
            text="Solved on my own ✅",
            width=20,
            bg="#2a9d8f",
            fg="white",
            command=self.solved
        ).pack(pady=5)

        tk.Button(
            action_frame,
            text="Needed answer ❌",
            width=20,
            bg="#e76f51",
            fg="white",
            command=self.needs_review
        ).pack(pady=5)

        tk.Button(
            action_frame,
            text="Skip ⏭",
            width=20,
            bg="#555555",
            fg="white",
            command=self.skip
        ).pack(pady=5)

        #FUTURE FEATURE
        # tk.Button(root, text="Show Answer", command=self.show_answer).pack(pady=5)

    #SESSION CONTROL

    def start_session(self, exam_name):
        self.bank.load_exam(exam_name)
        self.next_problem()

    def next_problem(self):
        problem = self.bank.get_next_problem()

        if problem is None:
            self.finish_session()
            return

        section, num = problem
        self.problem_label.config(
            text=f"Section {section}  —  Problem {num}"
        )

        self.update_progress()

    def solved(self):
        self.bank.mark_solved()
        self.next_problem()

    def needs_review(self):
        self.bank.mark_needs_review()
        self.next_problem()

    def skip(self):
        self.bank.skip_problem()
        self.next_problem()

    def update_progress(self):
        remaining = self.bank.problems_left()
        done = self.bank.total_completed()

        self.progress_label.config(
            text=f"Completed: {done}   |   Remaining: {remaining}"
        )

    #GROUPING LOGIC

    def group_by_section(self, problem_list):
        grouped = {}

        for section, prob in problem_list:
            if section not in grouped:
                grouped[section] = []
            grouped[section].append(prob)

        formatted = ""
        for section in sorted(grouped.keys()):
            probs = ", ".join(grouped[section])
            formatted += f"Section {section}: {probs}\n\n"

        return formatted if formatted else "None"

    #END SCREEN

    def finish_session(self):
        mastered = self.group_by_section(self.bank.completed)
        review = self.group_by_section(self.bank.needs_review)

        message = f"""
You finished!

========================
MASTERED:
========================
{mastered}

========================
REVIEW:
========================
{review}
"""

        messagebox.showinfo("Session Complete", message)

        self.problem_label.config(text="All done!")
        self.progress_label.config(text="")


#RUN

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyApp(root)
    root.mainloop()