import random
import csv
import os

def generate_csv(filepath: str, num_rows: int = 5000):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['flight_id', 'departure_date', 'airline', 'status', 'monto_pago'])
        
        airlines = ['AA', 'DL', 'UA', 'SW']
        statuses = ['ON_TIME', 'DELAYED', 'CANCELLED']
        
        for i in range(num_rows):
            flight_id = f"{random.choice(airlines)}{random.randint(100, 9999)}"
            departure_date = f"2026-11-{random.randint(1, 30):02d}"
            airline = flight_id[:2]
            status = random.choice(statuses)
            monto_pago = round(random.uniform(100.0, 1500.0), 2)
            
            # Injecting purposeful errors (approx 1%)
            if random.random() < 0.01:
                # 1. Nulo crítico
                flight_id = ""
            elif random.random() < 0.01:
                # 2. Dato numérico corrupto
                monto_pago = "ERROR_TEXT"
                
            writer.writerow([flight_id, departure_date, airline, status, monto_pago])

    print(f"Generado {filepath} con {num_rows} registros.")

if __name__ == "__main__":
    # Genera el archivo en la misma ruta
    output_path = os.path.join(os.path.dirname(__file__), 'daily_flights.csv')
    generate_csv(output_path)
