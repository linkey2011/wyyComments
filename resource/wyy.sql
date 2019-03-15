/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 50722
 Source Host           : localhost:3306
 Source Schema         : wyy

 Target Server Type    : MySQL
 Target Server Version : 50722
 File Encoding         : 65001

 Date: 15/03/2019 20:45:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for listener
-- ----------------------------
DROP TABLE IF EXISTS `listener`;
CREATE TABLE `listener`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `listenerid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 33 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for songtotal
-- ----------------------------
DROP TABLE IF EXISTS `songtotal`;
CREATE TABLE `songtotal`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `songid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `ok` int(10) NULL DEFAULT 0,
  `finish` int(10) NULL DEFAULT 0,
  `lastpage` int(10) NULL DEFAULT 1,
  `listenerid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `num` int(11) NULL DEFAULT NULL,
  `songname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6287 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
