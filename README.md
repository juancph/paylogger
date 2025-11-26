# 💰 Gestor de Deudas

Aplicación web desarrollada con **Flask** que permite registrar, visualizar y eliminar deudas de manera sencilla.  
El proyecto usa almacenamiento en formato **JSON** y cuenta con una interfaz moderna y responsiva.

---

## 🚀 Características

- 📋 Ver una lista de deudas registradas.  
- ➕ Agregar nuevas deudas o pagos.  
- ❌ Eliminar una deuda con un clic.    
- 🧱 Estructura modular (Blueprints, utils, data, static, templates).

---

## 🗂️ Estructura del proyecto

```
paylogger
├── app
│   ├── data
│   │   ├── deudas.json
│   │   └── pagos.json
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   ├── agregar.css
│   │   │   ├── deudas.css
│   │   │   └── style.css
│   │   └── img
│   │       ├── deuda.svg
│   │       ├── lista.svg
│   │       ├── logo.svg
│   │       └── persona.svg
│   ├── templates
│   │   ├── agregar.html
│   │   ├── deudas.html
│   │   └── index.html
│   └── utils
│       ├── config.py
│       ├── gestionar_json.py
│       └── __init__.py
├── README.md
├── requirements.txt
└── run.py
```

---

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio**
```bash
git clone https://github.com/juancph/paylogger.git
cd paylogger
```

2. **Crear y activar un entorno virtual**
```bash
python -m venv venv
source venv/bin/activate     # En Linux/Mac
venv\Scripts\activate        # En Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**
```bash
python run.py
```

5. **Abre tu navegador y pon**
[http://localhost:5000](http://localhost:5000)
