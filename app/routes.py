from flask import Blueprint, render_template, request, url_for, redirect
from app.utils.config import MONTO_MINIMO, STEP, RUTA_PAGOS, RUTA_DEUDAS
from app.utils.gestionar_json import leer, escribir

bp = Blueprint("main", __name__)

@bp.route("/")
def inicio():
    return render_template("index.html")


@bp.route("/agregar")
def agregar():
    cambio = request.args.get("cambio", default=None, type=int)
    mensaje = ""

    if cambio is not None and cambio > 0:
        mensaje = f"Debes devolver {cambio}"

    return render_template("agregar.html", cambio=mensaje, MONTO_MINIMO=MONTO_MINIMO, STEP=STEP)

@bp.route("/deudas")
def deudas():
    lista_deudas = leer(RUTA_DEUDAS)
    return render_template("deudas.html", deudas=lista_deudas)

@bp.route("/enviar", methods=["POST"])
def enviar_usuario():
    nombre = request.form["nombre"]
    dinero = request.form["dinero"]

    cambio = int(dinero) - MONTO_MINIMO

    if cambio > 0:
        archivo_deudas = leer(RUTA_DEUDAS)
        nueva = {
            "nombre": nombre,
            "cambio": cambio
        }

        archivo_deudas.append(nueva)

        escribir(archivo_deudas, RUTA_DEUDAS)

    leer_archivo = leer(RUTA_PAGOS)
    leer_archivo.append(nombre)
    escribir(leer_archivo, RUTA_PAGOS)

    return redirect(url_for("main.agregar", cambio=cambio))

@bp.route("/eliminar_deuda/<nombre>")
def eliminar_deuda(nombre):
    leer_deudas = leer(RUTA_DEUDAS)

    for d in leer_deudas:
        if d["nombre"] == nombre:
            leer_deudas.remove(d)
            break

    escribir(leer_deudas, RUTA_DEUDAS)

    return redirect(url_for("main.deudas"))
