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
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `idTeachers` int NOT NULL AUTO_INCREMENT,
  `surname` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `otchestvo` varchar(255) NOT NULL,
  `post` varchar(255) NOT NULL,
  `phone` int NOT NULL,
  `departments_id` int DEFAULT NULL,
  PRIMARY KEY (`idTeachers`),
  KEY `departments_id` (`departments_id`),
  CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`departments_id`) REFERENCES `departments` (`idDepartments`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (1,'Иванов','Иван','Иванович','Преподаватель',123456789,1),(2,'Петров','Петр','Петрович','Доцент',987654321,2),(3,'Сидоров','Сидор','Сидорович','Профессор',111111111,3),(4,'Кузнецов','Константин','Константинович','Преподаватель',222222222,1),(5,'Смирнов','Сергей','Сергеевич','Доцент',333333333,2),(6,'Иванова','Анна','Ивановна','Профессор',444444444,3),(7,'Петрова','Мария','Петровна','Преподаватель',555555555,1),(8,'Семенов','Игорь','Игоревич','Доцент',666666666,2),(9,'Козлов','Владислав','Владиславович','Профессор',777777777,3),(10,'Михайлов','Анастасия','Андреевна','Преподаватель',888888888,1),(11,'Егоров','Дмитрий','Дмитриевич','Доцент',999999999,2),(12,'Васильев','Артем','Артемович','Профессор',101010101,3),(13,'Тарасов','Алексей','Алексеевич','Преподаватель',121212121,1),(14,'Белякова','Елена','Евгеньевна','Доцент',131313131,2),(15,'Сорокин','Александр','Александрович','Профессор',141414141,3),(16,'Кузнецова','Ольга','Олеговна','Преподаватель',151515151,1),(17,'Новиков','Павел','Павлович','Доцент',161616161,2),(18,'Краснов','Евгений','Евгеньевич','Профессор',171717171,3),(19,'Ковалев','Алексей','Алексеевич','Преподаватель',181818181,1),(20,'Савельев','Михаил','Михайлович','Доцент',191919191,2);
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-01 15:59:28
