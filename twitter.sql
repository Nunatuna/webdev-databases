-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: mariadb
-- Generation Time: Oct 01, 2025 at 03:19 PM
-- Server version: 10.6.20-MariaDB-ubu2004
-- PHP Version: 8.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `twitter`
--

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `post_pk` bigint(20) UNSIGNED NOT NULL,
  `post_user_fk` bigint(20) UNSIGNED NOT NULL,
  `post_message` varchar(280) NOT NULL,
  `post_total_likes` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`post_pk`, `post_user_fk`, `post_message`, `post_total_likes`) VALUES
(1, 11, 'My first post! Hello World!', 10),
(2, 11, 'My Second Post! This is so easy!', 20),
(3, 11, 'My third post! Im on a roll!', 30),
(4, 9, 'My Fourth post', 40),
(5, 9, 'My fifth post!', 50),
(6, 11, 'Sixth post! Wow', 60),
(8, 11, 'Seventh post!', 70);

-- --------------------------------------------------------

--
-- Table structure for table `trending`
--

CREATE TABLE `trending` (
  `trend_pk` bigint(20) UNSIGNED NOT NULL,
  `trend_title` varchar(20) NOT NULL,
  `trend_tag` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trending`
--

INSERT INTO `trending` (`trend_pk`, `trend_title`, `trend_tag`) VALUES
(1, 'Grækenland', 'Denmark'),
(2, 'Cooking', 'Italy'),
(3, 'Camping', 'Denmark'),
(4, 'Hiking', 'Norway'),
(5, 'Technology', 'Germany'),
(6, 'Mental health', 'Canada'),
(7, 'Human Rights', 'USA'),
(8, 'Meat balls', 'Sweden');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_pk` bigint(20) UNSIGNED NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  `user_username` varchar(20) NOT NULL,
  `user_first_name` varchar(20) NOT NULL,
  `user_last_name` varchar(20) NOT NULL,
  `user_avatar_path` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_pk`, `user_email`, `user_password`, `user_username`, `user_first_name`, `user_last_name`, `user_avatar_path`) VALUES
(9, 'ette@gmail.com', 'scrypt:32768:8:1$8Tk2zopyEtkmgUbk$7341cf48a9b7a9f1f5dade2c3565f81450d5ce98a675e3cefd20f07aff9cfbcebabf403b9e1bc010d35d43d486e7ae395ef9e80640fd7e73687be51a5f2f2df0', 'Ette', 'Henriette', 'Christiansen', 'https://avatar.iran.liara.run/public/35'),
(11, 'aiden@gmail.com', 'scrypt:32768:8:1$toC33rDpwT5ZBi2O$e3ffb01ca0cd61dd13e90ace7bddf77ea475473a61dece344c2ad43612d7ae061044f29f63264fad5169616efdd6a5851b8dd3c2d633c094a63b6e8199002129', 'Nuna', 'Aiden', 'Schnegelsberg', 'https://avatar.iran.liara.run/public/50'),
(12, 'user1@gmail.com', 'scrypt:32768:8:1$toC33rDpwT5ZBi2O$e3ffb01ca0cd61dd13e90ace7bddf77ea475473a61dece344c2ad43612d7ae061044f29f63264fad5169616efdd6a5851b8dd3c2d633c094a63b6e8199002129', 'shonk', 'Gordon', 'Blue', 'https://avatar.iran.liara.run/public/21'),
(13, 'nuggies@gmail.com', 'scrypt:32768:8:1$toC33rDpwT5ZBi2O$e3ffb01ca0cd61dd13e90ace7bddf77ea475473a61dece344c2ad43612d7ae061044f29f63264fad5169616efdd6a5851b8dd3c2d633c094a63b6e8199002129', 'nuggies', 'Buddy', 'Bud', 'https://avatar.iran.liara.run/public/60');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`post_pk`),
  ADD UNIQUE KEY `post_pk` (`post_pk`);

--
-- Indexes for table `trending`
--
ALTER TABLE `trending`
  ADD PRIMARY KEY (`trend_pk`),
  ADD UNIQUE KEY `trend_pk` (`trend_pk`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_pk`),
  ADD UNIQUE KEY `user_pk` (`user_pk`),
  ADD UNIQUE KEY `user_email` (`user_email`),
  ADD UNIQUE KEY `user_name` (`user_username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `post_pk` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `trending`
--
ALTER TABLE `trending`
  MODIFY `trend_pk` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_pk` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
