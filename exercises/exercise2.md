## Tarea 2.1

La resolución es $4096 \times 2160$ píxeles con $30.000$ FPS y una duración de $14.433$ segundos. Calculando igual que antes, el tamaño de fotograma es $26.542.080$. En este caso los fotogramas totales son $433$, por lo que el tamaño total del vídeo sin comprimir es de $11.492.720.640$ btyes o $11,49272064$ GB.

## Tarea 2.2

En MediaInfo la resolución y FPS son los mismos. La duración es de 14 segundos 433 ms, perfil `High@L5.2` con un submuestreo chroma 4:2:0 a 8 bits y un espacio de color BT.709. EL GOP es de M=3 y N=30 por lo que hay un P-frame cada 3 cuadros y un I-frame cada 30 cuadros, como en el vídeo anterior. Tiene escaneado progresivo y usa `CABAC` para la entropía.

## Tarea 2.3

En MediaInfo se indica que el tamaño real del asset-02 es de 133 MiB ($139.460.608$ bytes). Con la información del apartado 2.2 calculo que el factor de compresión es $\frac{11.492.720.640}{139.460.608}=82.40836466$. Por tanto, la compresión es de aproximandamente 82:1.

## Tarea 2.4

El primer fotograma es un `I-frame` mientras que el segundo fotograma es un `B-frame`. En este caso existen 15 cuadros tipo `I` distribuidos de manera regular en los segundos enteros $0,\,1,\cdots 14$. Sigue una estructura I, B, B, P, $\cdots$ I donde cada 30 frames aparece un I-frame (N=30) y cada 3 frames aparece un P-frame (M=3). 

## Tarea 2.5

Ciertamente, a pesar de que el `asset-02` tiene movimiento e incluso zoom, no hay diferencia en la configuración GOP. Hubiera pensado que al ser dinámico y no estático,  hubiera aparecido otra estructura con GOP más cortos. Podría suponer que el móvil a fin de mantener compresión o comaptibilidad, mantiene el estándar. También entiendo que lo puede hacer dado que se comparte mucho multimedia en reproducción y streaming en dispositivos móviles.