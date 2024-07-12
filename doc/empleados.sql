CREATE DATABASE IF NOT EXISTS `empleados_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE empleados_db;

CREATE TABLE IF NOT EXISTS `empleados` (
  `idempleado` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `foto` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`idempleado`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO empleados VALUES(NULL,'Juan Perez','jperez@correo.com','unafotodejuan.jpg');

SELECT * FROM empleados_db.empleados;