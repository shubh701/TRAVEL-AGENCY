import tkinter as tk
from tkinter import messagebox
import mysql.connector

# -------- DB CONNECTION --------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345@Shubh",
    database="travel_db"
)
cursor = conn.cursor()

# -------- THEME --------
BG        = "#0D1117"
CARD      = "#161B22"
ACCENT    = "#2563EB"
ACCENT2   = "#38BDF8"
TEXT      = "#F0F6FC"
SUBTEXT   = "#8B949E"
SUCCESS   = "#22C55E"
DANGER    = "#EF4444"
BORDER    = "#30363D"
FONT_H    = ("Georgia", 28, "bold")
FONT_SUB  = ("Georgia", 13)
FONT_BODY = ("Courier", 11)
FONT_BTN  = ("Georgia", 12, "bold")
FONT_LBL  = ("Courier", 10)

# -------- HELPERS --------
def styled_entry(parent, show=None, width=30):
    frame = tk.Frame(parent, bg=BORDER, padx=1, pady=1)
    e = tk.Entry(frame, bg="#1C2128", fg=TEXT, insertbackground=TEXT,
                 font=FONT_BODY, relief="flat", width=width,
                 highlightthickness=0, bd=4)
    if show:
        e.config(show=show)
    e.pack()
    return frame, e

def accent_button(parent, text, cmd, color=ACCENT, width=20):
    btn = tk.Button(parent, text=text, command=cmd,
                    bg=color, fg="white", font=FONT_BTN,
                    relief="flat", cursor="hand2", width=width,
                    activebackground=ACCENT2, activeforeground="white",
                    padx=10, pady=8)
    btn.bind("<Enter>", lambda e: btn.config(bg=ACCENT2))
    btn.bind("<Leave>", lambda e: btn.config(bg=color))
    return btn

def clear_root():
    for w in root.winfo_children():
        w.destroy()

def get_user_name(user_id):
    cursor.execute("SELECT name FROM Users WHERE user_id=%s", (user_id,))
    r = cursor.fetchone()
    return r[0] if r else "User"

# ============================================================
# SCREEN 1 — WELCOME / SPLASH
# ============================================================
def show_welcome():
    clear_root()
    root.configure(bg=BG)

    # ---- decorative canvas background ----
    canvas = tk.Canvas(root, width=520, height=600, bg=BG, highlightthickness=0)
    canvas.place(x=0, y=0)
    for cx, cy, r, col in [(60,60,55,"#1E3A5F"),(460,90,75,"#0F2A4A"),
                            (260,560,95,"#162032"),(40,510,45,"#1A2E48"),
                            (480,480,60,"#122030")]:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=col, outline="")

    # ---- hero emoji + title ----
    title_frame = tk.Frame(root, bg=BG)
    title_frame.place(relx=0.5, rely=0.13, anchor="center")

    tk.Label(title_frame, text="✈", font=("Arial", 52), bg=BG, fg=ACCENT2).pack()
    tk.Label(title_frame, text="TravelEase", font=("Georgia", 38, "bold"),
             bg=BG, fg=TEXT).pack()
    tk.Label(title_frame, text="Your journey begins here", font=("Georgia", 13, "italic"),
             bg=BG, fg=SUBTEXT).pack(pady=5)

    # ---- accent divider ----
    div = tk.Frame(root, bg=ACCENT, height=2, width=200)
    div.place(relx=0.5, rely=0.34, anchor="center")

    # ---- stats bar ----
    stats = tk.Frame(root, bg=CARD, padx=10, pady=14)
    stats.place(relx=0.5, rely=0.44, anchor="center")
    for icon, val, label in [("🌍", "150+", "Destinations"),
                              ("🏨", "500+", "Hotels"),
                              ("✈", "80+", "Airlines")]:
        col = tk.Frame(stats, bg=CARD, padx=22)
        col.pack(side="left")
        tk.Label(col, text=icon, font=("Arial", 22), bg=CARD).pack()
        tk.Label(col, text=val, font=("Georgia", 16, "bold"), bg=CARD, fg=ACCENT2).pack()
        tk.Label(col, text=label, font=("Courier", 9), bg=CARD, fg=SUBTEXT).pack()

    # ---- main buttons ----
    btn_frame = tk.Frame(root, bg=BG)
    btn_frame.place(relx=0.5, rely=0.67, anchor="center")

    accent_button(btn_frame, "🔐   LOGIN", show_login, color=ACCENT, width=24).pack(pady=8)
    accent_button(btn_frame, "📝   REGISTER", show_register, color="#16A34A", width=24).pack(pady=8)

    tk.Label(root, text="© 2025 TravelEase  •  Made with ♥",
             bg=BG, fg=BORDER, font=("Courier", 9)).place(relx=0.5, rely=0.96, anchor="center")

