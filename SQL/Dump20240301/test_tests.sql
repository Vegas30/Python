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
-- Table structure for table `tests`
--

DROP TABLE IF EXISTS `tests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tests` (
  `idTest` int NOT NULL AUTO_INCREMENT,
  `nameTest` varchar(255) NOT NULL,
  `proiden` varchar(10) NOT NULL,
  `ball` varchar(50) NOT NULL,
  `lesson_id` int DEFAULT NULL,
  PRIMARY KEY (`idTest`),
  KEY `lesson_id` (`lesson_id`),
  CONSTRAINT `tests_ibfk_1` FOREIGN KEY (`lesson_id`) REFERENCES `lessons` (`idLessons`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tests`
--

LOCK TABLES `tests` WRITE;
/*!40000 ALTER TABLE `tests` DISABLE KEYS */;
INSERT INTO `tests` VALUES (33,'Тест по математике','Да','90',1),(34,'Тест по физике','Нет','85',2),(35,'Тест по химии','Нет','80',3),(36,'Тест по биологии','Да','95',4),(37,'Тест по истории','Да','30',5),(38,'Тест по географии','Да','92',6),(39,'Тест по литературе','Да','20',7),(40,'Тест по английскому языку','Да','96',8),(41,'Тест по музыке','Да','85',9),(42,'Тест по изобразительному искусству','Да','90',10),(43,'Тест по физической культуре','Да','100',11),(44,'Тест по информатике','Нет','78',12),(45,'Тест по технологии','Нет','30',13),(46,'Тест по обществознанию','Да','87',14),(47,'Тест по праву','Да','94',15),(48,'Тест по психологии','Нет','40',16),(49,'Тест по экономике','Да','90',17),(50,'Тест по политологии','Да','34',18),(51,'Тест по социологии','Да','60',19),(52,'Тест по этике','Нет','89',20),(53,'Тест по программированию','Нет','91',21),(54,'Тест по маркетингу','Нет','93',22),(55,'Тест 21','Да','85',23),(56,'Тест 22','Да','50',24),(57,'Тест 23','Да','88',25),(58,'Тест 24','Да','92',26),(59,'Тест 25','Да','32',27),(60,'Тест 26','Нет','96',28),(61,'Тест 27','Нет','85',29),(62,'Тест 28','Да','56',30),(63,'Тест 29','Да','100',30),(64,'Тест 30','Нет','78',1);
/*!40000 ALTER TABLE `tests` ENABLE KEYS */;
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
