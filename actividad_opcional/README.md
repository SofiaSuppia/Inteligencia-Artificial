# Actividad Opcional 3 — EDA Heart Disease Dataset

## 1. Diccionario de variables

| Variable | Nombre real (UCI) | Significado en español |
|----------|-------------------|------------------------|
| `age` | age | **Edad** del paciente (en años) |
| `sex` | sex | **Sexo** (1 = hombre, 0 = mujer) |
| `cp` | chest pain type | **Tipo de dolor de pecho**: 1 = angina típica, 2 = angina atípica, 3 = dolor no anginal, 4 = asintomático |
| `trestbps` | resting blood pressure | **Presión arterial en reposo** (mmHg) al ingresar al hospital |
| `chol` | serum cholestoral | **Colesterol sérico** (mg/dl) — colesterol total en sangre |
| `fbs` | fasting blood sugar | **Glucemia en ayunas > 120 mg/dl** (1 = sí, 0 = no) — indicador de diabetes |
| `restecg` | resting electrocardiographic results | **Resultados del electrocardiograma en reposo**: 0 = normal, 1 = anomalía de onda ST-T, 2 = probable/definitiva hipertrofia del ventrículo izquierdo |
| `thalach` | maximum heart rate achieved | **Frecuencia cardíaca máxima alcanzada** durante la prueba de esfuerzo (latidos/min) |
| `exang` | exercise induced angina | **Angina inducida por el ejercicio** (1 = sí, 0 = no) — dolor de pecho que aparece al hacer esfuerzo |
| `oldpeak` | ST depression induced by exercise relative to rest | **Depresión del segmento ST** inducida por el ejercicio respecto al reposo, medida en el electrocardiograma |
| `slope` | the slope of the peak exercise ST segment | **Pendiente del segmento ST** en el pico del ejercicio: 1 = ascendente, 2 = plana, 3 = descendente |
| `ca` | number of major vessels colored by fluoroscopy | **Número de vasos sanguíneos principales coloreados por fluoroscopía** (0-3). Cada vaso coloreado indica una obstrucción arterial visible: 0 = sin vasos obstruidos, 3 = tres vasos afectados (enfermedad severa). Es **ordinal**. |
| `thal` | thallium stress test result | **Resultado de la prueba de esfuerzo con talio**: 3 = normal, 6 = defecto fijo, 7 = defecto reversible |
| `num` | diagnosis of heart disease | **Diagnóstico de enfermedad cardíaca** — grado de estrechamiento arterial: 0 = sin enfermedad (<50%), 1-4 = severidad creciente (>50%). Para el análisis se binarizó en `target`: 0 = "Sin enfermedad", 1-4 = "Con enfermedad" |
| `source` | base de origen | Base de datos de donde proviene el registro: Cleveland, Hungary, Switzerland o Long Beach VA (agregada al combinar las 4 bases) |

### Notas clave sobre valores que pueden (o no) ser 0

| Variable | ¿Puede valer 0? | Por qué |
|----------|-----------------|---------|
| `sex`, `fbs`, `exang`, `restecg` | **Sí** | 0 = "no", "ausencia" o "fem"/"masc" (valor legítimo) |
| `ca` | **Sí** | 0 = "ningún vaso afectado" (valor clínico válido) |
| `oldpeak` | **Sí** | 0 = sin depresión del ST (o incluso puede ser negativo = elevación) |
| `num` | **Sí** | 0 = sin enfermedad (<50% de estrechamiento) |
| `age`, `thalach` | **No** | Edad o frecuencia cardíaca 0 es imposible |
| `chol`, `trestbps` | **No** | Colesterol o presión 0 es fisiológicamente imposible → **error de registro** |

---

## 2. Resumen del trabajo realizado

- **Dataset**: 4 bases de UCI (id=45) combinadas → **920 registros**, 14 variables + `source`.
  - Cleveland: 303 · Hungary: 294 · Switzerland: 123 · Long Beach VA: 200.
  - Se cargaron manualmente los archivos `processed.*.data` porque `ucimlrepo` solo expone Cleveland.
