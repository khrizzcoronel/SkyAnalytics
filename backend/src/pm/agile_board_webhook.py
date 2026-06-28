class AgileBoard:
    def __init__(self):
        self.tickets = {}

    def create_ticket(self, ticket_id: str, title: str, priority: str = "Normal"):
        self.tickets[ticket_id] = {"title": title, "status": "To Do", "priority": priority}
        print(f"[AGILE BOARD] Creado: {ticket_id} | Priority: {priority} | Status: To Do")

    def handle_webhook(self, event_type: str, branch_or_pr_name: str):
        print(f"\n[WEBHOOK] Recibido evento: '{event_type}' en '{branch_or_pr_name}'")
        
        # Extraer ticket ID asumiendo convención (ej. feature/SKY-101-...)
        parts = branch_or_pr_name.split('/')
        if len(parts) > 1:
            ticket_id_candidate = parts[1].split('-')[0:2]
            ticket_id = "-".join(ticket_id_candidate).upper()
        else:
            return
            
        if ticket_id not in self.tickets:
            return
            
        if event_type == "create_branch":
            self.tickets[ticket_id]["status"] = "In Progress"
            print(f"[AGILE BOARD] Movido {ticket_id} a 'In Progress' automaticamente.")
        elif event_type == "open_pr":
            self.tickets[ticket_id]["status"] = "In Review"
            print(f"[AGILE BOARD] Movido {ticket_id} a 'In Review' automaticamente.")
        elif event_type == "merge_pr":
            self.tickets[ticket_id]["status"] = "Done"
            print(f"[AGILE BOARD] Movido {ticket_id} a 'Done'. ¡Definition of Done cumplido!")

if __name__ == "__main__":
    board = AgileBoard()
    
    # Planeación
    board.create_ticket("SKY-101", "Añadir endpoint GraphQL de Clima")
    
    # Simulación de ciclo de vida del desarrollador
    board.handle_webhook("create_branch", "feature/SKY-101-graphql-weather")
    board.handle_webhook("open_pr", "feature/SKY-101-graphql-weather")
    board.handle_webhook("merge_pr", "feature/SKY-101-graphql-weather")
