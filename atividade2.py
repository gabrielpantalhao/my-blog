import requests

# ============================================
# 1. LOGIN NA SPTRANS
# ============================================

TOKEN = "c63269489dab5c336c22e4101946f8549cda2430bc7d9751bbba198c4144a529"

url_login = f"https://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={TOKEN}"

# Sessão para manter cookies
sess = requests.Session()
login_response = sess.post(url_login)

if login_response.text.lower() == "true":
    print("🔓 Login efetuado com sucesso!")
else:
    print("❌ Falha no login. Verifique o token.")
    exit()


# ============================================
# 2. CONSULTA DA LINHA (675K-10)
# ============================================

linha = "675K-10"
url_linha = f"https://api.olhovivo.sptrans.com.br/v2.1/Linha/Buscar?termosBusca={linha}"

linha_resp = sess.get(url_linha).json()

print("\n📌 Dados da Linha:")
print(linha_resp)
