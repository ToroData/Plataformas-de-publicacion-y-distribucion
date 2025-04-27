## Tarea 3.1

Se acepta una codificación MPEG-2 en los DVD. Para la resolución de $720 \times 576$ para PAL se exige 25 FPS y una relación 16:9 o 4:3 [1]. Si el cliente hubiera querido Blu-ray se aceptaría usar el códec por default de la grabación, es decir, H.264/AVC, además, podría usar H.265 HEVC [2] o por cuestión de retrocompatibilidad con las primeras versiones, se puede usar MPEG-2 [3]. LAs relaciones pueden ser de 720p, 1080p como estándar y 4K para Blu-ray ultra HD con HEVC.

## Tarea 3.2

El vídeo se ha grabado en 30 FPS por lo que se debe reducir a 25 FPS para cumplir con el estándar PAL y tener compatibilidad con DVD. Se debe usar el filtro de Cambiar FPS —situado en el lateral de la aplicación— para adaptar la velocidad de los fotogramas.

## Tarea 3.3

El tamaño de fotograma nuevo sería de $720 \times 576 \times 3=1.244.160$. El número de fotogramas sería $25 \times 14.433=360.825$. Multiplicando los fotogramas por bytes/fotograma se obtiene un tamaño sin comprimir de $448.924.032$ bytes o $448.92$ MiB. He consultado el tamaño de `pec2_dvd.mpg` en MediaInfo y opcupa 12.7 MiB (Fig. 1). Por tanto, el factor de compresión es $\frac{448.92}{12.7} \approx 35.35$; un factor aproximado de  33.7:1. En el apartado 2.3 se comentó que había un factor de aproximadamente el 82:1 lo que muestra que la compresión MPEG-2 para DVD es menos eficiente que la compresión actual H.264/AVC. Esto se debe a que no exprime la codificación de entropía o la técnica de predicción.

## Tarea 3.4

El tamaño de GOP es N y, por tanto, hay que marcar 8; correpsonde al número de frames entre dos I-frames. El número de fotgramas B son la cantidad de B-frames entre `I` y `P` o `P` y `P`. Por tanto sería, $M-1=1$.

Número de fotogramas = 1
Tamaño de GOP = 8

## Tarea 3.5

Consultando el tamaño del archivo en MediaInfo veo que es de 13.1 MiB, con el cálculo de la tarea 3.3 se obtiene un factor de compresión $\frac{448.92}{13.1}\approx 34.267$; un factor 34.3:1. Ahora, la compresión es menos eficiente dado que se ha disminuido la longitud del GOP, por tanto, se da menos espacio a la compresión con pérdida.

## Tarea 3.6

La nueva exploración que propongo es usar un GOP de 15 y un M=3, por tanto el número de fotogramas B será de 2. La duración actual es de 17s 320ms (Fig. 2), siguiendo el mismo proceso de cálculo que las anteriores ocasiones obtengo un resultado de $528.768.000$ bytes o $528.77$ MiB. El tamaño actual es de 12.8 MiB por lo tanto la compresión que se obtiene es un factor 41.3:1; $\frac{528.77}{12.8}=41.31$. Esto, efectivamente, confirma el análisis del apartado anterior, en el sentido que la estructura de un GOP más largo maximiza la predicción interframe y permite obtener un mayor factor de compresión que con un GOP corto. Aunque el estándar PAL actual con el GOP propuesto está bastante comprimido, sigue siendo mucho menos eficiente que las versiones que se usarían con Blu-ray.

## Referencias

[1] Hernández, L. (2025, 9 marzo). Qué diferencia hay entre DVD video NTSC y PAL. Sonilec. https://sonilec.mx/que-diferencia-hay-entre-dvd-video-ntsc-y-pal/

[2] H.264 y H.265 - AVC y HEVC - ¿Cuál es la diferencia? (2024, 22 enero). Flussonic. https://flussonic.com/es/blog/news/h264-vs-h265/

[3] colaboradores de Wikipedia. (2025, 9 abril). Disco Blu-ray. Wikipedia, la Enciclopedia Libre. https://es.wikipedia.org/wiki/Disco_Blu-ray