- **Tratamiento de ceros inválidos (Opción A)**: `chol` (172 ceros) y `trestbps` (1 cero) convertidos a `NaN`.
- **Datos faltantes**: `ca` 66%, `thal` 53%, `slope` 34%, `chol` 22%. **Mecanismo MAR**: los faltantes se concentran por base de origen (`ca` ~96-99% en Hungary/Switzerland/VA vs 1% en Cleveland). Decisión: **no imputar**, documentar y trabajar con filas completas.
- **Outliers**: IQR → `trestbps` (27), `chol` (23), `oldpeak` (16); Z-score (|z|>3) confirma solo `trestbps` (7) y `chol` (8). No se eliminan: valores clínicamente plausibles.
- **Clasificación**: `ca` es **ordinal** (no continua), por eso se analiza por frecuencias y entropía, no con promedio.
- **Correlaciones más fuertes con el target**: `thalach` (−0.40), `oldpeak` (+0.39), `age` (+0.28). `chol` casi sin relación lineal (+0.12).
- **Sexo vs target**: 79% de la muestra es masculina; 63% de los hombres tiene enfermedad vs 26% de las mujeres.
- **Entropía**: target casi perfecta (0.99/1); `cp` es la más diversa (1.63), `fbs` la menos (0.65).

---

## 3. Guión de presentación (10 minutos)

### Slide 1 — Carátula (~1.5 min)
> "Buenas. Mi trabajo es un **análisis exploratorio de datos completo** del dataset *Heart Disease* de UCI (id=45). La clave del trabajo es que **no usé solo la base de Cleveland** (la única que expone `ucimlrepo`, 303 filas), sino que cargué las **4 bases originales**: Cleveland (303), Hungary (294), Switzerland (123) y Long Beach VA (200), **920 registros en total**, con 14 variables clínicas más el origen de cada registro."

> "Esa decisión — cargar las 4 bases — es lo que me permitió detectar el hallazgo principal del trabajo: el patrón de datos faltantes, que solo se ve cuando comparás una base con otra."

### Slide 2 — Características generales y datos faltantes (~4 min)
> "Primero, el dataset tiene dos características de composición: está **desbalanceado en sexo** (79% hombres) pero el **target está casi perfectamente balanceado** (55% con enfermedad, 45% sin); la entropía del target es 0.99 de 1 posible, lo que lo hace buen candidato para clasificación."

> "**Primer hallazgo — ceros inválidos:** variables continuas como `chol` y `trestbps` tenían **172 y 1 ceros** (imposibles: nadie tiene colesterol 0 mg/dl). Los convertí a `NaN` porque distorsionaban la media y la detección de outliers. Un detalle importante: `ca` tiene 0 y 611 faltantes, pero los **ceros de `ca` son válidos** (0 = ningún vaso afectado) y son **mutuamente excluyentes** de los faltantes (`?`). Por eso no se convierten."

> "**Segundo hallazgo — mecanismo de ausencia MAR:** `ca` falta en el **96-99%** de Hungary, Switzerland y Long Beach VA, pero solo en el **1.3% de Cleveland**. `thal` (53%) y `slope` (34%) siguen el mismo patrón. Como la probabilidad de faltar depende de la **base de origen**, que es una variable observada, el mecanismo es **MAR**, no aleatorio. Por eso apliqué la **Opción A: no imputé**; de hecho, imputar `ca` (66% de nulos) habría sido inventar más de la mitad de los valores."

### Slide 3 — Outliers, relaciones y conclusiones (~4 min)
> "**Outliers:** con el método **IQR**, `trestbps` tiene 27 outliers (2.9%) y `chol` 23 (2.5%). Con el **Z-score** (|z| > 3) quedan solo los extremos reales: `trestbps` 7 y `chol` 8. No los elimino: son pocos y probablemente valores clínicos reales (colesterol hasta 603 mg/dl). El boxplot anotado permite ver los cuartiles y los límites de decisión."

