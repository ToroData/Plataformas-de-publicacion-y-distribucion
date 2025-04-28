## Ejercicio 5

Hablaré del CDN de AWS ya que lo conozco mejor al tener la certificación de solutions architect. El objetivo del CDN es hacer que los recutsos sean accesibles con rapidez y fiabilidad para el usario final independientemente de su ubicación geográfica y, por tanto, independientemente de la ubicación de los servidores (centrales o distribuidos). Se puede optimizar la distribución, el almacenamiento (caché) y la codificación en función del dsipositivo y tipo de red y acceso.

En AWS el CDN se llama Amazon CloudFront y es un servicio gflobal que posibilita la entrega de contenido dinámico y estático. Por ejemplo: HTML, CSS, JS, imágenes o vídeos. Se pueden subir a un bucket de s3 y distribuirlos con una distribuirlos y cachearlos con CloudFront. Precisamente, las imágenes y vídeos de esta web que entrego para la PEC están hospedados en s3 y podría cachearlos con CloudFront. También se puede realizar streaming con HTTP Live Streaming HLS como podría ser el caso de Adobe Flash Media Server RTMP. También se pueden cachear recursos y distribución de aplicaciones interactivas con el objetivo siempre de reducri la latencia. En relación con la codificación se puede usar con Elastic Transcoder o MediaConverter para adaptar los clips de vídeo a distintas resoluciones y anchos de banda.

La distribución de contenido se hace sobre las ubicaciones de borde que comúnmente se referencian como edge locations. El objetivo es acercar los contenidos a la ubicación geográfica más proxima al usuario final para reducir la latencia, mejorar la velocidad de transferencia con cachés locales y mejorar la disponibilidad así como la redundancia. En un nivel superior, están las ubicaciones de borde regionales o regional edge caches. Estas son un nivel intermedio y soportan buckets de S3, EC2, ELB y HTTP servers tanto on-premise o de terceros. Por otra parte, se pued eintegrar con AWS Lambda@Edge para contenido dinámico personalizado, AWS WAF para integrar un firewall que protege contra DoS a las apps web y AWS Shield que es una capa mucho más avanzada de seguridad y cubre ataques tipo DDoS.

En relación con los costes, se paga por uso y tiene cargos asociados por la transferencia de datos hacia internet (varía por volumen y región); transferencia de datos de salida al origen; por el número de peticiones tipo HTTP/HTTPS por millón de solicitudes; tiene coste por invalidaciones de objetos superada la capa gratis; SSL personalizadas de IP dedicada y otros servicios asociados como field-level encrypation o métricas.

A nivel de limitación se debe comentar que el RTMP solo se pude hacer desde s3 no desde orígenes personalizas; el bloqueo geográfico se puede hacer por país pero no por subregiones más acotadas; se pueden incurrir en grandes costes si el TTL no se configura bien en aplicaciones que se actualiza mucho los contenidos cacheados y se dejan contenidos obsoletos en caché; además, las operaciones de invalidación de objetos cacheados demora unos minutos hasta que tiene efecto.

## Referencias

[1] AWS. (2025). Amazon CloudFront Developer Guide. https://docs.aws.amazon.com/pdfs/AmazonCloudFront/latest/DeveloperGuide/AmazonCloudFront_DevGuide.pdf

[2] Características clave de una red de entrega de contenido – Rendimiento, seguridad – Amazon CloudFront. (s. f.). Amazon Web Services, Inc. https://aws.amazon.com/es/cloudfront/features/?nc=sn&loc=2&whats-new-cloudfront.sort-by=item.additionalFields.postDateTime&whats-new-cloudfront.sort-order=desc

[3] CDN de Amazon CloudFront - Planes y precios - Probar de forma gratuita. (s. f.). Amazon Web Services, Inc. https://aws.amazon.com/es/cloudfront/pricing/?nc=sn&loc=3 

[4] Introducción a Amazon CloudFront. (s. f.). [Vídeo]. Amazon Web Services, Inc. https://aws.amazon.com/es/cloudfront/getting-started/?nc=sn&loc=4