# ============================================================
# SCREEN 2 — LOGIN
# ============================================================
def show_login():
    clear_root()
    root.configure(bg=BG)

    tk.Button(root, text="← Back", bg=BG, fg=SUBTEXT, font=FONT_LBL,
              relief="flat", cursor="hand2", command=show_welcome).place(x=15, y=15)

    card = tk.Frame(root, bg=CARD, padx=45, pady=35,
                    highlightbackground=BORDER, highlightthickness=1)
    card.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(card, text="✈", font=("Arial", 36), bg=CARD, fg=ACCENT2).pack()
    tk.Label(card, text="Welcome Back", font=("Georgia", 22, "bold"), bg=CARD, fg=TEXT).pack(pady=4)
    tk.Label(card, text="Sign in to your account", font=FONT_SUB, bg=CARD, fg=SUBTEXT).pack(pady=(0, 20))

    tk.Label(card, text="EMAIL ADDRESS", bg=CARD, fg=SUBTEXT, font=FONT_LBL).pack(anchor="w")
    ef, email_e = styled_entry(card)
    ef.pack(fill="x", pady=(2, 12))

    tk.Label(card, text="PASSWORD", bg=CARD, fg=SUBTEXT, font=FONT_LBL).pack(anchor="w")
    pf, pass_e = styled_entry(card, show="*")
    pf.pack(fill="x", pady=(2, 20))

    def do_login():
        cursor.execute("SELECT * FROM Users WHERE email=%s AND password=%s",
                       (email_e.get(), pass_e.get()))
        user = cursor.fetchone()
        if user:
            show_dashboard(user[0], user[1])
        else:
            messagebox.showerror("Login Failed", "Invalid email or password")

    accent_button(card, "SIGN IN  →", do_login, width=28).pack(pady=4)

    tk.Label(card, text="Don't have an account?", bg=CARD, fg=SUBTEXT, font=FONT_LBL).pack(pady=(14, 2))
    tk.Button(card, text="Create Account", bg=CARD, fg=ACCENT2, font=FONT_LBL,
              relief="flat", cursor="hand2", command=show_register).pack()

