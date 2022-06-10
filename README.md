# Base de datos de todos los centros educativos  españoles con su respectivo e-mail.

Los datos del [listado de colegios](Listado.xls) han sido obtenidos del registro estatal de [Centros Docentes no Universitarios (RCD)](https://www.educacion.gob.es/centros/home.do).
Los correos electronicos se han obtenido de la pagina web [buscocolegio.com ](https://www.buscocolegio.com/) mediante web scrapping y el mismo resultado se puede obtener siguiendo los pasos del codigo [extrar_colegios.py](extraer_colegios.py). La base de datos esta disponible en [csv](listado_emails.csv) y [xlsx](listado_emails.xlsx). 

Para un total de 3178 colegios el email no estaba disponible. 

Los datos se consultaron el 10/06/2022

Aqui se puede observar una previsualizacion de las primeras 10 filas de la base de datos:
| Provincia   | Localidad   | Denominación genérica                    | Denominación específica   |   Código | Naturaleza     | Domicilio                          |   C. Postal |   Teléfono | email                            |
|:------------|:------------|:-----------------------------------------|:--------------------------|---------:|:---------------|:-----------------------------------|------------:|-----------:|:---------------------------------|
| Almería     | Abla        | Centro de Educación de Adultos           | Abla                      |  4501032 | Centro público | Santos Mártires, s/n               |        4510 |  950359522 | registro@abla.es                 |
| Almería     | Abla        | Colegio de Educación Infantil y Primaria | Joaquín Tena Sicilia      |  4000018 | Centro público | San Segundo,  7                    |        4510 |  950359901 | 04000018.edu@juntadeandalucia.es |
| Almería     | Abla        | Escuela Infantil                         | Abla                      |  4009435 | Centro público | San Segundo, 3                     |        4510 |  950351032 | 04009435.edu@juntadeandalucia.es |
| Almería     | Abrucena    | Colegio de Educación Infantil y Primaria | Antonio Relaño            |  4000021 | Centro público | Balsillas, 36                      |        4520 |  950359902 | 04000021.edu@juntadeandalucia.es |
| Almería     | Adra        | Centro de Educación de Adultos           | Mediterráneo              |  4500234 | Centro público | Marisma, 6                         |        4770 |  950579500 | 04500234.edu@juntadeandalucia.es |
| Almería     | Adra        | Centro Privado de Educación Infantil     | Chispas                   |  4011351 | Centro privado | San Nicolás, 3, Bajo C             |        4770 |  637729674 | ceas@colegioarturosoria.org      |
| Almería     | Adra        | Centro Privado de Educación Infantil     | Había una vez             |  4011132 | Centro privado | de Málaga, esquina con C/ Baleares |        4770 |  659915943 | ceas@colegioarturosoria.org      |
| Almería     | Adra        | Centro Privado de Educación Infantil     | La Casita de Fresa        |  4011296 | Centro privado | Buenavista, 54                     |        4770 |  622553248 | ceas@colegioarturosoria.org      |
| Almería     | Adra        | Centro Privado de Educación Infantil     | Mi Primer Cole            |  4011247 | Centro privado | del Mediterráneo, 70               |        4770 |  677775242 | ceas@colegioarturosoria.org      |
| Almería     | Adra        | Centro Privado de Educación Infantil     | Mundo Mágico              |  4010358 | Centro privado | Araucaria, local 4-A               |        4770 |  672297282 | direccion@eimundomagico.es       |
