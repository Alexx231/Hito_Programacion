-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 18-02-2024 a las 19:19:52
-- Versión del servidor: 8.2.0
-- Versión de PHP: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `solocrossfit`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `plan_trabajo` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `peso_actual` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `categoria_peso` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `gastos_detallados` text COLLATE utf8mb4_general_ci,
  `costo_total` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `comparacion_peso_categoria` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `eventos_competiciones` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `plan_trabajo`, `peso_actual`, `categoria_peso`, `gastos_detallados`, `costo_total`, `comparacion_peso_categoria`, `eventos_competiciones`) VALUES
(5, 'Oksana', 'tur', 'no', 'siman', NULL, '', '', NULL),
(6, 'flashflkahj', 'shoio5hijrs', 'sfdhksldfhjs', 'gfhkjariher', NULL, '', '', NULL),
(12, 'Alejandro', 'asdasd', '59kg', 'peso pluma', '800', '', '', NULL),
(13, 'Alejandro', 'asdasd', '59kg', 'peso pluma', '800', '', '', NULL),
(14, 'Alex', 'Sexo', '87kg', '85kg', '1500', '', '', NULL),
(15, 'ivan', 'si', '90', '100', '1200', '', '', NULL),
(16, 'vic', 'comermucho', '60', '70', '2500', '2000', '', '25');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
