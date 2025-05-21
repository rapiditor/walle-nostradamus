from src import data_loader, feature_engineering, model, predictor, utils
import os
from datetime import datetime

def main():
    print("🔁 Iniciando sistema Wall-E – Nostradamus...")

    # 1. Cargar datos (simulado)
    print("📥 Cargando datos...")
    raw_data = [{"equipo": "Yankees", "bateo": 0.285, "pitcheo": 2.91},
                {"equipo": "Red Sox", "bateo": 0.260, "pitcheo": 4.12}]

    # 2. Procesar datos
    print("🧼 Procesando datos...")
    processed_data = raw_data  # Aquí iría feature_engineering.transform(raw_data)

    # 3. Predecir con modelo
    print("🧠 Aplicando modelo...")
    pick = "Yankees"  # Aquí iría model.predict(processed_data)

    # 4. Guardar resultado
    today = datetime.today().strftime("%Y-%m-%d")
    output_path = f"output/picks/{today}.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(f"✅ Pick del día ({today}): {pick}\n")

    # 5. Log
    log_path = f"output/logs/{today}.log"
    with open(log_path, "w") as log:
        log.write(f"LOG [{today}]: Pick generado: {pick}\n")

    print(f"✅ Pick generado y guardado: {pick}")

if __name__ == "__main__":
    main()
