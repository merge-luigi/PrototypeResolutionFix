# Prototype (2009) High Resolution & Widescreen Fix (v1.0)

An open-source Python patcher that unlocks high widescreen resolutions (such as **1080p / 1200p+**) for *Prototype (2009)* by patching `prototypeenginef.dll` in-place.

Language / Idioma: [English](#english) | [Español](#español)

---

<a name="english"></a>
# [UK] English

## Reverse Engineering Discoveries & Features

This script neutralizes 3 hardcoded engine bottlenecks inside `prototypeenginef.dll`:

| # | Offset | Feature | Impact |
|---|--------|---------|--------|
| **1** | `0x2E02B7` | **Safety Cap Removal** | Removes the hardcoded `1280x800` resolution ceiling caused by VRAM overflows on modern GPUs. |
| **2** | `0x4DFC3C` | **VRAM Menu Bypass** | Prevents graphic quality settings (Shadows, Textures) from forcing themselves to "Low". |
| **3** | `0x616F20` | **Direct3D 9 Filter Bypass** | Forces `EnumAdapterModes` to accept modern widescreen display modes. |

---

## Quick Start Guide

> **Tip:** Make sure **Prototype is closed** before executing the script.

1. **Download or Copy** `PrototypeResolutionFix.py`.
2. **Place the script** in your Prototype installation directory (where `prototypef.exe` resides), *or run it from any directory* (the script auto-detects Steam installations).
3. **Run the patcher**:
   ```bash
   python PrototypeResolutionFix.py
   ```
4. **Launch Prototype**, navigate to **Options -> Graphics -> Resolution**, and select your new widescreen resolution!

---

## Safety & Legal Information

> **Note:** **100% Legal & Clean**: This project does **not** distribute copyrighted game binaries (`.dll` or `.exe`). It modifies your legally owned local copy in-place.

- **Automatic Backup**: An unpatched original backup (`prototypeenginef.dll.bak`) is created automatically before any bytes are altered.

---

## License
Distributed under the [MIT License](LICENSE).

<br/>
<hr/>
<br/>

<a name="español"></a>
# [ES] Español

## Descubrimientos de Ingeniería Inversa y Características

Este script neutraliza 3 cuellos de botella del motor codificados en `prototypeenginef.dll`:

| # | Offset | Característica | Impacto |
|---|--------|----------------|---------|
| **1** | `0x2E02B7` | **Eliminación del Cap de Seguridad** | Elimina el límite de `1280x800` causado por el desbordamiento de VRAM en placas de video modernas. |
| **2** | `0x4DFC3C` | **Bypass de VRAM en Menú** | Evita que las opciones de calidad gráfica (sombras, texturas) se fuercen a calidad "Baja". |
| **3** | `0x616F20` | **Bypass de Filtro Direct3D 9** | Fuerza a `EnumAdapterModes` a reconocer modos de pantalla panorámica modernos. |

---

## Guía de Inicio Rápido

> **Consejo:** Asegúrate de **cerrar Prototype** antes de ejecutar el parcheador.

1. **Descarga o Copia** `PrototypeResolutionFix.py`.
2. **Ubica el script** en la carpeta de instalación de Prototype (donde se encuentra `prototypef.exe`), *o ejecútalo desde cualquier carpeta* (el script detecta instalaciones de Steam automáticamente).
3. **Ejecuta el parcheador**:
   ```bash
   python PrototypeResolutionFix.py
   ```
4. **Abre Prototype**, ve a **Opciones -> Gráficos -> Resolución** y selecciona tu nueva resolución panorámica.

---

## Información Legal y de Seguridad

> **Nota:** **100% Legal y Limpio**: Este proyecto **no** distribuye binarios protegidos por derechos de autor (`.dll` o `.exe`). Modifica tu copia local de forma segura.

- **Respaldo Automático**: Se genera automáticamente una copia de seguridad original (`prototypeenginef.dll.bak`) antes de modificar cualquier byte.

---

## Licencia
Distribuido bajo la Licencia [MIT](LICENSE).
