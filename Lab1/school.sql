-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2021-10-07 21:43:07
-- 服务器版本： 8.0.26
-- PHP 版本： 7.3.29-to-be-removed-in-future-macOS

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `school`
--

-- --------------------------------------------------------

--
-- 表的结构 `class`
--

CREATE TABLE `class` (
  `class_id` int NOT NULL,
  `class_name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `class`
--

INSERT INTO `class` (`class_id`, `class_name`) VALUES
(1, 'ip-05'),
(2, 'ip-06'),
(3, 'ip-07');

-- --------------------------------------------------------

--
-- 表的结构 `students`
--

CREATE TABLE `students` (
  `students_id` int NOT NULL,
  `students_name` varchar(30) NOT NULL,
  `class_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `students`
--

INSERT INTO `students` (`students_id`, `students_name`, `class_id`) VALUES
(1001, 'Bob', 1),
(1002, 'Burton', 1),
(1003, 'Nika', 2);

-- --------------------------------------------------------

--
-- 表的结构 `subjects`
--

CREATE TABLE `subjects` (
  `subjects_id` int NOT NULL,
  `subjects_name` varchar(10) NOT NULL,
  `students_id` int NOT NULL,
  `grades` int NOT NULL,
  `teachers_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `subjects`
--

INSERT INTO `subjects` (`subjects_id`, `subjects_name`, `students_id`, `grades`, `teachers_id`) VALUES
(101, 'database', 1001, 85, 1),
(102, 'linux', 1001, 79, 2),
(103, 'c++', 1002, 88, 3),
(101, 'database', 1002, 97, 1),
(101, 'database', 1003, 77, 1);

-- --------------------------------------------------------

--
-- 表的结构 `teachers`
--

CREATE TABLE `teachers` (
  `teachers_id` int NOT NULL,
  `teachers_name` varchar(30) NOT NULL,
  `Contact` int NOT NULL,
  `age` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `teachers`
--

INSERT INTO `teachers` (`teachers_id`, `teachers_name`, `Contact`, `age`) VALUES
(1, 'ALex', 634781292, 35),
(2, 'Allen', 904823742, 28),
(3, 'Oleg', 843294839, 45);

--
-- 转储表的索引
--

--
-- 表的索引 `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`class_id`);

--
-- 表的索引 `students`
--
ALTER TABLE `students`
  ADD KEY `FK` (`class_id`),
  ADD KEY `FK4` (`students_id`);

--
-- 表的索引 `subjects`
--
ALTER TABLE `subjects`
  ADD KEY `FK2` (`teachers_id`),
  ADD KEY `FK3` (`students_id`),
  ADD KEY `index` (`subjects_id`) USING BTREE;

--
-- 表的索引 `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`teachers_id`);

--
-- 限制导出的表
--

--
-- 限制表 `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `FK` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `FK4` FOREIGN KEY (`students_id`) REFERENCES `subjects` (`students_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- 限制表 `subjects`
--
ALTER TABLE `subjects`
  ADD CONSTRAINT `FK2` FOREIGN KEY (`teachers_id`) REFERENCES `teachers` (`teachers_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
