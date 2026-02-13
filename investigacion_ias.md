# Investigación: IAs Gratuitas para Resúmenes de Registros Extensos

Esta investigación se centra en identificar herramientas y modelos de IA que permitan procesar y resumir grandes volúmenes de texto (registros, logs, documentos extensos) sin costo.

## 1. Herramientas Web Gratuitas (SaaS)

| Herramienta | Límite Aproximado | Idiomas | Registro Req. | Características Clave |
| :--- | :--- | :--- | :--- | :--- |
| **Decopy AI** | Alto (PDF/Video) | Multilingüe | No (Básico) | Resúmenes precisos, puntos clave y mapas mentales. |
| **QuillBot** | ~600-1200 palabras* | Multilingüe | Opcional | Modos "Oraciones clave" y "Párrafo". Muy intuitivo. |
| **Resoomer** | Ilimitado (Texto) | Multilingüe | No | Filtra ideas principales automáticamente. Ideal para artículos. |
| **Summarizer.org**| Hasta 2000 palabras*| 11 idiomas | No | Permite ajustar la longitud del resumen. |
| **TLDR This** | 5 resúmenes/mes* | Inglés/Esp | Sí | Muy eficaz pero limitado en su versión gratuita. |
| **ChatGPT (Free)**| ~128k context | Multilingüe | Sí | Versátil; requiere "chunking" manual para registros excesivos. |

*\*Los límites pueden variar según actualizaciones de la plataforma.*

## 2. Modelos Open Source (Uso Local)

Para registros extremadamente sensibles o de gran volumen (Gb/Tb), se recomienda el uso local con hardware adecuado.

| Modelo | Ventana de Contexto | Licencia | Ideal para... |
| :--- | :--- | :--- | :--- |
| **DeepSeek-V3 / R1** | 128,000 tokens | MIT | Razonamiento complejo y análisis de logs extensos. |
| **Qwen3-30B-A3B** | 256,000 tokens | Apache 2.0 | Excelente equilibrio entre velocidad y capacidad de contexto. |
| **Llama 4 Scout** | 10M+ tokens | Llama 3.1 | Procesamiento de libros enteros o bases de datos completas. |
| **Mistral NeMo** | 128,000 tokens | Apache 2.0 | Eficiencia en hardware de consumo medio (NVIDIA RTX). |

### Requerimientos de Hardware (Estimados)
- **Modelos Pequeños (8B/14B):** Mínimo 16GB RAM o 8GB VRAM (GPU).
- **Modelos Medios (30B-70B):** Mínimo 32GB-64GB RAM o 24GB VRAM.

## 3. Recomendaciones según el Tipo de Registro

- **Logs de Servidor / Auditoría:** Usar **DeepSeek R1** localmente (privacidad total) o **Decopy AI** si los datos no son sensibles.
- **Documentos Científicos (PDF):** **Mapify** o **Decopy AI** por su capacidad de generar mapas mentales.
- **Registros de Chat / Conversaciones:** **QuillBot** o **ChatGPT** (vía API gratuita si se dispone de créditos).

## 4. Estrategias para Textos "Infinitos"

Si el registro supera el límite de la IA (Context Window):
1. **Recursive Summarization:** Dividir el texto en partes, resumir cada parte, y luego resumir los resúmenes.
2. **LangChain / RAG:** Implementar una base de datos vectorial para que la IA consulte solo las partes relevantes del registro.
