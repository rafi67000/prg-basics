import json

# Dane pacjenta
data = {
    "patient_record": {
        "patient_id": "P001234",
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1985-05-15",
        "gender": "Male",
        # Dane kontaktowe zapisane w osobnym słowniku
        "contact_info": {
            "phone_number": "+1-555-123-4567",
            "email": "johndoe@example.com",
            "address": {
                "street": "123 Main St",
                "city": "New York",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA"
            }
        },
        # Historia medyczna zawiera listy i słowniki
        "medical_history": {
            "allergies": ["Penicillin", "Peanuts"],
            "current_medications": ["Lisinopril 10mg", "Metformin 500mg"],
            "past_illnesses": ["Hypertension", "Type 2 Diabetes"],
            "surgeries": [
                {
                    "surgery_type": "Appendectomy",
                    "date": "2015-08-20"
                }
            ]
        }
    }
}

# Zapisanie danych do pliku JSON
with open('patient.json', 'w', encoding='utf-8') as file:
    # indent=4 dodaje wcięcia w pliku JSON
    json.dump(data, file, indent=4)

print('Data has been written to patient.json')
