# CotizaVentanas

**CotizaVentanas** es un programa desarrollado para calcular el costo de ventanas de aluminio de acuerdo con las especificaciones proporcionadas. El sistema considera los estilos de ventana, acabados de aluminio, tipos de vidrio y esmerilado, y aplica descuentos por grandes cantidades de pedido.

## Estructura del Proyecto

El proyecto está organizado en la siguiente estructura de directorios y archivos:
CotizaVentanas/ │ ├── app/ │ ├── docs/ │ ├── venv/ # Entorno virtual │ ├── main.py │ ├── .gitignore ├── README.md └── requirements.txt

### Archivos Principales

- **`app/main.py`**: Archivo principal que ejecuta el programa. Solicita al usuario la entrada de datos y calcula el costo total de las ventanas.
- **`app/nave.py`**: Define la clase `Nave`, que representa un panel dentro de una ventana y contiene métodos para calcular el perímetro y el área del vidrio.
- **`app/ventana.py`**: Define la clase `Ventana`, que utiliza la clase `Nave` para calcular los costos del acabado, vidrio, y otras partes de la ventana.

## Requisitos

El proyecto requiere Python 3.8 o superior. Para instalar las dependencias necesarias, sigue estos pasos:

1. **Clonar el Repositorio**:

   ```bash
   git clone https://github.com/anderson6069/CotizaVentanas.git
    ```
2. **Navegar al Directorio del Proyecto**:

    ```bash 
    cd CotizaVentanas
    ```
3. **Crear un Entorno Virtua**:

```bash 
python -m venv venv
```
4. **Activar el Entorno Virtual**:

```bash 
 source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows
```
5. **Instalar Dependencias**
```bash 
pip install -r requirements.txt
```

## Ejecución del Programa

Para ejecutar el programa, sigue estos pasos:

1. **Navegar al Directorio CotizaVentanas**:
```bash 
cd CotizaVentanas
```
2. **Ejecutar el Archivo main.py**:
```bash 
cd python main.py
```

## Uso del Programa

El programa solicitará al usuario los siguientes datos:
- Ancho de la ventana (cm): Ingresa el ancho de la ventana en centímetros.
- Alto de la ventana (cm): Ingresa el alto de la ventana en centímetros.
- Estilo de la ventana (O, XO, OXXO): Selecciona el estilo de la ventana.
- Tipo de acabado (Pulido, Lacado Brillante, Lacado Mate, Anodizado): Selecciona el tipo de acabado para el aluminio.
- Tipo de vidrio (Transparente, Bronce, Azul): Selecciona el tipo de vidrio.
- ¿El vidrio tiene esmerilado? (sí/no): Indica si el vidrio tiene esmerilado adicional.
- Cantidad de ventanas: Ingresa la cantidad de ventanas a calcular.
- El programa calculará y mostrará el costo total para la cantidad de ventanas ingresadas.

## Archivo .gitignore

El archivo .gitignore está configurado para excluir archivos y directorios no necesarios, como el entorno virtual y archivos de compilación. Asegúrate de revisar este archivo para cualquier ajuste adicional.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.