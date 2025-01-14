-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `result` (
  `idResult` int NOT NULL AUTO_INCREMENT,
  `ocenka` int DEFAULT NULL,
  `dolg` varchar(10) DEFAULT NULL,
  `student_id` int DEFAULT NULL,
  `tests_id` int DEFAULT NULL,
  PRIMARY KEY (`idResult`),
  KEY `student_id` (`student_id`),
  KEY `tests_id` (`tests_id`),
  CONSTRAINT `result_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`idStudent`),
  CONSTRAINT `result_ibfk_2` FOREIGN KEY (`tests_id`) REFERENCES `tests` (`idTest`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `result`
--

LOCK TABLES `result` WRITE;
/*!40000 ALTER TABLE `result` DISABLE KEYS */;
INSERT INTO `result` VALUES (31,4,'Нет',1,33),(32,5,'Да',2,34),(33,3,'Да',3,35),(34,4,'Нет',4,36),(35,5,'Да',5,37),(36,4,'Нет',6,38),(37,5,'Да',7,39),(38,3,'Да',8,40),(39,4,'Нет',9,41),(40,5,'Да',10,42),(41,4,'Нет',11,43),(42,5,'Да',12,44),(43,3,'Да',13,45),(44,4,'Нет',14,46),(45,5,'Да',15,47),(46,4,'Нет',16,48),(47,5,'Да',17,49),(48,3,'Да',18,50),(49,4,'Нет',19,51),(50,5,'Да',20,52),(51,4,'Нет',21,53),(52,5,'Да',22,54),(53,3,'Да',23,55),(54,4,'Нет',24,56),(55,5,'Да',25,57),(56,4,'Нет',26,58),(57,5,'Да',27,59),(58,3,'Да',28,60),(59,4,'Нет',29,61),(60,5,'Да',30,62);
/*!40000 ALTER TABLE `result` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-01 15:59:27
