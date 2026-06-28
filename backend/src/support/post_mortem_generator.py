from datetime import datetime

class PostMortemGenerator:
    BANNED_NAMES = ["juan", "pedro", "maria", "carlos", "kacor"]

    def blameless_check(self, text: str) -> bool:
        text_lower = text.lower()
        for name in self.BANNED_NAMES:
            if name in text_lower:
                print(f"[BLAMELESS CHECK] VIOLACION: Se detecto el nombre '{name}'. El RCA debe enfocarse en procesos, no culpar personas.")
                return False
        return True

    def generate_template(self, incident_id: str, severity: str, root_cause_draft: str) -> str:
        print(f"\n[POST-MORTEM BOT] Generando plantilla para Incidente {incident_id} ({severity})...")
        
        if not self.blameless_check(root_cause_draft):
            return "ERROR: Plantilla rechazada por violar cultura Blameless."
            
        date = datetime.now().strftime("%Y-%m-%d")
        
        md = f"""# Post-Mortem: {incident_id}
**Fecha:** {date}
**Severidad:** {severity}

## 1. Timeline
- [10:00] Incidente detectado por Datadog.
- [10:05] SRE asume rol de Incident Commander.
- [10:25] Mitigacion aplicada. Servicio restaurado.

## 2. Root Cause (5 Whys)
{root_cause_draft}

## 3. Action Items (Prevencion)
- [ ] Tarea 1: Añadir timeout a la base de datos (Prioridad Urgent).
- [ ] Tarea 2: Mejorar alerta sintetica.
"""
        return md

if __name__ == "__main__":
    generator = PostMortemGenerator()
    
    # Prueba 1: RCA culposo (Blame)
    draft_blame = "El error ocurrio porque Juan ejecuto un script de migracion mal en produccion."
    res1 = generator.generate_template("INC-402", "Sev1", draft_blame)
    print(res1)
    
    # Prueba 2: RCA sistemico (Blameless)
    draft_blameless = "El sistema permitio que un script de migracion sin timeout se ejecutara, saturando la conexion de base de datos."
    res2 = generator.generate_template("INC-403", "Sev1", draft_blameless)
    print("\n--- PLANTILLA APROBADA ---")
    print(res2)
