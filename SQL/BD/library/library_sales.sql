CREATE DATABASE  IF NOT EXISTS `library` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `library`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: library
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Первичный ключ таблицы продаж',
  `quantity` int NOT NULL COMMENT 'Количество проданных книг (должно быть больше 0)',
  `book_price` decimal(10,2) NOT NULL COMMENT 'Цена книги на момент продажи',
  `total_price` decimal(10,2) GENERATED ALWAYS AS ((`quantity` * `book_price`)) STORED COMMENT 'Общая стоимость продажи (рассчитывается автоматически)',
  `order_id` int NOT NULL COMMENT 'ID связанного заказа',
  `book_id` int NOT NULL COMMENT 'ID проданной книги',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания записи',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время последнего обновления записи',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `order_id` (`order_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sales_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sales_chk_1` CHECK ((`quantity` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` (`id`, `quantity`, `book_price`, `order_id`, `book_id`, `created_at`, `updated_at`) VALUES (1,2,550.75,1,31,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(2,3,425.50,1,32,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(3,1,675.25,2,33,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(4,4,310.00,2,34,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(5,2,490.75,3,35,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(6,3,265.50,3,36,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(7,1,595.25,4,37,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(8,2,380.00,4,38,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(9,4,455.75,5,39,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(10,1,520.50,5,40,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(11,3,285.25,6,41,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(12,2,610.00,6,42,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(13,1,395.50,7,43,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(14,4,475.25,7,44,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(15,2,540.75,8,45,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(16,3,330.00,8,46,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(17,1,685.50,9,47,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(18,2,415.25,9,48,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(19,4,360.00,10,49,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(20,1,505.75,10,50,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(21,3,290.50,11,51,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(22,2,625.25,11,52,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(23,1,435.00,12,53,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(24,4,495.75,12,54,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(25,2,375.50,13,55,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(26,3,560.25,13,56,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(27,1,640.00,14,57,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(28,2,405.75,14,58,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(29,4,335.50,15,59,'2025-01-23 16:16:54','2025-01-23 16:16:54'),(30,1,590.25,15,60,'2025-01-23 16:16:54','2025-01-23 16:16:54');
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-23 21:23:36
