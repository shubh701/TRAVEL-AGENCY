-- ============================================================
-- TravelEase — Online Travel Booking System
-- FILE     : 02_insert_data.sql
-- PURPOSE  : Inserts sample data into all tables
-- AUTHOR   : Shubh Varshney | Roll No. 51714803124 | Group I-8
-- NOTE     : Run 01_create_tables.sql first
-- ============================================================

USE travel_db;

-- ------------------------------------------------------------
-- USERS
-- ------------------------------------------------------------
INSERT INTO Users (name, email, password) VALUES
('Shubh Varshney', 'shubh@email.com',  'Pass@123'),
('Priya Mehta',    'priya@email.com',  'Pass@123'),
('Arjun Verma',    'arjun@email.com',  'Pass@123'),
('Sneha Patel',    'sneha@email.com',  'Pass@123'),
('Rohan Gupta',    'rohan@email.com',  'Pass@123');

-- ------------------------------------------------------------
-- FLIGHTS
-- ------------------------------------------------------------
INSERT INTO Flights (airline, source, destination, price) VALUES
('IndiGo',    'Delhi',   'Mumbai',    3500.00),
('Air India', 'Mumbai',  'Bangalore', 4200.00),
('SpiceJet',  'Delhi',   'Goa',       2900.00),
('Vistara',   'Chennai', 'Delhi',     5100.00),
('GoFirst',   'Kolkata', 'Hyderabad', 3800.00),
('IndiGo',    'Delhi',   'Bangalore', 4000.00),
('Air India', 'Goa',     'Mumbai',    3100.00);

-- ------------------------------------------------------------
-- HOTELS
-- ------------------------------------------------------------
INSERT INTO Hotels (hotel_name, location, price_per_night) VALUES
('The Taj Mahal Palace', 'Mumbai',    12000.00),
('Lemon Tree Hotel',     'Delhi',      3500.00),
('ITC Gardenia',         'Bangalore',  8000.00),
('Novotel Goa',          'Goa',        6500.00),
('Hyatt Regency',        'Chennai',    7200.00),
('Radisson Blu',         'Hyderabad',  5500.00),
('OYO Rooms',            'Kolkata',    1200.00);

-- ------------------------------------------------------------
-- BOOKINGS
-- ------------------------------------------------------------
INSERT INTO Bookings (user_id, booking_date) VALUES
(1, '2025-01-10 10:30:00'),
(2, '2025-01-15 14:00:00'),
(3, '2025-02-01 09:15:00'),
(4, '2025-02-14 18:45:00'),
(5, '2025-03-05 11:00:00'),
(1, '2025-03-20 16:30:00'),
(2, '2025-04-01 08:00:00');

-- ------------------------------------------------------------
-- FLIGHT BOOKINGS
-- ------------------------------------------------------------
INSERT INTO Flight_Bookings (booking_id, flight_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7);

-- ------------------------------------------------------------
-- HOTEL BOOKINGS
-- ------------------------------------------------------------
INSERT INTO Hotel_Bookings (booking_id, hotel_id, check_in, check_out) VALUES
(1, 1, '2025-01-12', '2025-01-15'),
(2, 2, '2025-01-16', '2025-01-18'),
(3, 4, '2025-02-03', '2025-02-07'),
(4, 5, '2025-02-15', '2025-02-17'),
(5, 6, '2025-03-06', '2025-03-10'),
(6, 3, '2025-03-22', '2025-03-25'),
(7, 7, '2025-04-02', '2025-04-04');

-- ------------------------------------------------------------
-- LOYALTY
-- ------------------------------------------------------------
INSERT INTO Loyalty (user_id, points, tier) VALUES
(1, 1500, 'Gold'),
(2,  800, 'Silver'),
(3,  200, 'Bronze'),
(4, 3200, 'Platinum'),
(5,  450, 'Bronze');

-- ------------------------------------------------------------
-- BOOKING HISTORY
-- ------------------------------------------------------------
INSERT INTO BookingHistory (booking_id, status, change_time) VALUES
(1, 'Confirmed',  '2025-01-10 10:31:00'),
(1, 'Checked-In', '2025-01-12 08:00:00'),
(1, 'Completed',  '2025-01-15 12:00:00'),
(2, 'Confirmed',  '2025-01-15 14:01:00'),
(2, 'Cancelled',  '2025-01-16 09:00:00'),
(3, 'Confirmed',  '2025-02-01 09:16:00'),
(3, 'Completed',  '2025-02-07 11:00:00'),
(4, 'Confirmed',  '2025-02-14 18:46:00'),
(5, 'Confirmed',  '2025-03-05 11:01:00'),
(6, 'Confirmed',  '2025-03-20 16:31:00');