> "**Relaciones:** la variable que más correlaciona con la enfermedad es `thalach` (r = **−0.40**): quienes tienen enfermedad llegan a frecuencias cardíacas menores (128 lat/min promedio) vs los sanos (149). Le sigue `oldpeak` (r = **+0.39**). La correlación `age`-`trestbps` es positiva pero débil (0.25). Y en el gráfico de barras apiladas se ve algo contundente: **63% de los hombres tiene enfermedad vs 26% de las mujeres** — con la aclaración de que la muestra es 79% masculina, así que el dato puede reflejar sesgo de reclutamiento."

> "**Conclusión:** el principal desafío **no son las variables sino la calidad de los datos**: faltantes MAR estructurales, ceros inválidos y outliers. Para un modelo futuro recomiendo imputación **KNN/MICE** o **descartar `ca`/`thal`** por su alto porcentaje de faltantes."

### Cierre (~0.5 min)
> "En resumen: dataset completo (920 registros), tratamiento documentado de ceros inválidos, ausencia clasificada como MAR sin imputar, outliers detectados con IQR + Z-score, y las variables más informativas del diagnóstico son `thalach` y `oldpeak`."

---

## 4. Posibles preguntas del profesor y respuestas

**1. ¿Por qué no usaste `ucimlrepo` directamente?**
> Porque solo expone la base de Cleveland (303 registros), mientras que el dataset original de UCI son 4 bases tomadas con protocolos distintos. Cargué los archivos `processed.*.data` del zip para tener las 920 filas y así poder analizar el patrón de faltantes por base de origen.

**2. ¿Qué es `ca` y por qué la tratás distinto?**
> `ca` = número de vasos principales coloreados por fluoroscopía (0-3). Es **ordinal**, no continua: no tiene sentido calcular un promedio con decimales de "vasos coloreados". Por eso la saqué de las variables numéricas continuas, la analicé por frecuencias y la incluí en la entropía. Además sus 611 faltantes son `?` de 3 bases, mientras que sus ceros son valores clínicos válidos ("0 vasos afectados").

**3. ¿Por qué convertís los ceros de `chol` y `trestbps` a NaN y no los de `fbs` o `exang`?**
> Porque para `chol`/`trestbps` el valor 0 es fisiológicamente imposible (no existe colesterol o presión arterial 0), así que es un error de registro. En cambio `fbs`, `exang`, `restecg` y `ca` son binarias/ordinales donde 0 significa "no", "ausencia" o "ningún vaso": es un valor legítimo.

**4. ¿Por qué no imputaste los datos faltantes?**
> Porque el mecanismo es MAR y la ausencia es estructural: esas mediciones simplemente no se registraron en algunas bases. Imputar `ca` o `thal` (66% y 53% de nulos) habría inventado la mayoría de los valores. En un EDA descriptivo la Opción A de la cátedra es documentar, clasificar el mecanismo y no imputar.

**5. ¿Qué diferencia hay entre MCAR, MAR y MNAR?**
> - **MCAR**: la probabilidad de faltar no depende de nada, es aleatoria pura.
> - **MAR**: depende de **otras variables observadas**. Acá, de la base de origen (que sí conocemos).
> - **MNAR**: depende del **valor faltante en sí mismo** (p. ej., los pacientes más graves omiten el examen). Es el más difícil de manejar.
> Nuestro caso es **MAR** porque sabemos exactamente a qué base pertenece cada faltante.

**6. ¿Por qué no eliminaste los outliers de `chol` y `trestbps`?**
> El IQR marca 23 y 27 outliers, pero el Z-score solo confirma 8 y 7 como extremos estadísticos. Con 920 registros, la mediana no se distorsiona (colesterol con mediana 239.5). Además, en un dataset de pacientes cardíacos esos valores altos son clínicamente plausibles, así que los documenté pero no los borré. Eliminar datos reales sin justificación clínica es peor que conservarlos.