# ============================================================
# SCREEN 3 — REGISTER
# ============================================================
def show_register():
    clear_root()
    root.configure(bg=BG)

    tk.Button(root, text="← Back", bg=BG, fg=SUBTEXT, font=FONT_LBL,
              relief="flat", cursor="hand2", command=show_welcome).place(x=15, y=15)

    card = tk.Frame(root, bg=CARD, padx=45, pady=35,
                    highlightbackground=BORDER, highlightthickness=1)
    card.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(card, text="🌍", font=("Arial", 36), bg=CARD, fg=ACCENT2).pack()
    tk.Label(card, text="Create Account", font=("Georgia", 22, "bold"), bg=CARD, fg=TEXT).pack(pady=4)
    tk.Label(card, text="Join TravelEase today", font=FONT_SUB, bg=CARD, fg=SUBTEXT).pack(pady=(0, 20))

    tk.Label(card, text="FULL NAME", bg=CARD, fg=SUBTEXT, font=FONT_LBL).pack(anchor="w")
    nf, name_e = styled_entry(card)
    nf.pack(fill="x", pady=(2, 12))

    tk.Label(card, text="EMAIL ADDRESS", bg=CARD, fg=SUBTEXT, font=FONT_LBL).pack(anchor="w")
    ef, email_e = styled_entry(card)
    ef.pack(fill="x", pady=(2, 12))

    tk.Label(card, text="PASSWORD", bg=CARD, fg=SUBTEXT, font=FONT_LBL).pack(anchor="w")
    pf, pass_e = styled_entry(card, show="*")
    pf.pack(fill="x", pady=(2, 20))

    def do_register():
        try:
            cursor.execute("INSERT INTO Users (name,email,password) VALUES (%s,%s,%s)",
                           (name_e.get(), email_e.get(), pass_e.get()))
            conn.commit()
            messagebox.showinfo("Success", "Account created! Please login.")
            show_login()
        except Exception as ex:
            messagebox.showerror("Error", "Email already exists or DB error:\n" + str(ex))

    accent_button(card, "CREATE ACCOUNT  →", do_register, color="#16A34A", width=28).pack(pady=4)

    tk.Label(card, text="Already have an account?", bg=CARD, fg=SUBTEXT, font=FONT_LBL).pack(pady=(14, 2))
    tk.Button(card, text="Sign In", bg=CARD, fg=ACCENT2, font=FONT_LBL,
              relief="flat", cursor="hand2", command=show_login).pack()

# ============================================================
# SCREEN 4 — DASHBOARD
# ============================================================
def show_dashboard(user_id, user_name):
    clear_root()
    root.configure(bg=BG)

    # ---- top bar ----
    topbar = tk.Frame(root, bg=CARD, height=60,
                      highlightbackground=BORDER, highlightthickness=1)
    topbar.pack(fill="x")
    topbar.pack_propagate(False)

    tk.Label(topbar, text="✈ TravelEase", font=("Georgia", 15, "bold"),
             bg=CARD, fg=ACCENT2).pack(side="left", padx=20, pady=15)
    tk.Button(topbar, text="Logout", bg=DANGER, fg="white", font=FONT_LBL,
              relief="flat", cursor="hand2", command=show_welcome,
              padx=8, pady=4).pack(side="right", padx=15, pady=15)
    tk.Label(topbar, text=f"👤  {user_name}", font=FONT_BODY,
             bg=CARD, fg=TEXT).pack(side="right", pady=15)

    # ---- greeting ----
    greet = tk.Frame(root, bg=BG, pady=20)
    greet.pack(fill="x", padx=30)
    tk.Label(greet, text=f"Hello, {user_name} 👋", font=("Georgia", 20, "bold"),
             bg=BG, fg=TEXT).pack(anchor="w")
    tk.Label(greet, text="What would you like to do today?", font=FONT_SUB,
             bg=BG, fg=SUBTEXT).pack(anchor="w")

    # ---- action cards ----
    cards_frame = tk.Frame(root, bg=BG)
    cards_frame.pack(pady=10, padx=30, fill="x")

    def action_card(parent, emoji, title, subtitle, cmd, col=ACCENT):
        card = tk.Frame(parent, bg=CARD, padx=18, pady=18,
                        highlightbackground=BORDER, highlightthickness=1, cursor="hand2")
        card.pack(side="left", expand=True, fill="both", padx=6)

        tk.Label(card, text=emoji, font=("Arial", 30), bg=CARD).pack()
        tk.Label(card, text=title, font=("Georgia", 13, "bold"), bg=CARD, fg=TEXT).pack(pady=4)
        tk.Label(card, text=subtitle, font=FONT_LBL, bg=CARD, fg=SUBTEXT,
                 wraplength=125, justify="center").pack()

        btn = tk.Button(card, text="Open  →", command=cmd,
                        bg=col, fg="white", font=FONT_LBL, relief="flat",
                        cursor="hand2", padx=10, pady=5)
        btn.pack(pady=(10, 0))
        btn.bind("<Enter>", lambda e: btn.config(bg=ACCENT2))
        btn.bind("<Leave>", lambda e: btn.config(bg=col))
        card.bind("<Enter>", lambda e: card.config(bg="#1E2530"))
        card.bind("<Leave>", lambda e: card.config(bg=CARD))

    action_card(cards_frame, "✈️", "Book Flight",
                "Search & book flights worldwide",
                lambda: show_flights(user_id))
    action_card(cards_frame, "🏨", "Book Hotel",
                "Find perfect stays at great prices",
                lambda: show_hotels(user_id), col="#7C3AED")
    action_card(cards_frame, "📋", "My Bookings",
                "View all your trip details",
                lambda: show_my_bookings(user_id), col="#059669")

    # ---- quick tips ----
    tips = tk.Frame(root, bg=CARD, padx=20, pady=16,
                    highlightbackground=BORDER, highlightthickness=1)
    tips.pack(padx=30, pady=20, fill="x")
    tk.Label(tips, text="💡  QUICK TIPS", font=FONT_LBL, bg=CARD, fg=ACCENT2).pack(anchor="w")
    for tip in ["Book early for the best flight prices",
                "Check hotel check-in / check-out times carefully",
                "Keep your booking ID for future reference"]:
        tk.Label(tips, text=f"  •  {tip}", font=FONT_LBL, bg=CARD, fg=SUBTEXT).pack(anchor="w")

