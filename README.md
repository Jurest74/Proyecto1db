# Proyecto 1 - Bases de datos distribuida

## Integrantes

-   Juan Diego
-   Santiago Aguirre
-   Ricardo Gottheil

# Proceso de instalación y ejecución

En este proyecto estamos usando PIPENV para manejar un entorno virtual de python. Para instalar lo, se necesita tener python en la versión 3 y pip instalado.

Teniendo encuenta lo anterior, se deben seguir los siguientes pasos:

### **1. Instalación de PIPENV**

Utilizando pip, instaremos PIPENV uusando el siguiente comando:

```bash
pip install pipenv
```

### **2. Instalación del ambiente de python**

En el directorio raiz, debemos ejecutar el comando:

```bash
pipenv install
```

### **3. Instalando dependencias dentros del ambiente que se ha creado**

Si usamos **VS CODE** solo abrir, y esperar a que detecte el ambiente de desarrollo que hemos creado con PIPENV.

Si en dado caso, no es detectado por **VS CODE**, ejecutar el siguiente comando:

```bash
pipenv shell
```

Una vez activado el ambiente de desarrollo, debemos ejecutar el siguiente comando desde la carpeta raiz del proyecto:

```bash
pipenv run pip install -r requirements.txt
```

### **4. Ejecución del proyecto**

Para ejecutar el proyecto, nos debemos mover a la carpeta main ( `cd main` ) y ejecutar el comando:

```bash
uvicorn main:app
```

Si se necesita que se reinicie el servidor cada vez que se haga un cambio, usar:

```bash
uvicorn main:app --reload
```

---

## Eliminación del entorno de desarrollo

Al finalizar el proyecto si ya no se va a trabajar más en el mismo, usar el siguiente comando desde la carpeta raiz del proyecto:

```bash
pipenv --rm
```
