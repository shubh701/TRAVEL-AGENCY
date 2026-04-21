# ✈️ Travel Booking Database — MySQL Mini Project

A fully relational MySQL database system for managing travel bookings, including flights, hotels, users, loyalty points, and booking history.

---

## 📌 Project Overview

This project simulates the backend database of a travel booking platform (like MakeMyTrip or Goibibo). It handles user registrations, flight and hotel bookings, loyalty rewards, and tracks the full history of every booking.

---

## 🗄️ Database Name

```
travel_db
```

---

## 📊 Schema — Tables

| Table | Description |
|---|---|
| `Users` | Stores registered user info |
| `Flights` | Available flights with airline, route, and price |
| `Hotels` | Available hotels with location and price per night |
| `Bookings` | Master booking record linked to a user |
| `Flight_Bookings` | Links a booking to a specific flight |
| `Hotel_Bookings` | Links a booking to a hotel with check-in/check-out dates |
| `Loyalty` | Tracks loyalty points and tier for each user |
| `BookingHistory` | Logs every status change of a booking over time |

---

## 🔗 Entity Relationship Overview

```
Users
 ├── Bookings
 │    ├── Flight_Bookings → Flights
 │    ├── Hotel_Bookings  → Hotels
 │    └── BookingHistory
 └── Loyalty
```

---

## 🚀 How to Set Up

### Prerequisites
- MySQL 8.0+ installed
- MySQL Workbench or any MySQL client

### Option 1 — MySQL Workbench
1. Open **MySQL Workbench**
2. Connect to `root @ localhost`
3. Open the `travel_db.sql` file
4. Press `Ctrl + Shift + Enter` to run all

### Option 2 — Terminal / Command Line
```bash
mysql -u root -p < travel_db.sql
```

### Option 3 — Paste manually
```bash
mysql -u root -p
# Then paste the contents of travel_db.sql
```

---

## 📁 Project Structure

```
travel-db-mysql/
├── travel_db.sql       # Full database schema
└── README.md           # Project documentation
```

---

## 🧩 Table Details

### Users
```sql
user_id | name | email
```

### Flights
```sql
flight_id | airline | source | destination | price
```

### Hotels
```sql
hotel_id | hotel_name | location | price_per_night
```

### Bookings
```sql
booking_id | user_id | booking_date
```

### Flight_Bookings
```sql
id | booking_id | flight_id
```

### Hotel_Bookings
```sql
id | booking_id | hotel_id | check_in | check_out
```

### Loyalty
```sql
user_id | points | tier
```

### BookingHistory
```sql
id | booking_id | status | change_time
```

---

## 💡 Features

- ✅ Normalized relational schema (Foreign Keys throughout)
- ✅ Supports both flight and hotel bookings under one master booking
- ✅ Loyalty points and tier tracking per user
- ✅ Full booking status history / audit trail
- ✅ Clean separation of concerns across tables

---

## 🛠️ Tech Stack

| Tool | Usage |
|---|---|
| MySQL 8.0 | Database engine |
| MySQL Workbench | GUI client |
| SQL | Schema definition & querying |

---

## 👨‍💻 Author

**Shubh**  
Mini Project — DBMS  
📍 Delhi, India

---

## 📜 License

This project is open source and free to use for learning purposes.
