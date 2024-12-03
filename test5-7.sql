/*5 Generar una query de SQL que muestre la siguiente información, los nombres que tengan un
height arriba de 180 pero menor a 190, que cumplan la condición de ser male y el hair_color
sea cualquiera menos “none”*/

SELECT name FROM testdata.data_union
WHERE height BETWEEN 180 AND 190 AND sex = 'male' AND hair_color!='none';

/*6 Por medio de una sentencia SQL generar la siguiente bandera:
1 <-> el mass está arriba del promedio
0 <-> el mass es menor igual al promedi
*/
SELECT 
    name, 
    mass,
    CASE 
        WHEN mass > (SELECT AVG(mass) FROM data_union) THEN 1 
        ELSE 0 
    END AS bandera
FROM 
    data_union;

/*Pregunta 6 también puedo crear una VIEW*/
CREATE VIEW mass_flat AS
SELECT 
    name, 
    mass,
    CASE 
        WHEN mass > (SELECT AVG(mass) FROM data_union) THEN 1 
        ELSE 0 
    END AS bandera
FROM 
    data_union;
    
SELECT * FROM mass_flat;

/*7 Calcular la altura promedio, la altura máxima y mínima por especie, mediante una sentencia SQL*/
SELECT 
    species,
    AVG(height) AS altura_promedio,
    MAX(height) AS altura_maxima,
    MIN(height) AS altura_minima
FROM 
    data_union
GROUP BY 
    species;


    /*Pregunta 2*/
    SELECT DISTINCT starships FROM data_union;

    /*Pregunta 3*/
    SELECT COUNT(*),skin_color,eye_color FROM data_union group by skin_color, eye_color;

    /*Pregunta 4*/
    SELECT name, COUNT(*) AS cantidad_duplicados
    FROM data_union
    GROUP BY name
    HAVING COUNT(*) > 1;