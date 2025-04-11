CREATE DATABASE ExploracionEspacial;

USE ExploracionEspacial;

CREATE TABLE AgenciaEspacial (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Pais VARCHAR(50),
    FechaCreacion DATE
);

INSERT INTO AgenciaEspacial (ID, Nombre, Pais, FechaCreacion) VALUES
(1, 'Administración Nacional de Aeronáutica y el Espacio (NASA)', 'Estados Unidos', '1958-07-29'),
(2, 'Corporación Espacial Estatal (Roscosmos)', 'Rusia', '1992-02-25'),
(3, 'Administración Espacial Nacional China (CNSA)', 'China', '1993-04-22');
