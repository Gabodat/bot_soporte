from database import Session, Incidencia
from datetime import datetime

def insert_ticket_109():
    session = Session()
    try:
        # Check if exists first to avoid duplicates if run multiple times
        existing = session.query(Incidencia).filter_by(id=109).first()
        if existing:
            print("Ticket 109 already exists.")
            return

        # Insert Ticket 109
        t = Incidencia(
            id=109,
            usuario_nombre="usuario_prueba",
            cedula="123456",
            telf="04121234567",
            email="test@test.com",
            ubicacion="Sede Principal",
            unidad="N/A",
            equipo="Computadora",
            falla="Falla de prueba para validacion de tecnico",
            user_id="123456789", # Dummy ID
            estado="Abierto",
            fecha_registro=datetime.now()
        )
        session.add(t)
        session.commit()
        print("Ticket 109 created successfully.")
    except Exception as e:
        print(f"Error creating ticket: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    insert_ticket_109()
