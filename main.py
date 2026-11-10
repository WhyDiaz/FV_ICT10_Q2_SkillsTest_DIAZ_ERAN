from pyscript import document, display

elements = {"`Hydrogen": ("H", 1, 1.008), "Helium": ("He", 2, 4.0026),"Carbon": ("C", 6, 12.011),"Nitrogen": ("N", 7, 14.007),"Oxygen": ("O", 8, 15.999),"Fluorine": ("F", 9, 18.998), "Neon": ("Ne", 10, 20.180), "Phosphorus": ("P", 15, 30.974), "Sulfur": ("S", 16, 32.06), "Chlorine": ("Cl", 17, 35.45), "Argon": ("Ar", 18, 39.948),  "Selenium": ("Se", 34, 78.971), "Bromine": ("Br", 35, 79.904),"Krypton": ("Kr", 36, 83.798), "Iodine": ("I", 53, 126.90),"Xenon": ("Xe", 54, 131.29),"Radon": ("Rn", 86, 222.0)}

def search_element(e):

    element1 = document.getElementById("element1").value
    result = elements.get(element1, ("Element NOT Found", "-", "-"))

    document.getElementById("Name").innerText = element1
    document.getElementById("Symbol").innerText = result[0]
    document.getElementById("AtomicNumber").innerText = result[1]
    document.getElementById("AtomicMass").innerText = result[2]