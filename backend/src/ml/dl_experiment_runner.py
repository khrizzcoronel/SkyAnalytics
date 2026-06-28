import time

class DLExperiment:
    def __init__(self, experiment_id: str, total_epochs: int):
        self.experiment_id = experiment_id
        self.total_epochs = total_epochs
        
    def provision_gpu(self):
        print(f"\n[ORCHESTRATOR] Solicitando instancia AWS Spot p4d.24xlarge para Experimento '{self.experiment_id}'...")
        print("[ORCHESTRATOR] Instancia asignada. Entorno aislado (Subred ML) creado.")

    def run_training(self):
        print("\n[DEEP LEARNING] Iniciando entrenamiento de red neuronal multimodal (Data Parallelism)...")
        for epoch in range(1, self.total_epochs + 1):
            # Simular trabajo
            if epoch % 10 == 0 or epoch == self.total_epochs:
                loss = max(0.1, 5.0 - (epoch * 0.1))
                print(f"   Epoch [{epoch}/{self.total_epochs}] | Loss: {loss:.4f}")
                self._save_checkpoint(epoch)

    def _save_checkpoint(self, epoch: int):
        print(f"      -> [S3 CHECKPOINTING] Guardando tensores de Epoch {epoch} en S3...")
        
    def teardown(self):
        print("\n[MONITOR DE HARDWARE] Entrenamiento finalizado. GPU inactiva por 5 minutos.")
        print("[MONITOR DE HARDWARE] Desaprovisionando nodo p4d.24xlarge de AWS.")
        print("[FINOPS] Entorno destruido. Presupuesto personal protegido.")

if __name__ == "__main__":
    experiment = DLExperiment("NLP-NOTAM-Parser", 50)
    
    # 1. Aprovisionar Hardware Especializado
    experiment.provision_gpu()
    
    # 2. Correr entrenamiento masivo
    experiment.run_training()
    
    # 3. Limpiar recursos
    experiment.teardown()
