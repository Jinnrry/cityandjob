-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2017-10-12 08:26:47
-- 服务器版本： 5.7.17-log
-- PHP Version: 7.1.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `51job`
--

-- --------------------------------------------------------

--
-- 表的结构 `jobinfo`
--

CREATE TABLE `jobinfo` (
  `id` int(11) NOT NULL,
  `post` varchar(50) NOT NULL COMMENT '招聘标题',
  `locate` varchar(20) NOT NULL COMMENT '工作地点',
  `salary_max` float NOT NULL COMMENT '最高工资',
  `salary_min` float NOT NULL COMMENT '最低工资',
  `type` varchar(10) NOT NULL COMMENT '工作类型',
  `href` varchar(100) NOT NULL COMMENT '详情链接',
  `datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '采集时间',
  `locat_num` int(11) NOT NULL COMMENT '该城市编号',
  `page` int(11) NOT NULL COMMENT '该城市第多少页数据'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `roomprice`
--

CREATE TABLE `roomprice` (
  `id` int(11) NOT NULL,
  `cityname` varchar(20) COLLATE utf8_bin NOT NULL,
  `price` int(11) NOT NULL,
  `datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据采集时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `jobinfo`
--
ALTER TABLE `jobinfo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `href` (`href`);

--
-- Indexes for table `roomprice`
--
ALTER TABLE `roomprice`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `jobinfo`
--
ALTER TABLE `jobinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `roomprice`
--
ALTER TABLE `roomprice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;COMMIT;
