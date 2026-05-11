import streamlit as st
import qrcode
from PIL import Image
import io
import os

APP_URL = "sua-url-aqui"

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

  .stApp {
    background-color: #1A1A1A;
  }

  /* Remove default padding */
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
    margin-bottom: 2.2rem;
    letter-spacing: 0.02em;
  }

  .orange-accent {
    color: #F26522;
    font-weight: 700;
  }

  /* Divider */
  .divider {
    border: none;
    border-top: 1px solid #333333;
    margin: 2rem 0;
  }

  /* Section headers */
  .section-label {
    font-size: 0.75rem;
    font-weight: 700;
    color: #F26522;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 0.6rem;
  }

  /* Footer */
  .footer {
    text-align: center;
    color: #555555;
    font-size: 0.82rem;
    margin-top: 2.5rem;
    padding-top: 1.2rem;
    border-top: 1px solid #2E2E2E;
  }

  /* Download button override */
  .stDownloadButton > button {
    background-color: #F26522 !important;
    color: #FFFFFF !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.65rem 2rem !important;
    width: 100%;
    letter-spacing: 0.03em;
    transition: background-color 0.2s ease;
  }

  .stDownloadButton > button:hover {
    background-color: #D4551A !important;
  }

  .qr-label {
    text-align: center;
    color: #888888;
    font-size: 0.82rem;
    margin-top: 0.5rem;
  }
</style>
""", unsafe_allow_html=True)


# ── HEADER ──────────────────────────────────────────────────────────────────
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

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── DOWNLOAD + QR CODE ───────────────────────────────────────────────────────
col_dl, col_qr = st.columns([3, 2], gap="large")

with col_dl:
    st.markdown("<p class='section-label'>Baixe o material</p>", unsafe_allow_html=True)

    docx_path = os.path.join(os.path.dirname(__file__), "NEO - Produtividade com IA.docx")
    if os.path.exists(docx_path):
        with open(docx_path, "rb") as fh:
            docx_bytes = fh.read()
        st.download_button(
            label="⬇  Baixar Material (.docx)",
            data=docx_bytes,
            file_name="NEO - Produtividade com IA.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    else:
        st.warning("Arquivo .docx não encontrado na pasta do app.")

with col_qr:
    st.markdown("<p class='section-label'>Acesse pelo celular</p>", unsafe_allow_html=True)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=2,
    )
    qr.add_data(APP_URL)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="#F26522", back_color="#1A1A1A")
    buf = io.BytesIO()
    qr_img.save(buf, format="PNG")
    buf.seek(0)

    st.image(buf, width=180)
    st.markdown("<p class='qr-label'>Aponte a câmera para baixar</p>", unsafe_allow_html=True)

# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown(
    "<div class='footer'>Conteúdo gerado com IA · NEO Empresarial · neoempresarial.com.br</div>",
    unsafe_allow_html=True,
)
