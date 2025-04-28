## Tarea 4.1

HEVC son las siglas de High Efficiency Video Coding y es la comercialización de la norma de compresión H.265 que sucede a la codificaión del asset-02 H.264/AVC. El códec HEVC es un 40% más eficiente que AVC, por lo que el usuario tendra buena calidad con un 40% más rápido y 40% de mejor calidad. En AWS lo resume en dos beneficios: HEVC es casi dos veces más eficiente que AVC y HEVC es compatible con 4K y procesamiento de alto rango dinámico [1].

Luego se ofrece una tabla multicomparativa [1]. La predicción intra en H.264 se hace en varias direcciones, varios patrones, 9 modos intra para 4 x 4; 9 para 8 x 8; y 4 para 16 x 16; mientras que en HEVC se hace con 35 modos para predicción intra, tamaño de predicción de 32 x 32, 16 x 16, 8 x 8 y 4 x 4. Los tipos de imagen codificada son I, B, P, SI, SP para H.264 y I,P,B para HEVC. La transformación es similar a DCT de enteros  8x8, 4x4; en HEVC se puede también con 32x32 y 16x16. EN HEVC el bloque de estimación de movimiento se hace por partición de árbol cuaternario jerárquico de 64x64 a 32x32,16x16 y 8x8 con 8 tipos de particionado por cada tamaño y no necesariamente cuadrada. En cambio en H.264 puede hacerlo con los bloques 16 x 16, 16 x 8, 8 x 16, 8 x 8, 8 x 4, 4 x 8 y 4 x 4. La entropía en H.264 se codifica con CABAC y tablas VLC CAVLC en HEVC se hace con CABAC. La distanccia entre cuadros para predicción es de hasta 16 cuadros de referencia anteriores o posteriores, incluidas referencias a largo plazo para H.264, mientras que para HEVC es de hasta 15 cuadros de referencia anteriores o posteriores, incluidas referencias a largo plazo. La estimación de movimiento fraccional con filtro de orden 6 de $\frac{1}{2}$ píxel; interpolación lineal de $\frac{1}{4}$ píxel; en HEVC filtro de orden 8 de $\frac{1}{4}$ píxel. Filtro en bulce es adaptativo de desbloqueo mientras que HEVC lo complementa con filtro adaptativo de compensación de muestra.

Como resumen se usa CTU de hasta 64x64 píxeles, predicción intraframe con 35 modos para optimizar la codificación espacial con subdivisión adaptativa de bloques, uso de CABAC, bitrate reducido un 50% con misma calidad y admite resoluciones UHD y 8K.

## Tarea 4.2

Para este ejercicio consulto los documentos de referencia: [2] [3].

Profile es el conjunto de herramientas de codificación y Level son los límites de parámetros técnicos: bitrate máximo, resolución máxima, etc. En H.264 los profiles conocidos son: baseline profile para un uso básico en videollamadas y entornos limitados; main profile que se optimiaz para streaming y broadcast; high profile que se usa en Blue-ray y 4K. El profile HEVC tiene: main profile con codificación de 8 bits y 4:2:0 chroma subsampling; main 10 profile que incorpora profundidad de color de 10 bits sobre el main; main still pricture profile que codifica imágenes estáticas.

| Nivel | Max bitrate (H.264/AVC) (kbps) | Max bitrate Main Tier (H.265/HEVC) (kbps) | Max bitrate High Tier (H.265/HEVC) (kbps) |
|-------|-------------------------------|------------------------------------------|------------------------------------------|
| 4.0   | 20,000                         | 12,000                                   | 30,000                                   |
| 4.1   | 50,000                         | 20,000                                   | 50,000                                   |
| 5.0   | 135,000                        | 25,000                                   | 100,000                                  |
| 5.1   | 240,000                        | 40,000                                   | 160,000                                  |
| 5.2   | 240,000                        | 60,000                                   | 240,000                                  |
| 6.0   | —                              | 60,000                                   | 240,000                                  |
| 6.1   | —                              | 120,000                                  | 480,000                                  |
| 6.2   | —                              | 240,000                                  | 800,000                                  |

## Tarea 4.3

Se indica en el campo Nievl de IDC en General/Básico donde se puede especificar el nivel de estándar.

## Tarea 4.4

Para H.264 se puede elegir: baseline, main, high, high10, high422, high444. Para H.265 ser puede elegir: main, mainstillpicutre

## Tarea 4.5

Mi asset-02 esta codificado como AVC. El factor de compresión hevc-70 respecto a asset-02 es $\approx 1.61$

## Tarea 4.6

`hevc-70.mkv`es 133 veces más pequeño que un clip de misma duración y resolución sin ninguna compresión. El factor de compresión respecto a un clip hipotético sería de $\approx 133.14$.

## Tarea 4.7

El factor de compresión con hevc-70 era de $\approx 1.61$ mientras que para hevc-40 es de $\approx 2.03$. el fichero hevc-40 tiene una mayor compresión porque se utiliza un bitrate objetivo más bajo que el original y Two Pass optimiza mejor la fistribución de bits. Aunque ha empeorado la fluidez de la grabación y la calidad en dinamismo. Esto es porque localmente elimina más bits y mantiene los más importantes.

## Tarea 4.8

Con GOP fijo a 30 se está imponiendo que se use un I-frame cada 30 frames sin posibilidad de adaptarse a la dinámica de la escena. Justo con esta configuración, en la escena dinámica que he grabado ha aumentado la fluidez, sin embargo, en escenas que fueran estáticas se estaría desperdiciando el potencial de compresión. Además, uno puede apreciar, por ejemplo, en los arboles que hay un efecto raro en las hojas con el movimiento de la cámara producido por la reorganización de bits no óptima localmetne por la rigidez de los GOP fijos. A nivel de compresión no ha afectado mucho. De hecho solo aumenta 0.1 MiB, pero esto, entiendo que es fruto de que la escena tiene mucho movimiento; si tuviera poco movimiento, podría verse una pérdida de capacidad de compresión.

## Referencias

[1] Codificación de video de alta eficiencia (HEVC). Amazon Web Services. (s. f.). Amazon Web Services, Inc. https://aws.amazon.com/es/media/tech/high-efficiency-video-coding/#:~:text=El%20c%C3%B3dec%20HEVC%20es%20alrededor,una%20calidad%20un%2040%20%25%20mejor.

[2] ITU-T. (2019a). High efficiency video coding.

[3] ITU-T. (2019b). ITU-T SERIES H: AUDIOVISUAL AND MULTIMEDIA SYSTEMS Infrastructure of audiovisual services-Coding of moving video. http://handle.itu.int/11.1002/1000/11830-en.