# ============================================================
# SCREEN 5 — FLIGHTS
# ============================================================
def show_flights(user_id):
    clear_root()
    root.configure(bg=BG)

    topbar = tk.Frame(root, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
    topbar.pack(fill="x")
    tk.Button(topbar, text="← Back", bg=CARD, fg=SUBTEXT, font=FONT_LBL, relief="flat",
              cursor="hand2",
              command=lambda: show_dashboard(user_id, get_user_name(user_id))).pack(side="left", padx=10, pady=12)
    tk.Label(topbar, text="✈  Book a Flight", font=("Georgia", 15, "bold"),
             bg=CARD, fg=TEXT).pack(side="left", pady=12)

    cursor.execute("SELECT * FROM Flights")
    flights = cursor.fetchall()

    container = tk.Frame(root, bg=BG)
    container.pack(fill="both", expand=True, padx=20, pady=15)
    tk.Label(container, text="Available Flights", font=("Georgia", 17, "bold"),
             bg=BG, fg=TEXT).pack(anchor="w", pady=(0, 10))

    canvas2 = tk.Canvas(container, bg=BG, highlightthickness=0)
    scroll = tk.Scrollbar(container, orient="vertical", command=canvas2.yview)
    inner = tk.Frame(canvas2, bg=BG)
    inner.bind("<Configure>", lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))
    canvas2.create_window((0, 0), window=inner, anchor="nw")
    canvas2.configure(yscrollcommand=scroll.set)
    canvas2.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    if not flights:
        tk.Label(inner, text="No flights found in database.\nAdd flights via MySQL first.",
                 font=FONT_SUB, bg=BG, fg=SUBTEXT, justify="center").pack(pady=50)
        return

    for f in flights:
        fid, airline, src, dst, price = f
        row = tk.Frame(inner, bg=CARD, padx=16, pady=12,
                       highlightbackground=BORDER, highlightthickness=1)
        row.pack(fill="x", pady=5)

        left = tk.Frame(row, bg=CARD)
        left.pack(side="left", expand=True, fill="x")
        tk.Label(left, text=f"✈  {airline}", font=("Georgia", 13, "bold"),
                 bg=CARD, fg=TEXT).pack(anchor="w")
        tk.Label(left, text=f"{src}  →  {dst}", font=FONT_BODY, bg=CARD, fg=ACCENT2).pack(anchor="w")
        tk.Label(left, text=f"Flight ID: {fid}", font=FONT_LBL, bg=CARD, fg=SUBTEXT).pack(anchor="w")

        right = tk.Frame(row, bg=CARD)
        right.pack(side="right")
        tk.Label(right, text=f"₹{price:,.0f}", font=("Georgia", 16, "bold"),
                 bg=CARD, fg=SUCCESS).pack()

        def book_this(fid=fid, airline=airline, src=src, dst=dst, price=price):
            confirm_flight(user_id, fid, airline, src, dst, price)

        b = tk.Button(right, text="Book →", command=book_this,
                      bg=ACCENT, fg="white", font=FONT_LBL, relief="flat",
                      cursor="hand2", padx=8, pady=4)
        b.bind("<Enter>", lambda e, btn=b: btn.config(bg=ACCENT2))
        b.bind("<Leave>", lambda e, btn=b: btn.config(bg=ACCENT))
        b.pack(pady=(6, 0))


