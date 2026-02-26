x: str = "8635372.98789"
y: int = 8635372
z: float = 8635372.98789

minha_lista: list = [x,y,z]

minha_lista.append(8967324875612378456)

minha_tuple: tuple = (x,y,z)

dicionario: dict = {
    "key1": 100000,
    
    "key2": "100000",
    "key3": [],
    "banasdjn": (1,2,3),
    "adfoHNIPDBUF": dict()
}

print(type(minha_lista[0]))
print(minha_tuple)

def funcao(x):
    return x + 2

print(funcao(0))
print(dicionario["key1"])
