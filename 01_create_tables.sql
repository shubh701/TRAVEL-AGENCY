-- ============================================================
-- TravelEase — Online Travel Booking System
-- FILE     : 01_create_tables.sql
-- PURPOSE  : Creates all tables for travel_db
-- AUTHOR   : Shubh Varshney | Roll No. 51714803124 | Group I-8
-- SUBJECT  : Database Management Systems (DBMS)
-- ============================================================

DROP DATABASE IF EXISTS travel_db;
CREATE DATABASE travel_db;
USE travel_db;

-- ------------------------------------------------------------
-- TABLE 1 : Users
-- Stores registered user accounts
-- ------------------------------------------------------------
CREATE TABLE Users (
    user_id  INT PRIMARY KEY AUTO_INCREMENT,
    name     VARCHAR(100),
    email    VARCHAR(100) UNIQUE,
    password VARCHAR(100)
);

-- ------------------------------------------------------------
-- TABLE 2 : Flights
-- Stores all available flights
-- ------------------------------------------------------------
CREATE TABLE Flights (
    flight_id   INT PRIMARY KEY AUTO_INCREMENT,
    airline     VARCHAR(100),
    source      VARCHAR(50),
    destination VARCHAR(50),
    price       DECIMAL(10,2)
);

-- ------------------------------------------------------------
-- TABLE 3 : Hotels
-- Stores all available hotels
-- ------------------------------------------------------------
CREATE TABLE Hotels (
    hotel_id        INT PRIMARY KEY AUTO_INCREMENT,
    hotel_name      VARCHAR(100),
    location        VARCHAR(100),
    price_per_night DECIMAL(10,2)
);

-- ------------------------------------------------------------
-- TABLE 4 : Bookings
-- Master booking record — parent of Flight_Bookings
-- and Hotel_Bookings
-- ------------------------------------------------------------
CREATE TABLE Bookings (
    booking_id   INT PRIMARY KEY AUTO_INCREMENT,
    user_id      INT,
    booking_date DATETIME,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- ------------------------------------------------------------
-- TABLE 5 : Flight_Bookings
-- Junction table — links a Booking to a Flight
-- ------------------------------------------------------------
CREATE TABLE Flight_Bookings (
    id         INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT,
    flight_id  INT,
    FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id),
    FOREIGN KEY (flight_id)  REFERENCES Flights(flight_id)
);

-- ------------------------------------------------------------
-- TABLE 6 : Hotel_Bookings
-- Links a Booking to a Hotel with stay dates
-- ------------------------------------------------------------
CREATE TABLE Hotel_Bookings (
    id         INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT,
    hotel_id   INT,
    check_in   DATE,
    check_out  DATE,
    FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id),
    FOREIGN KEY (hotel_id)   REFERENCES Hotels(hotel_id)
);

-- ------------------------------------------------------------
-- TABLE 7 : Loyalty
-- Tracks reward points and membership tier per user
-- ------------------------------------------------------------
CREATE TABLE Loyalty (
    user_id INT,
    points  INT,
    tier    VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- ------------------------------------------------------------
-- TABLE 8 : BookingHistory
-- Audit log — records every status change of a booking
-- ------------------------------------------------------------
CREATE TABLE BookingHistory (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    booking_id  INT,
    status      VARCHAR(50),
    change_time DATETIME,
    FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id)
);
