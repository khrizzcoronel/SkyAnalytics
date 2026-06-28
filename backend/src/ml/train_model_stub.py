import random

class ModelTrainingPipeline:
    def __init__(self, random_seed: int = 42):
        # Determinismo
        self.random_seed = random_seed
        random.seed(self.random_seed)

    def train_and_evaluate(self, base_mape_simulation: float) -> float:
        """
        Simula el entrenamiento de un modelo XGBoost.
        Toma horas en la vida real. Aquí retorna un MAPE simulado.
        """
        print(f"[ML PIPELINE] Iniciando entrenamiento XGBoost con semilla: {self.random_seed}...")
        print("[ML PIPELINE] Extrayendo features de los ultimos 6 meses...")
        print("[ML PIPELINE] Evaluando en test set del mes mas reciente...")
        
        # Simula que el nuevo modelo puede variar un poco respecto a un valor base
        # El MAPE es un error (menor es mejor)
        noise = random.uniform(-1.0, 1.0)
        challenger_mape = base_mape_simulation + noise
        
        print(f"[ML PIPELINE] Entrenamiento finalizado. MAPE Calculado: {challenger_mape:.2f}%")
        return challenger_mape

class ModelRegistryEvaluator:
    def __init__(self, threshold_improvement: float = 2.0):
        # Regla de negocio: mejora debe ser estricta > 2.0% absoluto
        self.threshold_improvement = threshold_improvement
        
    def evaluate(self, champion_mape: float, challenger_mape: float):
        print(f"\n[EVALUADOR] Comparando Modelos...")
        print(f" - Champion MAPE:   {champion_mape:.2f}%")
        print(f" - Challenger MAPE: {challenger_mape:.2f}%")
        
        # Como MAPE es "Error", una mejora es una reducción del número.
        improvement = champion_mape - challenger_mape
        print(f" - Mejora Absoluta: {improvement:.2f}%")
        
        if improvement > self.threshold_improvement:
            print(f"[REGISTRY] ¡ÉXITO! Mejora detectada ({improvement:.2f}% > {self.threshold_improvement}%).")
            print("[REGISTRY] Etiquetando nuevo modelo como: 'Staging-Candidate'")
            print("[SLACK ALERT] Nuevo Challenger listo para revisión. Por favor aprobar despliegue a Producción.")
        else:
            if improvement > 0:
                print(f"[REGISTRY] RECHAZADO. Mejora muy marginal ({improvement:.2f}% <= {self.threshold_improvement}%).")
            else:
                print(f"[REGISTRY] RECHAZADO. El nuevo modelo es PEOR que el histórico (Degradación).")
            print("[REGISTRY] Etiquetando corrida como: 'Archived'. El Champion se mantiene en producción.")

if __name__ == "__main__":
    champion_mape_actual = 15.0  # El modelo en producción tiene 15% de error
    
    # --- Prueba 1: Modelo Supera al Campeón ---
    print("="*50)
    print("RUN 1: Simulando modelo altamente preciso (Derrota al campeón)")
    # Forzamos una semilla que baje el error considerablemente
    pipeline_winner = ModelTrainingPipeline(random_seed=10)
    # Hacemos que de un valor base muy bajo
    winner_mape = pipeline_winner.train_and_evaluate(base_mape_simulation=11.5)
    evaluator = ModelRegistryEvaluator(threshold_improvement=2.0)
    evaluator.evaluate(champion_mape=champion_mape_actual, challenger_mape=winner_mape)

    print("\n" + "="*50)
    
    # --- Prueba 2: Modelo Empata/Pierde contra el Campeón ---
    print("RUN 2: Simulando modelo mediocre (Empate técnico o derrota)")
    pipeline_loser = ModelTrainingPipeline(random_seed=42)
    # Hacemos que de un valor base alto
    loser_mape = pipeline_loser.train_and_evaluate(base_mape_simulation=14.5)
    evaluator.evaluate(champion_mape=champion_mape_actual, challenger_mape=loser_mape)
