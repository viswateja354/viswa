# ==========================================================
# Smart College Helpdesk Bot
# Modern UI using customtkinter
# ==========================================================
# Required Library:
# pip install customtkinter
# ==========================================================

import customtkinter as ctk
from datetime import datetime

# ==========================================================
# APPLICATION CONFIGURATION
# ==========================================================

ctk.set_appearance_mode("dark")          # Dark mode
ctk.set_default_color_theme("dark-blue")  # Modern blue theme


# ==========================================================
# MAIN APPLICATION CLASS
# ==========================================================

class SmartCollegeHelpdeskBot(ctk.CTk):

    def __init__(self):
        super().__init__()

        # --------------------------------------------------
        # WINDOW SETTINGS
        # --------------------------------------------------
        self.title("Smart College Helpdesk Bot")
        self.geometry("1280x720")
        self.minsize(1000, 650)

        # --------------------------------------------------
        # COLOR PALETTE
        # --------------------------------------------------
        self.colors = {
    "bg": "#0a0a0a",          # Main background - Pure black
    "sidebar": "#111111",    # Sidebar - Dark gray
    "chat_bg": "#1a1a1a",    # Chat area background
    "bot_bubble": "#2a2a2a", # Bot message bubble
    "user_bubble": "#404040",# User message bubble
    "hover": "#555555",      # Button hover effect
    "text": "#f5f5f5",       # Main white text
    "subtext": "#b0b0b0",    # Light gray text
    "input": "#151515"       # Input field background
}   

        self.configure(fg_color=self.colors["bg"])

        # --------------------------------------------------
        # GRID LAYOUT
        # --------------------------------------------------
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --------------------------------------------------
        # CREATE UI SECTIONS
        # --------------------------------------------------
        self.create_sidebar()
        self.create_main_chat_area()
        self.create_input_bar()

        # --------------------------------------------------
        # INITIAL BOT MESSAGE
        # --------------------------------------------------
        self.add_bot_message(
            "Hello! 👋\n\n"
            "I'm your Smart College Helpdesk Bot.\n"
            "Ask me about:\n"
            "• Timetables\n"
            "• Faculty Information\n"
            "• Exam Dates\n"
            "• Attendance\n"
            "• College Events"
        )

    # ======================================================
    # SIDEBAR
    # ======================================================

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=260,
            corner_radius=0,
            fg_color=self.colors["sidebar"]
        )

        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.sidebar.grid_propagate(False)

        # --------------------------------------------------
        # SIDEBAR TITLE
        # --------------------------------------------------
        logo = ctk.CTkLabel(
            self.sidebar,
            text="🎓",
            font=("Segoe UI Emoji", 42)
        )
        logo.pack(pady=(30, 10))

        title = ctk.CTkLabel(
            self.sidebar,
            text="Smart College\nHelpdesk",
            font=("Segoe UI", 24, "bold"),
            text_color=self.colors["text"],
            justify="center"
        )
        title.pack(pady=(0, 30))

        # --------------------------------------------------
        # NAVIGATION BUTTONS
        # --------------------------------------------------
        buttons = [
            ("📅 Timetables", "Show today's timetable"),
            ("👨‍🏫 Faculty", "Faculty information"),
            ("📝 Exam Dates", "Upcoming exam dates"),
            ("📋 Attendance", "Check attendance"),
            ("🎉 Events", "Upcoming college events")
        ]

        for text, query in buttons:

            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                height=48,
                corner_radius=12,
                fg_color="#1e293b",
                hover_color=self.colors["hover"],
                font=("Segoe UI", 15),
                anchor="w",
                command=lambda q=query: self.quick_access(q)
            )

            btn.pack(fill="x", padx=20, pady=10)

        # --------------------------------------------------
        # FOOTER
        # --------------------------------------------------
        footer = ctk.CTkLabel(
            self.sidebar,
            text="Modern College Assistant\nv1.0",
            text_color=self.colors["subtext"],
            font=("Segoe UI", 12)
        )

        footer.pack(side="bottom", pady=25)

    # ======================================================
    # MAIN CHAT AREA
    # ======================================================

    def create_main_chat_area(self):

        # Main container
        self.main_frame = ctk.CTkFrame(
            self,
            fg_color=self.colors["chat_bg"],
            corner_radius=0
        )

        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # --------------------------------------------------
        # SCROLLABLE CHAT FRAME
        # --------------------------------------------------
        self.chat_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color=self.colors["chat_bg"],
            corner_radius=0
        )

        self.chat_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(20, 10)
        )

        self.chat_frame.grid_columnconfigure(0, weight=1)

    # ======================================================
    # INPUT BAR
    # ======================================================

    def create_input_bar(self):

        input_container = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.colors["chat_bg"],
            corner_radius=0,
            height=80
        )

        input_container.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 20)
        )

        input_container.grid_columnconfigure(0, weight=1)

        # --------------------------------------------------
        # TEXT ENTRY
        # --------------------------------------------------
        self.user_input = ctk.CTkEntry(
            input_container,
            height=50,
            corner_radius=14,
            placeholder_text="Ask something about your college...",
            font=("Segoe UI", 15),
            fg_color=self.colors["input"],
            border_color="#334155",
            text_color=self.colors["text"]
        )

        self.user_input.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 12)
        )

        # ENTER KEY SUPPORT
        self.user_input.bind("<Return>", self.send_message)

        # --------------------------------------------------
        # SEND BUTTON
        # --------------------------------------------------
        send_btn = ctk.CTkButton(
            input_container,
            text="➤",
            width=55,
            height=50,
            corner_radius=14,
            font=("Segoe UI", 18, "bold"),
            fg_color=self.colors["user_bubble"],
            hover_color=self.colors["hover"],
            command=self.send_message
        )

        send_btn.grid(row=0, column=1)

    # ======================================================
    # CHAT MESSAGE METHODS
    # ======================================================

    def add_user_message(self, message):

        container = ctk.CTkFrame(
            self.chat_frame,
            fg_color="transparent"
        )

        container.pack(fill="x", pady=10, padx=10)

        bubble = ctk.CTkLabel(
            container,
            text=message,
            wraplength=500,
            justify="left",
            fg_color=self.colors["user_bubble"],
            text_color="white",
            corner_radius=16,
            padx=18,
            pady=12,
            font=("Segoe UI", 14)
        )

        bubble.pack(anchor="e", padx=10)

    def add_bot_message(self, message):

        container = ctk.CTkFrame(
            self.chat_frame,
            fg_color="transparent"
        )

        container.pack(fill="x", pady=10, padx=10)

        bubble = ctk.CTkLabel(
            container,
            text=message,
            wraplength=550,
            justify="left",
            fg_color=self.colors["bot_bubble"],
            text_color=self.colors["text"],
            corner_radius=16,
            padx=18,
            pady=12,
            font=("Segoe UI", 14)
        )

        bubble.pack(anchor="w", padx=10)

    # ======================================================
    # QUICK ACCESS BUTTON HANDLER
    # ======================================================

    def quick_access(self, query):

        self.add_user_message(query)

        response = self.generate_response(query)

        self.after(300, lambda: self.add_bot_message(response))

    # ======================================================
    # SEND MESSAGE HANDLER
    # ======================================================

    def send_message(self, event=None):

        user_text = self.user_input.get().strip()

        if not user_text:
            return

        # Clear input field
        self.user_input.delete(0, "end")

        # Display user message
        self.add_user_message(user_text)

        # Generate bot response
        response = self.generate_response(user_text)

        # Simulate response delay
        self.after(400, lambda: self.add_bot_message(response))

    # ======================================================
    # MOCK CHATBOT LOGIC
    # ======================================================

    def generate_response(self, query):

        query = query.lower()

        # --------------------------------------------------
        # TIMETABLE
        # --------------------------------------------------
        if "timetable" in query or "class" in query:

            return (
                "📅 Today's Timetable:\n\n"
                "09:00 AM - Data Structures\n"
                "10:30 AM - Database Systems\n"
                "12:00 PM - Break\n"
                "01:00 PM - Artificial Intelligence\n"
                "03:00 PM - Software Engineering Lab"
            )

        # --------------------------------------------------
        # FACULTY
        # --------------------------------------------------
        elif "faculty" in query or "teacher" in query or "professor" in query:

            return (
                "👨‍🏫 Faculty Information:\n\n"
                "• Dr. Ananya Rao - AI Department\n"
                "• Prof. Vikram Mehta - Databases\n"
                "• Dr. Sneha Iyer - Software Engineering\n"
                "• Prof. Arjun Patel - Cybersecurity"
            )

        # --------------------------------------------------
        # EXAMS
        # --------------------------------------------------
        elif "exam" in query or "test" in query:

            return (
                "📝 Upcoming Exam Dates:\n\n"
                "• DBMS Midterm - June 12\n"
                "• AI Internal Assessment - June 18\n"
                "• Software Engineering Lab Exam - June 24\n"
                "• Semester Finals Begin - July 05"
            )

        # --------------------------------------------------
        # ATTENDANCE
        # --------------------------------------------------
        elif "attendance" in query:

            return (
                "📋 Attendance Summary:\n\n"
                "• Data Structures: 91%\n"
                "• DBMS: 88%\n"
                "• Artificial Intelligence: 94%\n"
                "• Software Engineering: 86%\n\n"
                "Overall Attendance: 89.75%"
            )

        # --------------------------------------------------
        # EVENTS
        # --------------------------------------------------
        elif "event" in query or "fest" in query:

            return (
                "🎉 Upcoming College Events:\n\n"
                "• TechFest 2026 - June 15\n"
                "• Hackathon Weekend - June 22\n"
                "• Cultural Night - July 02\n"
                "• AI Workshop Series - July 10"
            )

        # --------------------------------------------------
        # GREETINGS
        # --------------------------------------------------
        elif any(word in query for word in ["hi", "hello", "hey"]):

            return (
                "Hello! 👋\n"
                "How can I assist you today?"
            )

        # --------------------------------------------------
        # DATE/TIME
        # --------------------------------------------------
        elif "time" in query or "date" in query:

            now = datetime.now()

            return (
                f"🕒 Current Date & Time:\n\n"
                f"{now.strftime('%A, %d %B %Y')}\n"
                f"{now.strftime('%I:%M %p')}"
            )

        # --------------------------------------------------
        # DEFAULT RESPONSE
        # --------------------------------------------------
        else:

            return (
                "I'm here to help with college-related information.\n\n"
                "Try asking about:\n"
                "• Timetables\n"
                "• Faculty\n"
                "• Exam Dates\n"
                "• Attendance\n"
                "• Events"
            )


# ==========================================================
# RUN APPLICATION
# ==========================================================

if __name__ == "__main__":

    app = SmartCollegeHelpdeskBot()
    app.mainloop()