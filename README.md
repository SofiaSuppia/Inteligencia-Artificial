# Inteligencia Artificial

> Repositorio personal de estudio y práctica de **Inteligencia Artificial**.

## Sobre este repositorio

Acá voy reuniendo ejercicios, notebooks, ejemplos de código y recursos en Python que uso para practicar y ordenar el material de la materia. El contenido está organizado en carpetas numeradas (`00_...`, `01_...`, etc.), una por unidad temática, y se puede ir ampliando a medida que avance el estudio.

## Contenido publicado

- [Clase 1 - Introducción a Python](01_introduccion_python/)
- [Clase 2 - Introducción al análisis de datos](02_introduccion_analisis_datos/)
- [Clase 3 - Análisis exploratorio de datos (EDA)](03_analisis_exploratorio_datos_eda/)

## Material complementario

- [`material_complementario/`](material_complementario/) — notebooks y ejercicios de repaso de Python, NumPy, Pandas, Matplotlib y Seaborn. No es parte del temario de la materia ni sigue la numeración de clases.

## Organización del repositorio (branches y tags)

- Todo el material vive en la rama `master`. No hay otras ramas de desarrollo: el material se mantiene allí de forma centralizada.
- A medida que agregue nuevo contenido, se pueden ir actualizando los notebooks y recursos sobre `master`. Para tener todo al día, hace `git pull` periódicamente.
- Si quiero congelar una versión del estado del repositorio en un momento dado, puedo crear un **tag** (por ejemplo `v1.0`, `2026`). Así queda una referencia fija del material en ese punto.
- Si quiero volver a un tag anterior, ubicarme en el estado correspondiente:

  ```bash
  git fetch --tags
  git checkout tags/2025
  ```

## Quick start

### Prerrequisitos

- Git
- [uv](https://docs.astral.sh/uv/getting-started/installation/) — ver cómo instalarlo abajo

### 1. Instalar uv (si no lo tenés)

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux/Mac:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

No hace falta tener Python instalado de antemano: uv descarga la versión que le pidas.

### 2. Clonar el repositorio

```bash
git clone https://github.com/SofiaSuppia/Inteligencia-Artificial.git
cd Inteligencia-Artificial
```

### 3. Crear el entorno virtual

```bash
uv venv --python 3.11
```

### 4. Activar el entorno

**Windows (PowerShell):**

```bash
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### 5. Instalar dependencias

```bash
uv pip install -e .
```

### 6. Registrar el kernel en Jupyter

```bash
python -m ipykernel install --user --name=inteligencia-artificial --display-name "Python (IA)"
```

### 7. Abrir Jupyter y ponerse a trabajar

```bash
jupyter notebook
```

Al abrir una notebook, elegí el kernel **"Python (IA)"** desde **Kernel → Change Kernel**.

### Mantenerse actualizado

Cada vez que se publique material nuevo, alcanza con traer los cambios:

```bash
git pull
```

Si se agregan dependencias nuevas a `pyproject.toml`, volvé a correr `uv pip install -e .` para instalarlas.

## Problemas comunes

**`uv: no se reconoce como un comando` después de instalarlo**
El instalador agrega `uv` al PATH, pero las terminales que ya estaban abiertas no se enteran. Cerrá la terminal y abrí una nueva. Si no querés reabrirla, en esa misma sesión de PowerShell corré:

```powershell
$env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
```

**`.venv\Scripts\activate` falla con un error de "execution policy" en PowerShell**
Windows por defecto no deja correr scripts `.ps1`. Habilitalo solo para esa sesión:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

o activá el entorno desde `cmd.exe` en vez de PowerShell:

```bash
.venv\Scripts\activate.bat
```

**El kernel "Python (IA)" no aparece en Jupyter**
Confirmá que el entorno esté activado antes de registrar el kernel (paso 6 del Quick start) y volvé a correr el comando. Si seguís sin verlo, reiniciá Jupyter (cerrá y volvé a correr `jupyter notebook`).

**`uv pip install -e .` dice que no encuentra el entorno / instala en el Python global**
Es porque el `.venv` no está activado. Activalo (paso 4) y volvé a instalar; se nota porque el prompt de la terminal empieza con `(.venv)`.

**VS Code no encuentra las librerías instaladas**
El editor puede seguir usando otro intérprete de Python. Con la notebook o un `.py` abierto, elegí manualmente el intérprete: `Ctrl+Shift+P` → **Python: Select Interpreter** → el que apunta a `.venv`.

## Bibliografía recomendada

**Libro principal:**

- *Artificial Intelligence: A Modern Approach* — Stuart Russell, Peter Norvig (Ed. Pearson)

**Otros recursos útiles:**

- *Artificial Intelligence Basics: A Non-Technical Introduction* — Tom Taulli (Ed. Apress)
- *Artificial Intelligence For Dummies* — John Paul Mueller, Luca Massaron
- [*An Introduction to Statistical Learning*](https://www.statlearning.com/) — Gareth James et al. (Ed. Springer)
- [*Python Data Science Handbook*](https://jakevdp.github.io/PythonDataScienceHandbook/) — Jake VanderPlas
- *The Elements of Statistical Learning* — Trevor Hastie et al. (Ed. Springer)

## Contacto

Para consultas o mejoras, usar los issues del repositorio o el canal que prefiera usar para este proyecto.

## Licencia

Este material está bajo una licencia [Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es). Podés compartirlo y adaptarlo dando crédito, siempre que no sea con fines comerciales y que compartas cualquier adaptación bajo la misma licencia. Ver el archivo [LICENSE](LICENSE).

---

**Notas personales de Inteligencia Artificial.**