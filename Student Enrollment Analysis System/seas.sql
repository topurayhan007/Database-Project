-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2021 at 07:02 PM
-- Server version: 8.0.27
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `seas`
--

-- --------------------------------------------------------

--
-- Table structure for table `classroom_t`
--

CREATE TABLE `classroom_t` (
  `roomID` varchar(7) NOT NULL,
  `roomCapacity` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `course_t`
--

CREATE TABLE `course_t` (
  `courseID` varchar(7) NOT NULL,
  `courseName` varchar(50) NOT NULL,
  `creditHour` int NOT NULL,
  `deptcode` varchar(3) NOT NULL,
  `semester` varchar(6) NOT NULL,
  `year` year NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `department_t`
--

CREATE TABLE `department_t` (
  `deptCode` varchar(3) NOT NULL,
  `deptName` varchar(50) NOT NULL,
  `schoolTitle` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `faculty_t`
--

CREATE TABLE `faculty_t` (
  `facultyID` int NOT NULL,
  `facultyName` varchar(50) NOT NULL,
  `deptCode` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `school_t`
--

CREATE TABLE `school_t` (
  `schoolTitle` varchar(6) NOT NULL,
  `schoolName` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `section_t`
--

CREATE TABLE `section_t` (
  `courseID` varchar(7) NOT NULL,
  `sectionNo` int NOT NULL,
  `semester` varchar(6) NOT NULL,
  `year` year NOT NULL,
  `roomID` varchar(7) NOT NULL,
  `capacity` int NOT NULL,
  `noOfEnrolledStudent` int NOT NULL,
  `facultyID` int NOT NULL,
  `startTime` time DEFAULT NULL,
  `endTime` time DEFAULT NULL,
  `day` varchar(4) NOT NULL,
  `blocked` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `classroom_t`
--
ALTER TABLE `classroom_t`
  ADD PRIMARY KEY (`roomID`);

--
-- Indexes for table `course_t`
--
ALTER TABLE `course_t`
  ADD PRIMARY KEY (`courseID`),
  ADD KEY `deptcode` (`deptcode`);

--
-- Indexes for table `department_t`
--
ALTER TABLE `department_t`
  ADD PRIMARY KEY (`deptCode`),
  ADD KEY `schoolTitle` (`schoolTitle`);

--
-- Indexes for table `faculty_t`
--
ALTER TABLE `faculty_t`
  ADD PRIMARY KEY (`facultyID`),
  ADD KEY `deptCode` (`deptCode`);

--
-- Indexes for table `school_t`
--
ALTER TABLE `school_t`
  ADD PRIMARY KEY (`schoolTitle`);

--
-- Indexes for table `section_t`
--
ALTER TABLE `section_t`
  ADD PRIMARY KEY (`courseID`,`sectionNo`,`semester`,`year`),
  ADD KEY `facultyID` (`facultyID`),
  ADD KEY `roomID` (`roomID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `course_t`
--
ALTER TABLE `course_t`
  ADD CONSTRAINT `course_t_ibfk_1` FOREIGN KEY (`deptcode`) REFERENCES `department_t` (`deptCode`);

--
-- Constraints for table `department_t`
--
ALTER TABLE `department_t`
  ADD CONSTRAINT `department_t_ibfk_1` FOREIGN KEY (`schoolTitle`) REFERENCES `school_t` (`schoolTitle`);

--
-- Constraints for table `faculty_t`
--
ALTER TABLE `faculty_t`
  ADD CONSTRAINT `faculty_t_ibfk_1` FOREIGN KEY (`deptCode`) REFERENCES `department_t` (`deptCode`);

--
-- Constraints for table `section_t`
--
ALTER TABLE `section_t`
  ADD CONSTRAINT `section_t_ibfk_1` FOREIGN KEY (`facultyID`) REFERENCES `faculty_t` (`facultyID`),
  ADD CONSTRAINT `section_t_ibfk_2` FOREIGN KEY (`roomID`) REFERENCES `classroom_t` (`roomID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