**7. ¿Cuál es la variable más importante para predecir la enfermedad?**
> Con correlación lineal respecto al target: `thalach` (−0.40), `oldpeak` (+0.39) y `age` (+0.28). Lo sorprendente es que `chol` casi no correlaciona (+0.12) con el diagnóstico, a pesar de ser la variable que más se asocia popularmente con el riesgo cardíaco. Esto se refuerza con los promedios por grupo: el colesterol entre enfermos (254) y sanos (240) difiere poco.

**8. ¿Por qué decís que el dataset está desbalanceado pero el target también?**
> Son dos cosas distintas:
> - El **target** está balanceado: 55% con enfermedad vs 45% sin → casi iguales.
> - La **composición por sexo** está desbalanceada: 79% hombres, y de ellos el 63% tiene enfermedad, mientras que solo el 26% de las mujeres la tiene.
> Ese contraste puede reflejar el sesgo de reclutamiento de los estudios originales (más hombres con sintomatología) y por eso lo aclaro antes de sacar conclusiones del gráfico.

**9. ¿Qué harías distinto en un próximo paso?**
> Para modelar, probaría primero imputación KNN o MICE en `ca`, `thal` y `slope`; si el modelo no mejora, los descartaría. Como benchmark usaría la base de Cleveland sola (la más completa, con <2% de nulos). También codificaría bien `slope` y `exang` como ordinales/binarias y evaluaría con validación cruzada y métricas como exactitud, sensibilidad y especificidad (importante porque el costo de un falso negativo clínico es alto).

**10. ¿Qué es el "mecanismo de ausencia" y por qué importa a quién imputa?**
> Determina si imputar introduce sesgo. Si es MCAR, imputar con la media no sesga. Si es MAR, hay que imputar condicionando a las variables observadas (por eso KNN/MICE). Si es MNAR, ninguna imputación simple corrige el sesgo, y quizás convenga modelar la ausencia o excluir la variable. Como acá es MAR y depende de `source`, cualquier imputación correcta debería considerar la base de origen.

**11. ¿Por qué `age` y `trestbps` correlacionan positivamente?**
> Porque a mayor edad, la rigidez arterial aumenta y la presión tiende a subir: es esperable fisiológicamente. La correlación (+0.25) es débil-moderada pero consistente con la literatura. Lo mismo pasa con `age`-`thalach` (−0.37): la frecuencia cardíaca máxima alcanzable baja con la edad.

**12. ¿Qué es la entropía de Shannon y qué concluís con ella?**
> Mide la incertidumbre/diversidad de una variable categórica: 0 = un solo valor (nada informativo), H_max = todos los valores igual de probables (máxima incertidumbre). Conclusión: el target tiene entropía casi máxima (0.99/1) → las clases están muy balanceadas. `fbs` tiene la más baja (0.65) → está muy sesgada hacia "no" (83% no supera 120 mg/dl).

**13. ¿Por qué usaste dos métodos de detección de outliers?**
> Porque se complementan. El **IQR** es robusto a la distribución (usa cuartiles) pero marca todo lo que sale de 1.5×IQR, incluso si es clínicamente plausible; el **Z-score** depende de la media y la desviación (sensibles a los propios outliers) y marca solo los muy extremos (|z|>3). Comparar ambos permite separar lo "estadísticamente atípico" de lo "extremo real": por eso reporté que el IQR marca más y el Z-score confirma solo una parte.

**14. ¿Cómo validaste que el notebook esté correcto?**
> Ejecuté el notebook completo de corrida con `nbconvert --execute` (kernel `.venv`, Python 3.10.12) y verifiqué que no hubiera errores, de la misma forma en que se corre en VS Code. Cualquier celda que falle se detecta en esa ejecución integral.

**15. ¿Qué diferencia hay entre el EDA anterior (`actividad_opcional2`) y este?**
> El anterior usaba solo Cleveland (303 filas). Este usa las **4 bases (920 filas)**, incorpora la **clasificación del mecanismo de ausencia (MAR)** con `nulos_por_grupo`, re-clasifica `ca` como **ordinal**, agrega **entropía de Shannon**, **outliers con IQR + Z-score** y un análisis de correlaciones más completo con máscara de redundancia. Es el EDA integral.