def confirm_flight(user_id, flight_id, airline, src, dst, price):
    win = tk.Toplevel(root)
    win.title("Confirm Booking")
    win.geometry("360x300")
    win.configure(bg=CARD)
    win.grab_set()

    tk.Label(win, text="Confirm Flight Booking", font=("Georgia", 16, "bold"),
             bg=CARD, fg=TEXT).pack(pady=20)
    for label, val in [("Airline", airline), ("Route", f"{src} → {dst}"),
                       ("Price", f"₹{price:,.0f}")]:
        row = tk.Frame(win, bg=CARD)
        row.pack(fill="x", padx=30, pady=4)
        tk.Label(row, text=label + ":", font=FONT_LBL, bg=CARD, fg=SUBTEXT,
                 width=10, anchor="w").pack(side="left")
        tk.Label(row, text=val, font=FONT_BODY, bg=CARD, fg=TEXT).pack(side="left")

    def confirm():
        cursor.execute("INSERT INTO Bookings (user_id, booking_date) VALUES (%s, NOW())", (user_id,))
        conn.commit()
        bid = cursor.lastrowid
        cursor.execute("INSERT INTO Flight_Bookings (booking_id, flight_id) VALUES (%s,%s)",
                       (bid, flight_id))
        conn.commit()
        win.destroy()
        messagebox.showinfo("Booked! ✓", f"Flight booked successfully!\nBooking ID: {bid}")

    btn_row = tk.Frame(win, bg=CARD)
    btn_row.pack(pady=20)
    accent_button(btn_row, "Confirm ✓", confirm, color=SUCCESS, width=12).pack(side="left", padx=8)
    accent_button(btn_row, "Cancel", win.destroy, color=DANGER, width=12).pack(side="left", padx=8)

