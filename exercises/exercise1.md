## Tarea 1.1

En la figura 1, se pueden ver los detalles del asset-01 usado en la tarea 1. Como se puede apreciar el códec del vídeo es `H.264` o `MPEG-4 AVC` (2003) [1]. Es un estándar de compresión con pérdidas más usado actualmente y se usa en streaming, Blu-ray, HLS, etc. El formato de compresión por pérdidas elimina la información irrelevante del vídeo sin afectar la calidad de este. Particularmente se reducen los detalles entre frames, se aplica una predicción de movimiento (filtro de orden 6 de $\frac{1}{2}$ píxel y interpolarización lineal de cuarto de píxel) y se usa cuantización. Se usa la transformada discreta de coseno para optimizar espacialmente los bloques de píxeles y codificación de entropía avanzada. Específicamente, codificación aritmética binaria adaptativa al contexto —CABAC— y tablas de VCL adaptativas al contexto —CAVCL.

## Tarea 1.2

Tiene $4096 \times 2160$ píxeles por fotrograma que corresponde con el estándar 4K DCI. Tiene $30.000$ FPS y una duración de 13 segundos. Hay $4096 \times 2160=8.847.360$ píxeles por fotograma. Teniendo en cuenta que cada píxel de color son 3 bytes se obtiene $26.542.080$ bytes por fotograma. Ahora bien, son 30 FPS con una duración de 13 segundos multiplicado por el tamaño del fotograma se obtiene $10.351.411.200$, es decir, 10.35 GB.

## Tarea 1.3

En la Figura 1, se visualiza que la tasa promedio de bits es de $79,390$ kbps, es decir, $79.390.000$ bps o (dividiendo por 8) $9.923.750$ bytes/s. De lo cual se deduce que dado 13 segundo el el resultado es $129.008.750$ bytes que corresponden a 129 MB. Por tanto, el factor de compresión resultará en $\frac{10.351.411.200}{129.008.750}=80.23805517$ aproximadamente 80:1.

## Tarea 1.4

El contenedor multimedia es un `.mp4`. Basándome en la tabla 3, sí que el estándar del contenedor `MPEG-4 parte 14` es compatible con el códec `H.264`.

## Tarea 1.5

El primer fotograma es un `I-frame`. El intracode tiene toda la información disponible de la imagen; no tiene referencia a otros fotogramas. En cambio, el segundo frame es de tipo `B-frame`, es decir, bidireccional predictivo. Este tipo usa la imagen I del primer frame y otra posterior P situada en el cuarto frame para deducir la imagen intermedia B. Contiene una estimación de movimiento con calidad más baja, pero alta compresión [p.52, 1].

## Tarea 1.6

Existen 13 cuadros tipo `I` distribuidos de manera regular en los segundos enteros $0,\,1,\cdots 12$. Esto cuadra con el hecho de que el clip tiene una duración total de 13 segundos y una tasa de 30 FPS. Por tanto, cada 30 frames aparece un nuevo I-frame. Además, como la escena es prácticamente estática no debe introducir más I-frames.

## Tarea 1.7

Sigue una estructura I, B, B, P, $\cdots$ I. Como he comentado cada 30 fotogramas entra un I-frame. Los 30 fotogramas se componen mayoritariamente de mucha compresión tipo B y predictivas P.

## Tarea 1.8

El problema que se plantea es que si se corta en un frame que no es `I` entonces se está seccionando por un fotograma que no contiene toda la información de la imagen. En en la [quickstart de Avidemux](https://www.avidemux.org/admWiki/doku.php?id=using:quickstart) se puede leer precisamente lo que he explicado anteriormente, pero además, añade el hecho de que si cortas por un punto intermedio deberías recodificar. Por tanto, se debe tener en cuenta el GOP a fin de evitar saltos en los puntos d ecorte y asegurar la calidad del clip.

## Tarea 1.9

En la Figura 2, he dejado el detalle que he explorado en MediaInfo. Veo que el contenedor en MediaInfo se detecta como `MPEG-4 (Base Media / Version 2)` mientras que en Avidemux se detectaba com `.mp4`. También el códec se detecta como `AVC` profile `High@L5.2`. Las resoluciones, fps, espacio de colores y profundidad,  son idénticas. En MediaInfo aparece más información como el perfil del codec que dice que es High en el nivel 5.2. Especifica el tipo de cabecera de compresión `CABAC / 4 Ref Frames`. También especifica el GOP que es M=3 y N=30. Es decir, cada tercer frame es un P-frame y son 30 cuadros. El muestreo es profresivo. 

## Referencias

[1] Ribelles García, A. (2022). Codificación y distribución PID_00288025.
