CREATE DATABASE blood_bank;

USE blood_bank;

CREATE TABLE donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    blood_type VARCHAR(3) NOT NULL,
    contact_number VARCHAR(15) NOT NULL
);

CREATE TABLE donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_id INT,
    donation_date DATE NOT NULL,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id)
);

CREATE TABLE blood_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    blood_type VARCHAR(3) NOT NULL,
    request_date DATE NOT NULL,
    status ENUM('Pending', 'Fulfilled') DEFAULT 'Pending'
);
