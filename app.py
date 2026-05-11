import streamlit as st
import io
import os
import zipfile
import base64
import qrcode
from PIL import Image

APP_URL = "https://seminario-neo-ia.streamlit.app"

ASSETS = os.path.join(os.path.dirname(__file__), "assets")

CASES = [
    {
        "emoji": "🍋",
        "name": "Frizo",
        "subtitle": "Refrigerante de Limão",
        "description": "Marca de refrigerante premium de limão criada para o público jovem brasileiro. O case vai do briefing inicial até o site, com pesquisa de mercado, regulamentação e registro de marca.",
        "zip_name": "frizo-seminario-neo.zip",
        "files": [
            "NEO - Frizo - Roteiro e Prompts.docx",
            "01 - Briefing da Frizo.pdf",
            "02 - Mercado de Refrigerantes no Brasil.pdf",
            "03 - Tendencias Bebidas Premium e Saudaveis.pdf",
            "04 - Normas e Regulamentacao ANVISA.pdf",
            "05 - Patentes e Propriedade Intelectual.pdf",
        ],
    },
    {
        "emoji": "💪",
        "name": "NativaFit",
        "subtitle": "Proteína Premium",
        "description": "Marca de whey protein com ingredientes 100% brasileiros, como açaí e guaraná. O case cobre desde o briefing até o site, com pesquisa de mercado e análise das normas da Anvisa para suplementos.",
        "zip_name": "nativafit-seminario-neo.zip",
        "files": [
            "NEO - NativaFit - Roteiro e Prompts.docx",
            "Documento_01_Suplemento_NativaFit.pdf",
            "Documento_02_Suplemento_NativaFit.pdf",
            "Documento_03_Suplemento_NativaFit.pdf",
            "Documento_04_Suplemento_NativaFit.pdf",
            "Documento_05_Suplemento_NativaFit.pdf",
        ],
    },
    {
        "emoji": "🍺",
        "name": "Brisa Tropical",
        "subtitle": "Cerveja Artesanal",
        "description": "Cerveja artesanal com maracujá e capim-limão. O case vai do briefing ao site, com pesquisa de mercado, regulamentação de bebidas alcoólicas e análise de registro de marca.",
        "zip_name": "brisa-tropical-seminario-neo.zip",
        "files": [
            "NEO - Brisa Tropical - Roteiro e Prompts.docx",
            "Documento_01_Cerveja_Brisa_Tropical.pdf",
            "Documento_02_Cerveja_Brisa_Tropical.pdf",
            "Documento_03_Cerveja_Brisa_Tropical.pdf",
            "Documento_04_Cerveja_Brisa_Tropical.pdf",
            "Documento_05_Cerveja_Brisa_Tropical.pdf",
        ],
    },
]


def build_zip(case: dict) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for filename in case["files"]:
            filepath = os.path.join(ASSETS, filename)
            if os.path.exists(filepath):
                zf.write(filepath, arcname=filename)
    buf.seek(0)
    return buf.read()


def make_qr() -> io.BytesIO:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=2,
    )
    qr.add_data(APP_URL)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#1A1A1A", back_color="#FFFFFF")
    buf = io.BytesIO()
    qr_img.save(buf, format="PNG")
    buf.seek(0)
    return buf


