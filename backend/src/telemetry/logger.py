import logging
import json
import re
import uuid

class PIIScrubberFormatter(logging.Formatter):
    """Formateador que enmascara PII y genera salida JSON."""
    def format(self, record):
        msg = record.getMessage()
        # Scrubbing Tarjetas de Crédito simples (16 dígitos)
        msg = re.sub(r'\b(?:\d[ -]*?){13,16}\b', '[REDACTED_CC]', msg)
        
        log_record = {
            "level": record.levelname,
            "trace_id": getattr(record, 'trace_id', 'no-trace'),
            "message": msg
        }
        return json.dumps(log_record)

def get_logger():
    logger = logging.getLogger("TelemetryLogger")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(PIIScrubberFormatter())
        logger.addHandler(handler)
    return logger

if __name__ == "__main__":
    log = get_logger()
    fake_trace_id = str(uuid.uuid4())
    
    # Simula paso de trace_id usando extra dict
    log.info("Procesando pago de cliente VIP", extra={'trace_id': fake_trace_id})
    
    # Simula fuga de PII (Regla RN-O07-001)
    log.error("Fallo al cobrar tarjeta 4532 1234 5678 9012 por fondos insuficientes", extra={'trace_id': fake_trace_id})