# ============================================================
# SCREEN 6 — HOTELS
# ============================================================
def show_hotels(user_id):
    clear_root()
    root.configure(bg=BG)

    topbar = tk.Frame(root, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
    topbar.pack(fill="x")
    tk.Button(topbar, text="← Back", bg=CARD, fg=SUBTEXT, font=FONT_LBL, relief="flat",
              cursor="hand2",
              command=lambda: show_dashboard(user_id, get_user_name(user_id))).pack(side="left", padx=10, pady=12)
    tk.Label(topbar, text="🏨  Book a Hotel", font=("Georgia", 15, "bold"),
             bg=CARD, fg=TEXT).pack(side="left", pady=12)

    cursor.execute("SELECT * FROM Hotels")
    hotels = cursor.fetchall()

    container = tk.Frame(root, bg=BG)
    container.pack(fill="both", expand=True, padx=20, pady=15)
    tk.Label(container, text="Available Hotels", font=("Georgia", 17, "bold"),
             bg=BG, fg=TEXT).pack(anchor="w", pady=(0, 10))

    canvas2 = tk.Canvas(container, bg=BG, highlightthickness=0)
    scroll = tk.Scrollbar(container, orient="vertical", command=canvas2.yview)
    inner = tk.Frame(canvas2, bg=BG)
    inner.bind("<Configure>", lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))
    canvas2.create_window((0, 0), window=inner, anchor="nw")
    canvas2.configure(yscrollcommand=scroll.set)
    canvas2.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    if not hotels:
        tk.Label(inner, text="No hotels found in database.\nAdd hotels via MySQL first.",
                 font=FONT_SUB, bg=BG, fg=SUBTEXT, justify="center").pack(pady=50)
        return

    for h in hotels:
        hid, name, location, price = h
        row = tk.Frame(inner, bg=CARD, padx=16, pady=12,
                       highlightbackground=BORDER, highlightthickness=1)
        row.pack(fill="x", pady=5)

        left = tk.Frame(row, bg=CARD)
        left.pack(side="left", expand=True, fill="x")
        tk.Label(left, text=f"🏨  {name}", font=("Georgia", 13, "bold"),
                 bg=CARD, fg=TEXT).pack(anchor="w")
        tk.Label(left, text=f"📍 {location}", font=FONT_BODY, bg=CARD, fg=ACCENT2).pack(anchor="w")
        tk.Label(left, text=f"Hotel ID: {hid}", font=FONT_LBL, bg=CARD, fg=SUBTEXT).pack(anchor="w")

        right = tk.Frame(row, bg=CARD)
        right.pack(side="right")
        tk.Label(right, text=f"₹{price:,.0f}/night", font=("Georgia", 13, "bold"),
                 bg=CARD, fg=SUCCESS).pack()

        def book_this_hotel(hid=hid, hname=name):
            open_hotel_booking_form(user_id, hid, hname)

        b = tk.Button(right, text="Book →", command=book_this_hotel,
                      bg="#7C3AED", fg="white", font=FONT_LBL, relief="flat",
                      cursor="hand2", padx=8, pady=4)
        b.bind("<Enter>", lambda e, btn=b: btn.config(bg=ACCENT2))
        b.bind("<Leave>", lambda e, btn=b: btn.config(bg="#7C3AED"))
        b.pack(pady=(6, 0))


def open_hotel_booking_form(user_id, hotel_id, hotel_name):
    win = tk.Toplevel(root)
    win.title("Hotel Booking")
    win.geometry("380x340")
    win.configure(bg=CARD)
    win.grab_set()

    tk.Label(win, text=f"🏨  {hotel_name}", font=("Georgia", 15, "bold"),
             bg=CARD, fg=TEXT).pack(pady=(20, 4))
    tk.Label(win, text="Enter your stay dates", font=FONT_SUB, bg=CARD, fg=SUBTEXT).pack(pady=(0, 16))

    tk.Label(win, text="CHECK-IN DATE (YYYY-MM-DD)", bg=CARD, fg=SUBTEXT, font=FONT_LBL).pack(anchor="w", padx=40)
    cf, cin_e = styled_entry(win, width=25)
    cf.pack(padx=40, pady=(2, 12), anchor="w")

    tk.Label(win, text="CHECK-OUT DATE (YYYY-MM-DD)", bg=CARD, fg=SUBTEXT, font=FONT_LBL).pack(anchor="w", padx=40)
    of, cout_e = styled_entry(win, width=25)
    of.pack(padx=40, pady=(2, 20), anchor="w")

    def confirm():
        try:
            cursor.execute("INSERT INTO Bookings (user_id, booking_date) VALUES (%s, NOW())", (user_id,))
            conn.commit()
            bid = cursor.lastrowid
            cursor.execute("""INSERT INTO Hotel_Bookings (booking_id, hotel_id, check_in, check_out)
                              VALUES (%s,%s,%s,%s)""",
                           (bid, hotel_id, cin_e.get(), cout_e.get()))
            conn.commit()
            win.destroy()
            messagebox.showinfo("Booked! ✓", f"Hotel booked successfully!\nBooking ID: {bid}")
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    btn_row = tk.Frame(win, bg=CARD)
    btn_row.pack()
    accent_button(btn_row, "Confirm ✓", confirm, color=SUCCESS, width=12).pack(side="left", padx=8)
    accent_button(btn_row, "Cancel", win.destroy, color=DANGER, width=12).pack(side="left", padx=8)

