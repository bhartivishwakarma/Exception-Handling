instrument_families = {
    "Strings": ["Banjo", "Sitar"],
    "Percussion": ["Congas", "Bodhran"],
    "Woodwinds": ["Flute", "Oboe", "Clarinet"]
}

class InventoryError(Exception):
    pass

def print_instrument_families():
    families_to_check = ["Strings", "Percussion", "Woodwinds", "Brass"]
    for family in families_to_check:
        try:
            if family not in instrument_families:
                raise InventoryError(f"Family '{family}' not found in inventory!")
            
            instruments = ", ".join(instrument_families[family])
            print(f"Some instruments in the {family} family are: {instruments}")
        
        except InventoryError as e:
            print("Custom Error:", e)
        except Exception as e:
            print("Unexpected Error:", e)

print_instrument_families()
