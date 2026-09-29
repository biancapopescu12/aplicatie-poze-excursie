import streamlit as st


st.set_page_config(
    page_title="Albumul excursiei",
    page_icon="📸",
    layout="wide",
)

st.markdown(
    """
    <style>
        .block-container { max-width: 1000px; padding-top: 3rem; }
        .album-intro { color: #64748b; font-size: 1.05rem; margin-bottom: 1.5rem; }
        [data-testid="stFileUploader"] {
            border: 1px dashed #94a3b8;
            border-radius: 16px;
            padding: 1rem;
            background: #f8fafc;
        }
        [data-testid="stFileUploader"] section { padding: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📸 Albumul excursiei")
st.markdown(
    '<p class="album-intro">Adaugă fotografiile tale și bucură-te de toate amintirile într-un singur loc.</p>',
    unsafe_allow_html=True,
)

if "photos" not in st.session_state:
    st.session_state.photos = {}

uploaded_files = st.file_uploader(
    "Încarcă fotografii",
    type=["jpg", "jpeg", "png", "webp", "gif"],
    accept_multiple_files=True,
    help="Poți selecta una sau mai multe fotografii.",
)

for uploaded_file in uploaded_files or []:
    photo_bytes = uploaded_file.getvalue()
    photo_id = (uploaded_file.name, photo_bytes)
    st.session_state.photos[photo_id] = {
        "name": uploaded_file.name,
        "data": photo_bytes,
        "type": uploaded_file.type,
    }

photos = list(st.session_state.photos.values())
st.divider()
st.subheader(f"Fotografiile mele · {len(photos)}")

if not photos:
    st.info("Încă nu ai adăugat fotografii. Apasă pe zona de încărcare de mai sus pentru a începe.")
else:
    columns = st.columns(3)
    for index, photo in enumerate(photos):
        with columns[index % len(columns)]:
            st.image(photo["data"], caption=photo["name"], use_container_width=True)
