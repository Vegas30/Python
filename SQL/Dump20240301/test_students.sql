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
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `idStudent` int NOT NULL AUTO_INCREMENT,
  `surname` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `adress` varchar(255) NOT NULL,
  `city` varchar(50) NOT NULL,
  `region` int NOT NULL,
  `number` int NOT NULL,
  `special_id` int DEFAULT NULL,
  PRIMARY KEY (`idStudent`),
  KEY `special_id` (`special_id`),
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`special_id`) REFERENCES `specializations` (`idSpecial`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Иванов','Иван','ул. Ленина, д. 10','Москва',1,123456789,1),(2,'Петров','Петр','ул. Гагарина, д. 5','Санкт-Петербург',2,987654321,2),(3,'Сидоров','Сергей','ул. Пушкина, д. 15','Новосибирск',3,654321987,3),(4,'Козлов','Алексей','ул. Толстого, д. 20','Екатеринбург',4,456789123,4),(5,'Новикова','Анна','ул. Достоевского, д. 25','Казань',5,789123456,5),(6,'Кузнецов','Игорь','ул. Чехова, д. 30','Омск',6,321654987,6),(7,'Семенова','Марина','ул. Лермонтова, д. 35','Самара',7,654987321,7),(8,'Васильев','Владимир','ул. Пастернака, д. 40','Уфа',8,987321654,8),(9,'Попов','Дмитрий','ул. Булгакова, д. 45','Челябинск',9,258369147,9),(10,'Андреева','Ольга','ул. Федорова, д. 50','Ростов-на-Дону',10,147258369,10),(11,'Беляев','Евгений','ул. Тургенева, д. 55','Ульяновск',11,369147258,11),(12,'Лебедева','Татьяна','ул. Пушкина, д. 60','Владивосток',12,852963147,12),(13,'Алексеев','Илья','ул. Горького, д. 65','Красноярск',13,963147852,13),(14,'Смирнов','Максим','ул. Шевченко, д. 70','Иркутск',14,147852963,14),(15,'Егоров','Артем','ул. Дубровинского, д. 75','Воронеж',15,369258147,15),(16,'Тарасова','Анастасия','ул. Светланова, д. 80','Тольятти',16,258369741,16),(17,'Федоров','Никита','ул. Коллонтай, д. 85','Курск',17,741258369,17),(18,'Морозов','Павел','ул. Мира, д. 90','Саратов',18,369741258,18),(19,'Орлов','Денис','ул. Спартаковская, д. 95','Калининград',19,963741852,19),(20,'Богданова','Кристина','ул. Фурманова, д. 100','Ставрополь',20,741852963,20),(21,'Игнатьев','Роман','ул. Некрасова, д. 105','Ярославль',21,258741369,1),(22,'Соболева','Елена','ул. Лермонтова, д. 110','Иваново',22,852369741,2),(23,'Макаров','Сергей','ул. Пушкина, д. 115','Барнаул',23,369852147,3),(24,'Воронов','Александр','ул. Гоголя, д. 120','Улан-Удэ',24,147369852,4),(25,'Федосеева','Екатерина','ул. Шмидта, д. 125','Магнитогорск',25,963852741,5),(26,'Григорьев','Антон','ул. Куйбышева, д. 130','Тула',26,741369852,6),(27,'Ефимова','Алина','ул. Серова, д. 135','Сочи',27,258147369,7),(28,'Данилов','Владислав','ул. Ленина, д. 140','Владимир',28,369741258,8),(29,'Сергеев','Артемий','ул. Курчатова, д. 145','Пенза',29,147852369,9),(30,'Кузьмина','Дарья','ул. Гагарина, д. 150','Тамбов',30,852369147,10);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
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