st.set_page_config(
    page_title="Produtividade com IA · NEO Empresarial",
    page_icon="🟠",
    layout="centered",
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #1A1A1A;
    color: #FFFFFF;
  }

  .stApp { background-color: #1A1A1A; }

  .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 860px;
  }

  h1 {
    font-size: 2.6rem !important;
    font-weight: 800 !important;
    color: #FFFFFF !important;
    text-align: center;
    line-height: 1.2;
    margin-bottom: 0.2rem !important;
  }

  .subtitle {
    text-align: center;
    color: #AAAAAA;
    font-size: 1.05rem;
    margin-bottom: 1.4rem;
    letter-spacing: 0.02em;
  }

  .orange-accent { color: #F26522; font-weight: 700; }

  .divider {
    border: none;
    border-top: 1px solid #333333;
    margin: 2rem 0;
  }

  .section-label {
    font-size: 0.75rem;
    font-weight: 700;
    color: #F26522;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 0.6rem;
  }

  .footer {
    text-align: center;
    color: #555555;
    font-size: 0.82rem;
    margin-top: 2.5rem;
    padding-top: 1.2rem;
    border-top: 1px solid #2E2E2E;
  }

  /* URL banner */
  .url-banner {
    background: linear-gradient(to right, #FFD4B0 0%, #F26522 40%, #C94510 100%);
    border-radius: 12px 12px 0 0;
    padding: 1.1rem 1.8rem 1rem;
    text-align: center;
  }
  .url-banner .banner-label {
    font-size: 0.9rem;
    font-weight: 600;
    color: rgba(80,20,0,0.7);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.25rem;
    text-shadow: none;
  }
  .url-banner .banner-url {
    font-size: 1.9rem;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: 0.02em;
    line-height: 1.1;
    text-shadow: 0 1px 4px rgba(0,0,0,0.25);
  }

  /* QR strip abaixo do banner */
  .qr-strip {
    background-color: #2A1A0E;
    border-radius: 0 0 12px 12px;
    padding: 0.8rem 1.8rem;
    text-align: center;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
  }
  .qr-strip .qr-text {
    font-size: 0.88rem;
    color: rgba(255,255,255,0.7);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  /* Download buttons — padronizados e centralizados */
  div[data-testid="stDownloadButton"],
  .stDownloadButton {
    display: flex !important;
    justify-content: center !important;
    margin-top: 0.75rem !important;
  }
  .stDownloadButton > button {
    background-color: #F26522 !important;
    color: #FFFFFF !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.6rem 1.8rem !important;
    width: auto !important;
    min-height: 44px !important;
    letter-spacing: 0.03em;
    transition: background-color 0.2s ease;
    white-space: nowrap;
  }
  .stDownloadButton > button:hover {
    background-color: #D4551A !important;
  }

  /* Cards com altura fixa para botões alinharem */
  .case-card {
    background-color: #242424;
    border: 1px solid #333333;
    border-radius: 12px;
    padding: 1.4rem 1.2rem 1.2rem;
    height: 460px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
  }
  .case-card .case-emoji {
    font-size: 2rem;
    line-height: 1;
    margin-bottom: 0.4rem;
  }
  .case-card .case-name {
    font-size: 1.2rem;
    font-weight: 800;
    color: #FFFFFF;
    margin: 0 0 0.15rem 0;
  }
  .case-card .case-subtitle {
    font-size: 0.78rem;
    font-weight: 600;
    color: #F26522;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.6rem;
  }
  .case-card .case-desc {
    font-size: 0.85rem;
    color: #AAAAAA;
    line-height: 1.5;
    margin-bottom: 0.8rem;
  }
  .case-card .file-list {
    list-style: none;
    padding: 0;
    margin: 0;
    margin-top: auto;
  }
  .case-card .file-list li {
    font-size: 0.76rem;
    color: #888888;
    padding: 0.2rem 0;
    border-bottom: 1px solid #2E2E2E;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .case-card .file-list li:last-child { border-bottom: none; }
</style>
""", unsafe_allow_html=True)


# ── HEADER ───────────────────────────────────────────────────────────────────
logo_path = os.path.join(os.path.dirname(__file__), "logo_neo.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        st.image(logo, use_container_width=True)
else:
    st.markdown(
        "<p style='text-align:center;font-size:1.4rem;font-weight:800;"
        "color:#F26522;letter-spacing:0.1em;margin-bottom:1rem'>NEO EMPRESARIAL</p>",
        unsafe_allow_html=True,
    )

# ── TÍTULO ───────────────────────────────────────────────────────────────────
st.markdown("<h1><span class='orange-accent'>Produtividade</span> com IA</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Seminário NEO Empresarial · Inteligência Artificial na prática</p>", unsafe_allow_html=True)

# ── BANNER URL + QR ──────────────────────────────────────────────────────────
st.markdown(f"""
<div class='url-banner'>
  <div class='banner-label'>Acesse agora pela URL</div>
  <div class='banner-url'>{APP_URL.replace("https://", "")}</div>
</div>
""", unsafe_allow_html=True)

qr_b64 = base64.b64encode(make_qr().read()).decode()
st.markdown(f"""
<div style='text-align:center;margin-top:0.6rem;margin-bottom:0.5rem'>
  <p class='section-label' style='text-align:center'>Acesse pelo celular</p>
  <img src='data:image/png;base64,{qr_b64}' width='240' style='margin:0 auto;display:block'/>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── CASES PARA DOWNLOAD ───────────────────────────────────────────────────────
st.markdown("<p class='section-label'>Cases do seminário · Baixe o material completo</p>", unsafe_allow_html=True)

case_cols = st.columns(3, gap="medium")

for col, case in zip(case_cols, CASES):
    with col:
        file_items = "".join(f"<li>📄 {f}</li>" for f in case["files"])
        st.markdown(f"""
<div class='case-card'>
  <div class='case-emoji'>{case['emoji']}</div>
  <p class='case-name'>{case['name']}</p>
  <p class='case-subtitle'>{case['subtitle']}</p>
  <p class='case-desc'>{case['description']}</p>
  <ul class='file-list'>{file_items}</ul>
</div>
""", unsafe_allow_html=True)

        available = [f for f in case["files"] if os.path.exists(os.path.join(ASSETS, f))]
        if available:
            zip_bytes = build_zip(case)
            st.download_button(
                label=f"⬇  Baixar {case['name']} (.zip)",
                data=zip_bytes,
                file_name=case["zip_name"],
                mime="application/zip",
                key=f"dl_{case['zip_name']}",
            )
        else:
            st.download_button(
                label=f"⬇  Baixar {case['name']} (.zip)",
                data=b"",
                file_name=case["zip_name"],
                mime="application/zip",
                key=f"dl_{case['zip_name']}",
                disabled=True,
            )

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown(
    "<div class='footer'>Conteúdo gerado com IA · NEO Empresarial · neo.certi.org.br</div>",
    unsafe_allow_html=True,
)
