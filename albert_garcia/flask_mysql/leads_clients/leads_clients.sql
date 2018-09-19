-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: leads_clients
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `clients` (
  `client_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (2,'Michael','Choi','2018-09-13 00:00:00','2018-09-13 00:00:00'),(3,'Joe','Smith','2018-09-13 00:00:00','2018-09-13 00:00:00'),(4,'Ryan','Owen','2018-09-13 00:00:00','2018-09-13 00:00:00'),(5,'Masaki','Fujimoto','2018-09-13 00:00:00','2018-09-13 00:00:00');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leads`
--

DROP TABLE IF EXISTS `leads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `leads` (
  `lead_id` int(11) NOT NULL AUTO_INCREMENT,
  `clients_client_id` int(11) NOT NULL,
  `lead_name` varchar(90) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`lead_id`),
  KEY `fk_leads_clients_idx` (`clients_client_id`),
  CONSTRAINT `fk_leads_clients` FOREIGN KEY (`clients_client_id`) REFERENCES `clients` (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leads`
--

LOCK TABLES `leads` WRITE;
/*!40000 ALTER TABLE `leads` DISABLE KEYS */;
INSERT INTO `leads` VALUES (1,2,'youtube','2018-09-13 00:00:00','2018-09-13 00:00:00'),(2,2,'yahoo','2018-09-13 00:00:00','2018-09-13 00:00:00'),(3,2,'google','2018-09-13 00:00:00','2018-09-13 00:00:00'),(4,2,'apple','2018-09-13 00:00:00','2018-09-13 00:00:00'),(22,3,'target','2018-09-13 00:00:00','2018-09-13 00:00:00'),(23,3,'Walmart','2018-09-13 00:00:00','2018-09-13 00:00:00'),(24,3,'Sears','2018-09-13 00:00:00','2018-09-13 00:00:00'),(25,4,'Taco Bell','2018-09-13 00:00:00','2018-09-13 00:00:00'),(26,4,'McDonalds','2018-09-13 00:00:00','2018-09-13 00:00:00'),(27,4,'Wendy\'s','2018-09-13 00:00:00','2018-09-13 00:00:00'),(28,4,'Burger King','2018-09-13 00:00:00','2018-09-13 00:00:00'),(29,4,'Whataburger','2018-09-13 00:00:00','2018-09-13 00:00:00'),(30,4,'Chickfila','2018-09-13 00:00:00','2018-09-13 00:00:00'),(31,4,'Pizza Hut','2018-09-13 00:00:00','2018-09-13 00:00:00'),(32,5,'A1','2018-09-13 00:00:00','2018-09-13 00:00:00'),(33,5,'A-Z','2018-09-13 00:00:00','2018-09-13 00:00:00'),(34,5,'AAA','2018-09-13 00:00:00','2018-09-13 00:00:00'),(35,5,'ABC','2018-09-13 00:00:00','2018-09-13 00:00:00'),(36,5,'Fox','2018-09-13 00:00:00','2018-09-13 00:00:00'),(37,5,'NBC','2018-09-13 00:00:00','2018-09-13 00:00:00'),(38,5,'CBS','2018-09-13 00:00:00','2018-09-13 00:00:00');
/*!40000 ALTER TABLE `leads` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-15 13:15:10
