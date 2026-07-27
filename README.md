# Prototype (2009) — High Resolution & Widescreen Fix

Python patcher that unlocks 1080p/1440p/4K widescreen for *Prototype (2009)* by patching `prototypeenginef.dll` directly.

🌐 **Language / Idioma**: [English](#english) | [Español](#español)

---

<a name="english"></a>
## English

### How to Use

> Close Prototype before running the script.

```bash
git clone https://github.com/your-username/PrototypeResolutionFix.git
cd PrototypeResolutionFix
python PrototypeResolutionFix.py
```

Then launch Prototype → **Options → Graphics → Resolution** and select your resolution.

> **Non-Steam install?** Copy `PrototypeResolutionFix.py` into your game folder (where `prototypef.exe` is) and run it from there.

### What It Patches

Three hardcoded limits inside `prototypeenginef.dll`:

| Offset | Description |
|---|---|
| `0x2E02B7` | Removes the `1280x800` hardcoded resolution ceiling |
| `0x4DFC3C` | Prevents graphics quality from auto-resetting to Low |
| `0x616F20` | Forces Direct3D 9 to accept high widescreen display modes |

A backup (`prototypeenginef.dll.bak`) is created automatically before any changes are made. MIT License.

---

<a name="español"></a>
## Español

### Cómo Usarlo

> Cerrá Prototype antes de ejecutar el script.

```bash
git clone https://github.com/tu-usuario/PrototypeResolutionFix.git
cd PrototypeResolutionFix
python PrototypeResolutionFix.py
```

Luego abrí Prototype → **Opciones → Gráficos → Resolución** y elegí tu resolución.

> **¿Instalación fuera de Steam?** Copiá `PrototypeResolutionFix.py` a la carpeta del juego (donde está `prototypef.exe`) y ejecutalo desde ahí.

### Qué Parchea

Tres límites codificados dentro de `prototypeenginef.dll`:

| Offset | Descripción |
|---|---|
| `0x2E02B7` | Elimina el límite de resolución hardcodeado a `1280x800` |
| `0x4DFC3C` | Evita que la calidad gráfica se fuerce a Baja automáticamente |
| `0x616F20` | Fuerza a Direct3D 9 a reconocer modos panorámicos en alta resolución |

Se genera automáticamente un respaldo (`prototypeenginef.dll.bak`) antes de cualquier cambio. Licencia MIT.
