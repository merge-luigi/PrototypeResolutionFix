# 🎮 Prototype (2009) High Resolution & Widescreen Fix (v1.0)

An open-source Python patcher that unlocks high widescreen resolutions (such as **1080p / 1200p+**) for *Prototype (2009)* directly inside `prototypeenginef.dll`.

---

## 🛠️ Features & Reverse Engineering Discoveries

This script fixes hardcoded engine limits found in `prototypeenginef.dll`:

1. **Safety Cap Removal (`0x2E02B7`)**: Bypasses the hardcoded check that locks resolutions to `1280x800` when modern GPU VRAM overflows.
2. **VRAM Quality Menu Bypass (`0x4DFC3C`)**: Prevents graphics settings (Shadows, Textures) from resetting to Low quality.
3. **Global Direct3D 9 Filter Bypass (`0x616F20`)**: Forces `EnumAdapterModes` to accept widescreen display modes as valid.

---

## 🚀 How to Use

1. Download or copy `PrototypeResolutionFix.py`.
2. Place `PrototypeResolutionFix.py` in your Prototype installation folder (where `prototypef.exe` is located), OR run it from anywhere.
3. Close the game if it is running.
4. Run the script:
   ```bash
   python PrototypeResolutionFix.py
   ```
5. Launch Prototype, go to **Options -> Graphics**, and select your desired high resolution.

---

## 🛡️ Safety & Legal Note

- **100% Legal & Clean**: This repository does **not** host copyrighted game binaries (`.dll` or `.exe`). It modifies your legally owned local copy in-place.
- **Automatic Backup**: The script automatically creates `prototypeenginef.dll.bak` before making any changes.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

<br/>
<hr/>
<br/>

# 🇪🇸 Versión en Español

# 🎮 Parche de Alta Resolución y Pantalla Ancha para Prototype (2009) - v1.0

Un parcheador de código abierto en Python que desbloquea resoluciones altas y panorámicas (como **1080p / 1200p+**) en *Prototype (2009)* directamente dentro de `prototypeenginef.dll`.

--------------------------------------------------------------------------- ESPAÑOL ---------------------------------------------------------------------------------------------

## 🛠️ Características y Descubrimientos de Ingeniería Inversa

Este script corrige los límites codificados del motor en `prototypeenginef.dll`:

1. **Eliminación del Límite de Seguridad (`0x2E02B7`)**: Anula la restricción que bloqueaba las resoluciones a `1280x800` cuando la VRAM de las GPUs modernas sufría desbordamiento.
2. **Bypass de VRAM en Menú (`0x4DFC3C`)**: Evita que los ajustes gráficos (sombras, texturas) se reseteen automáticamente a calidad Baja.
3. **Bypass Global de Validación Direct3D 9 (`0x616F20`)**: Fuerza a `EnumAdapterModes` a aceptar los modos de pantalla panorámica como válidos.

---

## 🚀 Instrucciones de Uso

1. Descarga o copia `PrototypeResolutionFix.py`.
2. Coloca `PrototypeResolutionFix.py` en la carpeta de instalación de tu juego (donde se encuentra `prototypef.exe`), O ejecútalo desde cualquier ubicación.
3. Cierra el juego si está abierto.
4. Ejecuta el script:
   ```bash
   python PrototypeResolutionFix.py
   ```
5. Inicia Prototype, ve a **Opciones -> Gráficos** y selecciona la alta resolución deseada.

---

## 🛡️ Nota Legal y de Seguridad

- **100% Legal y Limpio**: Este repositorio **no** aloja binarios protegidos por derechos de autor (`.dll` o `.exe`). Modifica tu copia original localmente.
- **Respaldo Automático**: El script crea automáticamente una copia de seguridad `prototypeenginef.dll.bak` antes de aplicar cualquier modificación.
