-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-06-2026 a las 00:57:43
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestionbecas_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `becas`
--

CREATE TABLE `becas` (
  `id_beca` int(11) NOT NULL,
  `nombre_beca` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `gestion` varchar(20) NOT NULL,
  `promedio_minimo` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `becas`
--

INSERT INTO `becas` (`id_beca`, `nombre_beca`, `descripcion`, `gestion`, `promedio_minimo`) VALUES
(1, 'Beca Comedor', 'Asignación diaria de almuerzo en el comedor universitario.', '1/2026', 60.00),
(2, 'Beca Trabajo IDH', 'Apoyo económico a cambio de 20 horas semanales de apoyo en laboratorios o bibliotecas.', '1/2026', 65.00),
(3, 'Beca Excelencia Académica', 'Exoneración total de valores y estipendio mensual para los promedios más altos.', '1/2026', 85.00),
(5, 'Beca Deporte', 'Destinada a estudiantes destacados en disciplinas deportivas de la universidad.', '1/2026', 55.00),
(6, 'Beca Vivienda', 'Subsidio habitacional o asignación en albergue universitario para estudiantes de provincias alejadas.', '1/2026', 70.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `documentos`
--

CREATE TABLE `documentos` (
  `id_documento` int(11) NOT NULL,
  `id_postulacion` int(11) NOT NULL,
  `tipo_documento` varchar(100) NOT NULL,
  `url_archivo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `documentos`
--

INSERT INTO `documentos` (`id_documento`, `id_postulacion`, `tipo_documento`, `url_archivo`) VALUES
(1, 1, 'Formulario Socioeconómico', '/uploads/2026/comedor/formulario_100203.pdf'),
(2, 1, 'Croquis de Domicilio', '/uploads/2026/comedor/croquis_100203.pdf'),
(3, 2, 'Historial Académico Unificado', '/uploads/2026/excelencia/historial_100204.pdf'),
(4, 3, 'Historial Académico Unificado', '/uploads/2026/trabajo/historial_100205.pdf'),
(5, 4, 'Historial Académico Unificado', '/uploads/2026/trabajo/historial_100206.pdf'),
(6, 4, 'Disponibilidad de Horarios', '/uploads/2026/trabajo/horarios_100206.pdf'),
(17, 18, 'Certificado Deportivo Avalado', '/uploads/2026/deporte/certificado_100207.pdf'),
(18, 18, 'Historial Académico Unificado', '/uploads/2026/deporte/historial_100207.pdf'),
(19, 19, 'Historial Académico Unificado', '/uploads/2026/excelencia/historial_100208.pdf'),
(20, 20, 'Historial Académico Unificado', '/uploads/2026/trabajo/historial_100209.pdf'),
(21, 20, 'Currículum Vitae Simplificado', '/uploads/2026/trabajo/cv_100209.pdf'),
(22, 21, 'Formulario Socioeconómico', '/uploads/2026/vivienda/formulario_100210.pdf'),
(23, 21, 'Certificado de Origen de Provincias', '/uploads/2026/vivienda/certificado_origen_100210.pdf'),
(24, 22, 'Historial Académico Unificado', '/uploads/2026/excelencia/historial_100211.pdf'),
(25, 23, 'Formulario Socioeconómico', '/uploads/2026/comedor/formulario_100212.pdf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id_estudiante` int(11) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `carrera` varchar(100) NOT NULL,
  `promedio_acumulado` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`id_estudiante`, `nombres`, `apellidos`, `carrera`, `promedio_acumulado`) VALUES
(100203, 'Carlos ', 'Mamani Quispe', 'Informatica', 78.50),
(100204, 'Ana Maria', 'Vargas Flores', 'Informatica', 85.20),
(100205, 'Juan Pablo', 'Condori Choque', 'Estadistica', 61.00),
(100206, 'Elena', 'Mendoza Ortiz', 'Ingenieria', 92.10),
(100207, 'Diego ', 'Quisbert Choque', 'Fisica', 55.40),
(100208, 'Gabriela Belen', 'Gutierrez Apaza', 'Quimica', 89.70),
(100209, 'Rodrigo Gonzalo', 'Vilca Condori', 'Informatica', 72.10),
(100210, 'Paola ', 'Torrez Pinto', 'Matematica', 67.80),
(100211, 'Omar', 'Flores Calle', 'Ingenieria', 94.50),
(100212, 'Vanessa Alexandra', 'Miranda Ticona', 'Matematica', 45.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `postulaciones`
--

CREATE TABLE `postulaciones` (
  `id_postulacion` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `id_beca` int(11) NOT NULL,
  `fecha_postulacion` date NOT NULL,
  `estado` varchar(20) DEFAULT 'Pendiente',
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `postulaciones`
--

INSERT INTO `postulaciones` (`id_postulacion`, `id_estudiante`, `id_beca`, `fecha_postulacion`, `estado`, `observaciones`) VALUES
(1, 100203, 1, '2026-02-10', 'Aprobado', 'Cumple con el perfil socioeconómico y el promedio mínimo requerido.'),
(2, 100204, 3, '2026-02-11', 'Aprobado', 'Promedio destacado. Postulación aceptada de forma inmediata.'),
(3, 100205, 2, '2026-02-12', 'Rechazado', 'No cumple con el promedio mínimo requerido para la Beca Trabajo (Mínimo 65).'),
(4, 100206, 2, '2026-02-13', 'Pendiente', NULL),
(18, 100207, 1, '2026-02-15', 'Aprobado', 'Representante destacado de la selección de Futsal.'),
(19, 100208, 3, '2026-02-16', 'Aprobado', 'Cumple con creces el requisito de excelencia académica.'),
(20, 100209, 2, '2026-02-16', 'Pendiente', 'Documentación completa. En espera de entrevista técnica.'),
(21, 100210, 5, '2026-02-17', 'Rechazado', 'No alcanza el promedio mínimo requerido para el subsidio de vivienda.'),
(22, 100211, 3, '2026-02-18', 'Pendiente', 'Pendiente de validación de cupos disponibles por carrera.'),
(23, 100212, 1, '2026-02-19', 'Rechazado', 'El promedio acumulado actual no alcanza el mínimo institucional de permanencia o postulación.');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `becas`
--
ALTER TABLE `becas`
  ADD PRIMARY KEY (`id_beca`);

--
-- Indices de la tabla `documentos`
--
ALTER TABLE `documentos`
  ADD PRIMARY KEY (`id_documento`),
  ADD KEY `fk_documento_postulacion` (`id_postulacion`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id_estudiante`);

--
-- Indices de la tabla `postulaciones`
--
ALTER TABLE `postulaciones`
  ADD PRIMARY KEY (`id_postulacion`),
  ADD KEY `fk_postulacion_estudiante` (`id_estudiante`),
  ADD KEY `fk_postulacion_beca` (`id_beca`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `becas`
--
ALTER TABLE `becas`
  MODIFY `id_beca` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `documentos`
--
ALTER TABLE `documentos`
  MODIFY `id_documento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `postulaciones`
--
ALTER TABLE `postulaciones`
  MODIFY `id_postulacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `documentos`
--
ALTER TABLE `documentos`
  ADD CONSTRAINT `fk_documento_postulacion` FOREIGN KEY (`id_postulacion`) REFERENCES `postulaciones` (`id_postulacion`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `postulaciones`
--
ALTER TABLE `postulaciones`
  ADD CONSTRAINT `fk_postulacion_beca` FOREIGN KEY (`id_beca`) REFERENCES `becas` (`id_beca`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_postulacion_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
