# Importa a função principal do sistema bancário que está definida no módulo banco.py
from banco import sistema_principal

# Verifica se este arquivo está sendo executado diretamente (e não importado como módulo)
if __name__ == "__main__":
    # Chama a função principal para iniciar o sistema bancário
    sistema_principal()
