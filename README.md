<div align="justify">

  
# Product-space

En este proyecto se busca aplicar la metodología de Product Space propuesta por Hidalgo et al. (2007) para diversificación de productos de la Bioeconomía argentina.

# Sobre el uso de este repositorio

## Carpetas

- [data](./data/): carpeta para guardar los datos descargados -[raw](./data/raw)- y generados -[processed](./data/raw)- (crudos, pre-procesados y procesados).    
- [notebooks](./notebooks/): contiene las notebooks con el código y explicación de los análisis realizados correspondientes a cada paso de la investigación. 
- [figures](./figures/): carpeta para guardar los gráficos y visualizaciones generadas. 
- [references](./references/): se coloca toda la bibliografía consultada para el armado de este estudio.

## Fuentes de datos

### Datos de comercio 

* En el paper original se usan productos desagregados según la SITC revisión 4 a nivel de cuatro dígitos, de la base de datos de UNCOMTRADE. En este caso se utilizarán datos de [WITS](http://wits.worldbank.org/) provenientes de UNComtrade correspondientes al sistema armonizado (HS) a 4 dígitos para los años 1997 a 1999, 2007 a 2009 y 2017 a 2019. Se descargaron por partes los datos porque la consulta no puede exceder de 100 mil filas. Año por año se descargaron las exportaciones al Mundo a 4 dígitos del SA en dos grupos de países: con nombres de A a L (A_L) y M a Z (M_Z).
* Fecha de descarga: 15 de enero 2021. 
* Detalles de la consulta (query name: 4digproductspace) => ALL2 -- Heading (all 4-digit HS codes) HS 1996 (Selected Classification), Trade Flow Exports y Partners World -- WLD.

### Datos de clasificaciones (nomenclaturas) y correspondencias

- Las clasificaciones (nomenclatura) de **países** se extrajeron de UNComtrade. Corresponden a ISO3-digit. 
- Las clasificaciones (nomenclatura) de **productos** provienen de World Integrated Trade Solutions (WITS). Corresponden a datos a 4 dígitos del sistema armonizado para 1996 (HS1996 o H1)
- Las clasificaciones de **bienes pertenecientes a la bioeconomía** se extrajeron de Wierny et. al. (2015). En el ANEXO 2: Actividades consideradas para estimar la bioeconomía muestra la clasificación de las actividades según CIIU Rev3.
- Las tablas de **correspondencias entre CIIU Rev3 y HS1996** se descargaron de World Integrated Trade Solutions (WITS). Allí se ofrece información sobre diversas nomenclaturas de productos, lo que contribuye con el mapeo entre varias nomenclaturas distintas. En este caso se descargó la tabla de correlación o correspondencia entre el SA 1996 (o H1) y la ISIC (o CIIU por su sigla en español) Rev 3. En esta tabla los datos de productos del SA se encuentran a 6 dígitos por lo que se realiza un trabajo de conversión a nivel de partida para poder cruzar con los de comercio con que se está trabajando.
</div>