# ============================================================
# SCREEN 7 — MY BOOKINGS
# ============================================================
def show_my_bookings(user_id):
    clear_root()
    root.configure(bg=BG)

    topbar = tk.Frame(root, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
    topbar.pack(fill="x")
    tk.Button(topbar, text="← Back", bg=CARD, fg=SUBTEXT, font=FONT_LBL, relief="flat",
              cursor="hand2",
              command=lambda: show_dashboard(user_id, get_user_name(user_id))).pack(side="left", padx=10, pady=12)
    tk.Label(topbar, text="📋  My Bookings", font=("Georgia", 15, "bold"),
             bg=CARD, fg=TEXT).pack(side="left", pady=12)

    cursor.execute("""
        SELECT b.booking_id, f.airline, f.source, f.destination,
               h.hotel_name, h.location, hb.check_in, hb.check_out, b.booking_date
        FROM Bookings b
        LEFT JOIN Flight_Bookings fb ON b.booking_id = fb.booking_id
        LEFT JOIN Flights f ON fb.flight_id = f.flight_id
        LEFT JOIN Hotel_Bookings hb ON b.booking_id = hb.booking_id
        LEFT JOIN Hotels h ON hb.hotel_id = h.hotel_id
        WHERE b.user_id = %s
        ORDER BY b.booking_date DESC
    """, (user_id,))
    rows = cursor.fetchall()

    container = tk.Frame(root, bg=BG)
    container.pack(fill="both", expand=True, padx=20, pady=15)
    tk.Label(container, text=f"{len(rows)} Booking(s) Found",
             font=("Georgia", 15, "bold"), bg=BG, fg=TEXT).pack(anchor="w", pady=(0, 10))

    if not rows:
        tk.Label(container, text="No bookings yet.\nGo book a flight or hotel!",
                 font=FONT_SUB, bg=BG, fg=SUBTEXT, justify="center").pack(pady=60)
        return

    canvas2 = tk.Canvas(container, bg=BG, highlightthickness=0)
    scroll = tk.Scrollbar(container, orient="vertical", command=canvas2.yview)
    inner = tk.Frame(canvas2, bg=BG)
    inner.bind("<Configure>", lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))
    canvas2.create_window((0, 0), window=inner, anchor="nw")
    canvas2.configure(yscrollcommand=scroll.set)
    canvas2.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    for r in rows:
        bid, airline, src, dst, hname, hloc, cin, cout, bdate = r
        card = tk.Frame(inner, bg=CARD, padx=16, pady=12,
                        highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="x", pady=5)

        header = tk.Frame(card, bg=CARD)
        header.pack(fill="x")
        tk.Label(header, text=f"Booking #{bid}", font=("Georgia", 12, "bold"),
                 bg=CARD, fg=ACCENT2).pack(side="left")
        tk.Label(header, text=str(bdate)[:16], font=FONT_LBL,
                 bg=CARD, fg=SUBTEXT).pack(side="right")

        if airline:
            tk.Label(card, text=f"✈  {airline}  |  {src} → {dst}",
                     font=FONT_BODY, bg=CARD, fg=TEXT).pack(anchor="w", pady=2)
        if hname:
            tk.Label(card, text=f"🏨  {hname}, {hloc}  |  {cin} → {cout}",
                     font=FONT_BODY, bg=CARD, fg=TEXT).pack(anchor="w", pady=2)

# ============================================================
# MAIN
# ============================================================
root = tk.Tk()
root.title("TravelEase — Booking System")
root.geometry("520x600")
root.resizable(False, False)
root.configure(bg=BG)

show_welcome()
root.mainloop()