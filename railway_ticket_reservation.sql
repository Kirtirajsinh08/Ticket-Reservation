-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 19, 2024 at 02:22 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `railway ticket reservation`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `getUser` ()   BEGIN
select * from user;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `NAME` varchar(20) NOT NULL,
  `GENDER` varchar(10) NOT NULL,
  `AGE` int(10) NOT NULL,
  `PRICE` decimal(10,0) NOT NULL,
  `CURRENT_STATUS` varchar(30) NOT NULL,
  `PNR` bigint(20) NOT NULL,
  `TRAIN_NO` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`NAME`, `GENDER`, `AGE`, `PRICE`, `CURRENT_STATUS`, `PNR`, `TRAIN_NO`) VALUES
('shlok', 'm', 19, 380, 'A3/33', 84417125, 12146),
('ravi', 'm', 19, 130, 'B3/21', 84417139, 12146),
('deep', 'm', 19, 960, 'D2/54', 84417140, 12933),
('utsav', 'm', 19, 960, 'B1/42', 84417158, 12933),
('hello', '91', 91, 960, 'C2/46', 84417159, 12933),
('rudra', 'm', 17, 1500, 'C2/44', 84417160, 9404),
('teerth', 'male', 18, 960, 'A2/37', 84417162, 12933),
('shlok', 'male', 19, 960, 'B1/52', 84417163, 12933);

-- --------------------------------------------------------

--
-- Table structure for table `train`
--

CREATE TABLE `train` (
  `TRAIN_NO` int(10) NOT NULL,
  `TRAIN_NAME` varchar(20) NOT NULL,
  `SOURCE` varchar(20) NOT NULL,
  `DESTINATION` varchar(20) NOT NULL,
  `DEPARTURE` time NOT NULL,
  `ARRIVAL` time NOT NULL,
  `DURATION` time NOT NULL,
  `2S_AVAIL` int(10) NOT NULL,
  `CC_AVAIL` int(10) NOT NULL,
  `2S_PRICE` decimal(10,0) NOT NULL,
  `CC_PRICE` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `train`
--

INSERT INTO `train` (`TRAIN_NO`, `TRAIN_NAME`, `SOURCE`, `DESTINATION`, `DEPARTURE`, `ARRIVAL`, `DURATION`, `2S_AVAIL`, `CC_AVAIL`, `2S_PRICE`, `CC_PRICE`) VALUES
(12933, 'KARNAVATI SF', 'AHMEDABAD(ADI)', 'MUMBAI (MMCT)', '05:12:15', '14:12:15', '09:00:00', 35, 29, 280, 960),
(12146, 'BRC INTERCITY', 'AHMEDABAD(ADI)', 'VADODRA(BRC)', '14:30:00', '16:05:00', '01:35:00', 22, 19, 130, 380),
(12957, 'SWARNA RAJ', 'AHMEDABAD(ADI)', 'DELHI(DL)', '07:05:00', '20:05:00', '13:00:00', 123, 45, 460, 1200),
(22955, 'BANDRA MAHUVA SF', 'BANDRA T(BDTS)', 'MAHUVA(MHV)', '17:00:00', '09:00:00', '16:00:00', 12, 34, 378, 890),
(12951, 'RAJDHANI EXPRESS', 'DELHI (DL)', 'MUMBAI (MMCT)', '17:00:00', '08:35:00', '15:35:00', 234, 65, 660, 1340),
(12930, 'DOUBLE DECKER EXP', 'AHMEDABAD(ADI)', 'MUMBAI (MMCT)', '06:00:00', '13:00:00', '07:00:00', 110, 30, 300, 1250),
(9404, 'VANDE BHARAT EXP', 'AHMEDABAD(ADI)', 'MUMBAI (MMCT)', '15:00:00', '21:00:00', '09:00:00', 0, 117, 0, 1500),
(22953, 'GUJARAT SF EXPRESS', 'AHMEDABAD(ADI)', 'MUMBAI (MMCT)', '07:00:00', '14:00:00', '07:00:00', 121, 227, 460, 1080);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `USER_ID` int(5) NOT NULL,
  `USER_NAME` varchar(20) NOT NULL,
  `PASSWORD` varchar(20) NOT NULL,
  `PHONE_NUM` bigint(20) NOT NULL,
  `EMAIL` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`USER_ID`, `USER_NAME`, `PASSWORD`, `PHONE_NUM`, `EMAIL`) VALUES
(12412, 'shlok', 'shlok@1234', 9978689731, 'shlokmewada@gmail.com'),
(98747, 'yash', 'yash@1234', 9842566438, 'yashmishra@gmail.com'),
(36873, 'deep', 'deep@1234', 9937566883, 'deepatel@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`PNR`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `PNR` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84417164;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
