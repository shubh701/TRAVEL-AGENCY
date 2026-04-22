-- ============================================================
-- TravelEase — Online Travel Booking System
-- FILE     : 03_sample_queries.sql
-- PURPOSE  : All SQL queries used in the Python application
-- AUTHOR   : Shubh Varshney | Roll No. 51714803124 | Group I-8
-- ============================================================

USE travel_db;

-- ------------------------------------------------------------
-- QUERY 1 : Register a new user
-- Used in : show_register() screen
-- ------------------------------------------------------------
INSERT INTO Users (name, email, password)
VALUES ('Test User', 'test@email.com', 'Pass@123');

-- ------------------------------------------------------------
-- QUERY 2 : Login / Authenticate user
-- Used in : show_login() screen
-- ------------------------------------------------------------
SELECT * FROM Users
WHERE email = 'shubh@email.com'
AND   password = 'Pass@123';

-- ------------------------------------------------------------
-- QUERY 3 : Get username for dashboard display
-- Used in : show_dashboard() top bar
-- ------------------------------------------------------------
SELECT name FROM Users
WHERE user_id = 1;

-- ------------------------------------------------------------
-- QUERY 4 : Fetch all available flights
-- Used in : show_flights() screen
-- ------------------------------------------------------------
SELECT * FROM Flights;

-- ------------------------------------------------------------
-- QUERY 5 : Fetch all available hotels
-- Used in : show_hotels() screen
-- ------------------------------------------------------------
SELECT * FROM Hotels;

-- ------------------------------------------------------------
-- QUERY 6 : Create a master booking record
-- Used in : confirm_flight() and open_hotel_booking_form()
-- Step 1 of every booking
-- ------------------------------------------------------------
INSERT INTO Bookings (user_id, booking_date)
VALUES (1, NOW());

-- ------------------------------------------------------------
-- QUERY 7 : Record a flight booking
-- Used in : confirm_flight()
-- Step 2 — runs right after Query 6
-- ------------------------------------------------------------
INSERT INTO Flight_Bookings (booking_id, flight_id)
VALUES (LAST_INSERT_ID(), 1);

-- ------------------------------------------------------------
-- QUERY 8 : Record a hotel booking with stay dates
-- Used in : open_hotel_booking_form()
-- Step 2 — runs right after Query 6
-- ------------------------------------------------------------
INSERT INTO Hotel_Bookings (booking_id, hotel_id, check_in, check_out)
VALUES (LAST_INSERT_ID(), 2, '2025-05-01', '2025-05-05');

-- ------------------------------------------------------------
-- QUERY 9 : Fetch all bookings for a user (5-table LEFT JOIN)
-- Used in : show_my_bookings() screen
-- This is the most complex query in the entire project
-- ------------------------------------------------------------
SELECT
    b.booking_id,
    f.airline,
    f.source,
    f.destination,
    h.hotel_name,
    h.location,
    hb.check_in,
    hb.check_out,
    b.booking_date
FROM Bookings b
LEFT JOIN Flight_Bookings fb ON b.booking_id = fb.booking_id
LEFT JOIN Flights f          ON fb.flight_id  = f.flight_id
LEFT JOIN Hotel_Bookings hb  ON b.booking_id  = hb.booking_id
LEFT JOIN Hotels h           ON hb.hotel_id   = h.hotel_id
WHERE b.user_id = 1
ORDER BY b.booking_date DESC;
