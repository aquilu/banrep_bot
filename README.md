# Asistente Virtual sobre El Banco de la República

Este bot interactivo fue creado para ayudar a los usuarios a obtener información sobre la historia del Banco de la República.
El bot es entrenado y alimentado con el contenido del documento https://babel.banrepcultural.org/digital/collection/p17054coll18/id/413
## Instalación

1. Clone este repositorio.
2. Instale las dependencias utilizando `pip install -r requirements.txt`.
3. Ejecute `streamlit run app.py` para iniciar la aplicación.

## Uso

Simplemente escriba su pregunta en el campo de entrada y el bot proporcionará una respuesta basada en el contenido entrenado.

## Nota Importante

El archivo `banrep.md` en la carpeta `banrep_content` se proporciona solo para referencia y entender cómo se generaron los índices en `faiss_index`. No es necesario para el funcionamiento del bot, ya que los índices en `faiss_index` ya representan el contenido de este archivo.

## Contribuir

Las contribuciones son bienvenidas. Siéntase libre de abrir un issue o crear un pull request.
By halbarba
