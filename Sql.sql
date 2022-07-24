/*
SQLyog Ultimate v12.14 (64 bit)
MySQL - 8.0.28 : Database - dingpiaoxitong
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dingpiaoxitong` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `dingpiaoxitong`;

/*Table structure for table `dingpiao` */

DROP TABLE IF EXISTS `dingpiao`;

CREATE TABLE `dingpiao` (
  `Dingdanid` char(20) NOT NULL,
  `Dingpiaofangshi` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dingpiao` */

insert  into `dingpiao`(`Dingdanid`,`Dingpiaofangshi`) values 
('202206071k1234','网络'),
('202206072k4321','车站'),
('202206073k4321','网络'),
('202206074k1234','网络'),
('202206075k1234','网络');

/*Table structure for table `dingpiaoinfo` */

DROP TABLE IF EXISTS `dingpiaoinfo`;

CREATE TABLE `dingpiaoinfo` (
  `Dingdanid` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Userid` char(18) NOT NULL,
  `Trainid` char(10) NOT NULL,
  `Startday` datetime NOT NULL,
  `Dingpiaodate` datetime NOT NULL,
  `Dingpiaoshu` char(3) NOT NULL,
  `Allprice` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dingpiaoinfo` */

insert  into `dingpiaoinfo`(`Dingdanid`,`Userid`,`Trainid`,`Startday`,`Dingpiaodate`,`Dingpiaoshu`,`Allprice`) values 
('202206072k4321','11223344','k4321','2022-06-08 12:00:00','2022-06-07 15:30:00','1','20'),
('202206071k1234','55667788','k1234','2022-06-07 12:00:00','2022-06-07 09:31:23','1','20'),
('202206073k4321','33445566','k4321','2022-06-08 12:00:00','2022-06-07 16:35:50','1','20'),
('202206074k1234','99001122','k1234','2022-06-07 12:00:00','2022-06-07 20:36:47','1','20'),
('202206075k1234','88990055','k1234','2022-06-07 12:00:00','2022-06-07 20:50:47','1','20');

/*Table structure for table `train` */

DROP TABLE IF EXISTS `train`;

CREATE TABLE `train` (
  `Trainid` char(10) NOT NULL,
  `Startstation` char(20) NOT NULL,
  `Endstation` char(20) NOT NULL,
  `Startday` datetime NOT NULL,
  `Starttime` datetime NOT NULL,
  `Arrivetime` datetime NOT NULL,
  `Piaoshu` char(10) NOT NULL,
  `Price` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `train` */

insert  into `train`(`Trainid`,`Startstation`,`Endstation`,`Startday`,`Starttime`,`Arrivetime`,`Piaoshu`,`Price`) values 
('k1234','北京','长春','2022-06-07 12:00:00','2022-06-07 12:00:00','2022-06-08 17:24:19','4','20'),
('k4321','长春','北京','2022-06-08 12:00:00','2022-06-08 15:27:50','2022-06-09 15:27:57','5','20'),
('g60','南京','长沙','2022-06-10 12:00:00','2022-06-10 12:00:00','2022-06-11 12:00:00','20','50');

/*Table structure for table `tuipiao` */

DROP TABLE IF EXISTS `tuipiao`;

CREATE TABLE `tuipiao` (
  `Dingdanid` char(20) NOT NULL,
  `Dingpiaofangshi` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `tuipiao` */

insert  into `tuipiao`(`Dingdanid`,`Dingpiaofangshi`) values 
('202206072k4321','车站');

/*Table structure for table `userinfo` */

DROP TABLE IF EXISTS `userinfo`;

CREATE TABLE `userinfo` (
  `Userid` char(20) NOT NULL,
  `Username` char(20) NOT NULL,
  `Xingbie` char(2) DEFAULT NULL,
  `Phone` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `userinfo` */

insert  into `userinfo`(`Userid`,`Username`,`Xingbie`,`Phone`) values 
('11223344','张三','男','12345'),
('55667788','李四','女','67890'),
('99001122','王五','男','01234'),
('33445566','李六','女','34567'),
('88990055','刘九','男','78990');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
