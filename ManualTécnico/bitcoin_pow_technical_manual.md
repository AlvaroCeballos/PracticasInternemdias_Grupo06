# Manual Técnico: Simulación de Blockchain y Proof of Work (PoW)
UNIVERSIDAD DE SAN CARLOS DE GUATEMALA  
FACULTAD DE INGENIERÍA

PRÁCTICAS INTERMEDIAS

TUTOR ACADÉMICO: Sergio Leonel Gomez Bravo

![](Aspose.Words.962ca6f9-2f25-42cf-9af8-00b8e68fd0ce.001.png)

**SECCIÓN:** D 

### Integrantes

| NOMBRE | CARNÉ |
| :--- | :--- |
| José Sebastian Pirir Romero | 202300335 |
| Jonathan Eliud Jerónimo Salguero | 202300353 |
| Yury Alexander Cruz García | 202300359 |
| Angel David Martinez Garcia | 202300410 |
| Francisco Gerardo Castillo Sagastume | 202300653 |
| Alvaro Gabriel Ceballos Gil | 202300673 |
| Julio Alfredo Herrera Orantes | 202300850 |

## 1. Introducción
El presente documento es un manual técnico que describe el funcionamiento del script `bitcoin_pow_demo.py`. Este código implementa de forma simplificada y educativa la estructura de una cadena de bloques (Blockchain) junto con el mecanismo de consenso **Proof of Work (PoW)**, el mismo concepto matemático y computacional que utiliza la red de Bitcoin para validar sus transacciones y asegurar la inmutabilidad de la información.

## 2. Objetivos
- **Comprender el algoritmo Proof of Work:** Demostrar cómo se usa el poder computacional ("minería") para resolver un puzzle criptográfico (encontrar un hash que cumpla con una dificultad específica).
- **Entender la inmutabilidad de Blockchain:** Ilustrar cómo cada bloque está criptográficamente enlazado al anterior, asegurando que cualquier alteración al historial invalida la cadena entera.
- **Desarrollar una base de conocimientos criptográficos:** Analizar el uso de la función hash SHA-256 para transformar datos arbitrarios en huellas digitales únicas.

## 3. Requisitos del Sistema
- **Lenguaje:** Python 3.6 o superior.
- **Librerías:** `hashlib` y `time` (ambas forman parte de la librería estándar de Python, no se requieren instalaciones de terceros).

---

## 4. Paso a Paso: ¿Cómo funciona el código?

El script se divide en varias funciones clave que interactúan entre sí para crear y validar la cadena de bloques.

### 4.1. Generación del Hash (`calculate_hash`)
Cada bloque de datos necesita ser resumido en un identificador único (Hash). 
```python
def calculate_hash(index: int, timestamp: float, data: str, previous_hash: str, nonce: int) -> str:
```
- **Proceso:** Concatena todos los valores relevantes del bloque (`index`, `timestamp`, `data`, `previous_hash`, `nonce`), los codifica en formato UTF-8, y les aplica el algoritmo **SHA-256**. El resultado es una cadena de texto hexadecimal de longitud fija.

### 4.2. Minería del Bloque - Proof of Work (`mine_block`)
Aquí es donde ocurre el esfuerzo computacional. 
- **La meta:** Generar un hash que empiece con una cantidad específica de ceros consecutivos definida por la variable `difficulty` (por defecto, 4 ceros: `0000...`).
- **El mecanismo (Nonce):** Dado que los datos de un bloque (índice, datos, timestamp, hash previo) son relativamente estáticos, la única forma de cambiar el hash resultante es alterando un número aleatorio llamado **Nonce** (Number used once).
- **El bucle:** El sistema entra en un bucle `while True` donde incrementa el `nonce` de 1 en 1, calculando un nuevo hash en cada intento, hasta que el hash generado cumple con la dificultad. A esto se le llama **minar un bloque**.

### 4.3. Validación de la Cadena (`is_block_valid` y `is_chain_valid`)
Para garantizar que la base de datos distribuida no haya sido hackeada ni corrompida:
- `is_block_valid`: Verifica que los datos internos correspondan con su propio hash, que el hash posea los ceros requeridos (dificultad) y que su firma previa coincida puntualmente con el bloque anterior.
- `is_chain_valid`: Recorre el blockchain desde el bloque génesis hasta la punta asegurándose de que la secuencia matemática permanezca intacta. Si un solo byte cambia en un bloque antiguo, todos los bloques posteriores quedan inmediatamente invalidados.

### 4.4. Función Principal (`main`)
Ejecuta la orquestación:
1. **Bloque Génesis:** Es el primer bloque de la red, su hash anterior suele ser todo ceros.
2. **Transacciones:** Muestra cómo se anexan transacciones simuladas (ej: "Alice paga 0.1 BTC a Bob") creando bloques subsecuentes.
3. Imprime por pantalla las estadísticas técnicas: Datos de creación, nonce ganador, el tiempo (en segundos) que costó minarlo y el estatus final de validez de la cadena.

---

## 5. Aplicaciones en el Mundo Real
Aunque este script es un prototipo básico, los conceptos detrás de él sustentan sistemas que manejan billones de dólares globalmente:
1. **Criptomonedas (Bitcoin):** Usan PoW idéntico para procesar transferencias de valor sin necesidad de bancos centrales.
2. **Identidad Digital y Registros Médicos:** Cadenas de bloques aplicadas para asegurar historiales médicos de forma inmutable.
3. **Cadenas de Suministro (Supply Chain):** Rastrear la historia y transferencia de productos físicos a lo largo de redes de distribución, donde nadie pueda borrar o manipular el historial logístico.
4. **Smart Contracts:** (Utilizados mayormente en redes como Ethereum) piezas de software que se autoejecutan cumpliendo garantías basadas en el estado inmutable de una cadena de bloques.

## 6. Conclusiones
El código `bitcoin_pow_demo.py` es una pieza educativa excepcional. Reduce la enorme complejidad técnica de un ecosistema descentralizado a sus principios matemáticos fundamentales:
- **La seguridad deriva del "trabajo duro" computacional.** Alterar un registro antiguo implica re-minar ese bloque y todos los subsiguientes antes de que la red avance, algo computacionalmente inviable.
- Se demuestra cómo tecnologías muy conocidas, como los hashes (SHA-256), sirven como pegamento estructural para conseguir consenso sin la necesidad de una autoridad central humana.