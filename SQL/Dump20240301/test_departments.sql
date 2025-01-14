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
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `idDepartments` int NOT NULL AUTO_INCREMENT,
  `nameOtdel` varchar(50) NOT NULL,
  `bossOtdel` varchar(50) NOT NULL,
  PRIMARY KEY (`idDepartments`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,'Отдел разработки','Иванов Иван Иванович'),(2,'Отдел маркетинга','Петров Петр Петрович'),(3,'Отдел качества','Сидоров Сидор Сидорович'),(4,'Отдел продаж','Кузнецов Константин Константинович'),(5,'Отдел финансов','Смирнова Екатерина Владимировна'),(6,'Отдел кадров','Николаева Ольга Сергеевна'),(7,'Отдел логистики','Иванова Анна Васильевна'),(8,'Отдел аналитики','Петрова Мария Александровна'),(9,'Отдел юридический','Семенов Игорь Павлович'),(10,'Отдел безопасности','Григорьев Виктор Николаевич'),(11,'Отдел IT','Козлов Владислав Алексеевич'),(12,'Отдел PR','Михайлова Анастасия Игоревна'),(13,'Отдел закупок','Егоров Дмитрий Андреевич'),(14,'Отдел рекламы','Васильев Артем Олегович'),(15,'Отдел обслуживания','Тарасов Алексей Викторович'),(16,'Отдел стратегии','Белякова Елена Сергеевна'),(17,'Отдел развития','Сорокин Александр Васильевич'),(18,'Отдел инноваций','Кузнецова Ольга Дмитриевна'),(19,'Отдел контроля','Новиков Александр Петрович'),(20,'Отдел производства','Краснова Екатерина Ивановна');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
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
