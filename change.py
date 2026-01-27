import os
from PIL import Image

def optimizar_imagenes(directorio_entrada, directorio_salida, calidad=80):
    # Crear carpeta de salida si no existe
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    formatos_validos = ('.jpg', '.jpeg', '.png', '.bmp')

    for archivo in os.listdir(directorio_entrada):
        if archivo.lower().endswith(formatos_validos):
            try:
                ruta_completa = os.path.join(directorio_entrada, archivo)
                img = Image.open(ruta_completa)

                # 1. Convertir a RGB (necesario para JPEG/WebP si el original es RGBA/PNG)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # 2. Redimensionar proporcionalmente (Máximo 1920px de ancho/alto)
                max_size = 1920
                img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)

                # 3. Generar nuevo nombre con extensión .webp
                nombre_base = os.path.splitext(archivo)[0]
                ruta_salida = os.path.join(directorio_salida, f"{nombre_base}.webp")

                # 4. Guardar optimizado
                img.save(ruta_salida, "WEBP", quality=calidad, optimize=True)
                
                print(f"✅ Procesado: {archivo} -> {nombre_base}.webp")
            
            except Exception as e:
                print(f"❌ Error con {archivo}: {e}")

# Configuración de carpetas
carpeta_fotos = 'imagenes'  # Tu carpeta actual
carpeta_destino = 'imagenes_optimizadas'

optimizar_imagenes(carpeta_fotos, carpeta_destino)