# Hermes Agents Workspace

Repositorio centralizado para el desarrollo, configuración y ejecución de agentes autónomos basados en el ecosistema **Hermes** (Nous Research).

## 📁 Estructura del Proyecto

```text
hermes/
├── agents/             # Definiciones e implementaciones de agentes específicos
├── skills/             # Habilidades y herramientas modulares (Skills)
├── tools/              # Herramientas personalizadas para los agentes
├── config/             # Configuraciones de modelos, prompts y entornos
├── .gitignore          # Exclusión de credenciales y entornos virtuales
└── README.md           # Documentación del proyecto
```

## 🚀 Inicio Rápido

### Requisitos previos
- Python 3.10+ (o el runtime seleccionado)
- [Ollama](https://ollama.ai/) (opcional, para ejecución local de modelos Hermes)
- Clave de API de OpenRouter, Together AI o Nous Portal (si se usan endpoints en la nube)

### Entorno virtual
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
