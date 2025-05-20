# H-Index

Este proyecto proporciona una solución para calcular el **Índice H** de un investigador, una métrica clave que evalúa su impacto académico.

## ¿Qué es el Índice H?

El Índice H es un número `h` tal que un investigador tiene `h` publicaciones, cada una con al menos `h` citas. Mide tanto la productividad como la influencia del trabajo de un científico.

## Lógica de la Solución

La solución se basa en un enfoque eficiente de ordenamiento y verificación:

1.  **Ordenar Citas Descendentemente:** Las citas de todas las publicaciones se ordenan de mayor a menor. Esto es fundamental para identificar rápidamente el impacto de las publicaciones más citadas.
2.  **Iterar y Verificar:** Se recorre la lista de citas ordenada. En cada paso:
    * Se determina cuántos artículos se han considerado hasta ese momento (`num_articles`).
    * Se compara el número de citas de la publicación actual (`num_citations`) con `num_articles`.
        * Si `num_citations >= num_articles`: Este `num_articles` es un candidato válido para el Índice H. Se guarda el valor más alto que cumpla esta condición.
        * Si `num_citations < num_articles`: Como la lista está ordenada, las publicaciones subsiguientes no cumplirán la condición. La búsqueda se **detiene** en este punto.
3.  **Resultado Final:** El último valor guardado es el **Índice H** del investigador.