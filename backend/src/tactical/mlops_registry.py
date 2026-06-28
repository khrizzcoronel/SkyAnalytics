class ModelRegistry:
    def __init__(self):
        self.models = {}
        
    def register_run(self, model_id: str, mape: float, has_shap: bool):
        print(f"\n[MLOps] Registrando modelo '{model_id}'...")
        if not has_shap:
            print("[MLOps] [ERROR] Falla de explicabilidad: SHAP report no generado. Corrida descartada.")
            return False
            
        self.models[model_id] = {
            "mape": mape,
            "stage": "Staging",
            "has_shap": has_shap
        }
        print(f"[MLOps] Modelo '{model_id}' guardado en Staging (MAPE: {mape}%). SHAP report adjunto.")
        return True

    def promote_model(self, model_id: str, target_stage: str) -> bool:
        print(f"\n[MLOps] Evaluando promocion de '{model_id}' hacia '{target_stage}'...")
        
        if model_id not in self.models:
            print("[MLOps] [ERROR] Modelo no encontrado en el Registry.")
            return False
            
        model = self.models[model_id]
        
        if target_stage == "Production":
            # Regla RN-T05-001: MAPE <= 15%
            if model["mape"] > 15.0:
                print(f"[MLOps] [ROJO] Transicion Bloqueada. El MAPE del modelo ({model['mape']}%) supera el umbral del 15%.")
                return False
                
        model["stage"] = target_stage
        print(f"[MLOps] [VERDE] Promocion Exitosa. Modelo '{model_id}' esta ahora en '{target_stage}'.")
        return True

if __name__ == "__main__":
    registry = ModelRegistry()
    
    # Escenario 1: Fallo por explicabilidad
    registry.register_run("delay_model_v1", mape=12.0, has_shap=False)
    
    # Escenario 2: Entrenamiento y promocion bloqueada (MAPE alto)
    registry.register_run("delay_model_v2", mape=18.2, has_shap=True)
    registry.promote_model("delay_model_v2", "Production")
    
    # Escenario 3: Entrenamiento y promocion exitosa
    registry.register_run("delay_model_v3", mape=10.5, has_shap=True)
    registry.promote_model("delay_model_v3", "Production")
