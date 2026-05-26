import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Sakura Sushi",
    page_icon="🍣",
    layout="wide",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --red:    #C0392B;
    --dark:   #0D0D0D;
    --cream:  #FAF5EE;
    --gold:   #C9A84C;
    --card-bg:#1A1A1A;
    --border: rgba(201,168,76,0.25);
}

/* Global */
html, body, [class*="css"] {
    background-color: var(--dark) !important;
    color: var(--cream) !important;
    font-family: 'DM Sans', sans-serif;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header {visibility: hidden;}

/* Hero */
.hero {
    text-align: center;
    padding: 3.5rem 1rem 2rem;
    background: radial-gradient(ellipse at 50% 0%, rgba(192,57,43,0.18) 0%, transparent 70%);
    border-bottom: 1px solid var(--border);
    margin-bottom: 2.5rem;
}
.hero-badge {
    display: inline-block;
    font-size: 0.7rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--gold);
    border: 1px solid var(--gold);
    padding: 4px 14px;
    border-radius: 20px;
    margin-bottom: 1rem;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.8rem, 6vw, 5rem);
    font-weight: 900;
    color: var(--cream);
    line-height: 1;
    margin: 0;
}
.hero-title span { color: var(--red); }
.hero-sub {
    color: rgba(250,245,238,0.55);
    font-size: 1rem;
    margin-top: 0.6rem;
    font-weight: 300;
    letter-spacing: 0.05em;
}

/* Filter pills */
.filter-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-bottom: 2.5rem;
}

/* Section heading */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    color: var(--gold);
    border-left: 4px solid var(--red);
    padding-left: 14px;
    margin: 2.5rem 0 1.2rem;
}

/* Cards */
.card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    transition: transform 0.25s, box-shadow 0.25s, border-color 0.25s;
    height: 100%;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 50px rgba(192,57,43,0.22);
    border-color: var(--gold);
}
.card-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    display: block;
}
.card-body { padding: 1.1rem 1.2rem 1.4rem; }
.card-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--cream);
    margin-bottom: 4px;
}
.card-desc {
    font-size: 0.82rem;
    color: rgba(250,245,238,0.55);
    margin-bottom: 10px;
    line-height: 1.5;
}
.card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.price {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--gold);
}
.badge {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 20px;
    background: rgba(192,57,43,0.18);
    color: var(--red);
    border: 1px solid rgba(192,57,43,0.35);
}
.badge-new {
    background: rgba(201,168,76,0.15);
    color: var(--gold);
    border-color: rgba(201,168,76,0.4);
}

/* Divider */
.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 2rem 0;
}

/* Stats bar */
.stats {
    display: flex;
    justify-content: center;
    gap: 3rem;
    padding: 1.5rem;
    background: var(--card-bg);
    border-radius: 12px;
    border: 1px solid var(--border);
    margin-bottom: 2rem;
    flex-wrap: wrap;
}
.stat-item { text-align: center; }
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: var(--gold);
    font-weight: 700;
}
.stat-label {
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(250,245,238,0.45);
}
</style>
""", unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────
menu = [
    {
        "name": "Salmon Nigiri",
        "category": "Nigiri",
        "desc": "Irisan salmon segar premium di atas nasi sushi berbumbu cuka beras.",
        "price": "Rp 45.000",
        "img": "https://images.unsplash.com/photo-1617196034183-421b4040ed20?w=600&q=80",
        "tag": "Populer",
        "tag_type": "hot",
    },
    {
        "name": "Tuna Nigiri",
        "category": "Nigiri",
        "desc": "Tuna merah segar dengan tekstur lembut, disajikan dengan wasabi.",
        "price": "Rp 48.000",
        "img": "https://images.unsplash.com/photo-1559410545-0bdcd187e0a6?w=600&q=80",
        "tag": "Populer",
        "tag_type": "hot",
    },
    {
        "name": "Ebi Nigiri",
        "category": "Nigiri",
        "desc": "Udang rebus segar di atas nasi sushi, manis dan gurih alami.",
        "price": "Rp 42.000",
        "img": "https://images.unsplash.com/photo-1611143669185-af224c5e3252?w=600&q=80",
        "tag": "",
        "tag_type": "",
    },
    {
        "name": "Dragon Roll",
        "category": "Maki Roll",
        "desc": "Roll alpukat dan ebi tempura, dilapisi irisan alpukat tipis di atasnya.",
        "price": "Rp 95.000",
        "img": "https://images.unsplash.com/photo-1582450871972-ab5ca641643d?w=600&q=80",
        "tag": "Best Seller",
        "tag_type": "hot",
    },
    {
        "name": "Rainbow Roll",
        "category": "Maki Roll",
        "desc": "California roll dengan topping ikan warna-warni, tuna, salmon, dan yellowtail.",
        "price": "Rp 110.000",
        "img": "https://images.unsplash.com/photo-1568319188688-b1e29b578e5f?w=600&q=80",
        "tag": "Baru",
        "tag_type": "new",
    },
    {
        "name": "Spicy Tuna Roll",
        "category": "Maki Roll",
        "desc": "Tuna cincang dengan saus sriracha pedas, dibungkus nori renyah.",
        "price": "Rp 78.000",
        "img": "https://images.unsplash.com/photo-1596456755462-f25199e1e577?w=600&q=80",
        "tag": "Pedas",
        "tag_type": "hot",
    },
    {
        "name": "Philadelphia Roll",
        "category": "Maki Roll",
        "desc": "Salmon, krim keju, dan timun — kombinasi creamy yang memikat.",
        "price": "Rp 85.000",
        "img": "https://images.unsplash.com/photo-1617196034082-e3a699e66b40?w=600&q=80",
        "tag": "",
        "tag_type": "",
    },
    {
        "name": "Salmon Sashimi",
        "category": "Sashimi",
        "desc": "Lima iris salmon Norwegia premium tanpa nasi, sangat segar.",
        "price": "Rp 75.000",
        "img": "https://images.unsplash.com/photo-1534482421-64566f976cfa?w=600&q=80",
        "tag": "Populer",
        "tag_type": "hot",
    },
    {
        "name": "Tuna Sashimi",
        "category": "Sashimi",
        "desc": "Irisan tuna merah segar dengan tekstur lembut bak mentega.",
        "price": "Rp 80.000",
        "img": "https://images.unsplash.com/photo-1553621042-f6e147245754?w=600&q=80",
        "tag": "",
        "tag_type": "",
    },
    {
        "name": "Yellowtail Sashimi",
        "category": "Sashimi",
        "desc": "Hamachi segar bercita rasa ringan dan sedikit berlemak, favorit pecinta sashimi.",
        "price": "Rp 85.000",
        "img": "https://images.unsplash.com/photo-1611143669185-af224c5e3252?w=600&q=80",
        "tag": "Baru",
        "tag_type": "new",
    },
    {
        "name": "Chirashi Bowl",
        "category": "Donburi",
        "desc": "Mangkuk nasi sushi dengan aneka irisan ikan segar di atasnya.",
        "price": "Rp 125.000",
        "img": "https://images.unsplash.com/photo-1617196034183-421b4040ed20?w=600&q=80",
        "tag": "Best Seller",
        "tag_type": "hot",
    },
    {
        "name": "Salmon Don",
        "category": "Donburi",
        "desc": "Nasi Jepang hangat dengan irisan salmon mentah melimpah dan saus ponzu.",
        "price": "Rp 105.000",
        "img": "https://images.unsplash.com/photo-1559410545-0bdcd187e0a6?w=600&q=80",
        "tag": "",
        "tag_type": "",
    },
    {
        "name": "Caterpillar Roll",
        "category": "Maki Roll",
        "desc": "Unagi dan timun di dalam, dilapisi alpukat hijau seperti ulat bulu.",
        "price": "Rp 98.000",
        "img": "https://images.unsplash.com/photo-1582450871972-ab5ca641643d?w=600&q=80",
        "tag": "Baru",
        "tag_type": "new",
    },
    {
        "name": "Miso Soup",
        "category": "Pendamping",
        "desc": "Sup miso tradisional dengan tahu sutra, rumput laut, dan daun bawang.",
        "price": "Rp 25.000",
        "img": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=600&q=80",
        "tag": "",
        "tag_type": "",
    },
    {
        "name": "Edamame",
        "category": "Pendamping",
        "desc": "Kacang edamame rebus ditaburi garam laut, camilan khas Jepang.",
        "price": "Rp 28.000",
        "img": "https://images.unsplash.com/photo-1615361200141-f45040f367be?w=600&q=80",
        "tag": "",
        "tag_type": "",
    },
    {
        "name": "Gyoza",
        "category": "Pendamping",
        "desc": "Pangsit goreng berisi ayam dan sayuran, disajikan dengan saus ponzu.",
        "price": "Rp 55.000",
        "img": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?w=600&q=80",
        "tag": "Populer",
        "tag_type": "hot",
    },
    {
        "name": "Matcha Latte",
        "category": "Minuman",
        "desc": "Matcha grade ceremonial dengan susu oat creamy, hangat atau dingin.",
        "price": "Rp 38.000",
        "img": "https://images.unsplash.com/photo-1515823662972-da6a2e4d3002?w=600&q=80",
        "tag": "Favorit",
        "tag_type": "hot",
    },
    {
        "name": "Yuzu Lemonade",
        "category": "Minuman",
        "desc": "Minuman segar dari jeruk yuzu Jepang, asam manis menyegarkan.",
        "price": "Rp 35.000",
        "img": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=600&q=80",
        "tag": "Baru",
        "tag_type": "new",
    },
    {
        "name": "Hojicha Milk",
        "category": "Minuman",
        "desc": "Teh hojicha panggang dengan susu segar, aroma karamel yang khas.",
        "price": "Rp 36.000",
        "img": "https://images.unsplash.com/photo-1594631661960-34c5a5475a25?w=600&q=80",
        "tag": "",
        "tag_type": "",
    },
]

categories = ["Semua"] + sorted(list(set(m["category"] for m in menu)))

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">🍣 Fine Japanese Cuisine</div>
    <h1 class="hero-title">Sakura <span>Sushi</span></h1>
    <p class="hero-sub">Authentic omakase experience — crafted with precision & passion</p>
</div>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats">
    <div class="stat-item"><div class="stat-num">19</div><div class="stat-label">Menu Items</div></div>
    <div class="stat-item"><div class="stat-num">6</div><div class="stat-label">Kategori</div></div>
    <div class="stat-item"><div class="stat-num">⭐ 4.9</div><div class="stat-label">Rating</div></div>
    <div class="stat-item"><div class="stat-num">Fresh</div><div class="stat-label">Daily Import</div></div>
</div>
""", unsafe_allow_html=True)

# ── Filter ────────────────────────────────────────────────────────────────────
selected = st.selectbox("🔍 Filter Kategori", categories, label_visibility="collapsed")

search = st.text_input("", placeholder="🔎  Cari menu...", label_visibility="collapsed")

# ── Filter logic ──────────────────────────────────────────────────────────────
filtered = menu
if selected != "Semua":
    filtered = [m for m in filtered if m["category"] == selected]
if search:
    filtered = [m for m in filtered if search.lower() in m["name"].lower() or search.lower() in m["desc"].lower()]

# ── Group by category & render ────────────────────────────────────────────────
if not filtered:
    st.info("Tidak ada menu yang cocok dengan pencarianmu.")
else:
    cats_shown = [selected] if selected != "Semua" else categories[1:]
    for cat in cats_shown:
        cat_items = [m for m in filtered if m["category"] == cat]
        if not cat_items:
            continue

        st.markdown(f'<div class="section-title">{cat}</div>', unsafe_allow_html=True)

        cols = st.columns(3, gap="medium")
        for i, item in enumerate(cat_items):
            with cols[i % 3]:
                badge_html = ""
                if item["tag"]:
                    cls = "badge-new" if item["tag_type"] == "new" else "badge"
                    badge_html = f'<span class="{cls}">{item["tag"]}</span>'

                st.markdown(f"""
                <div class="card">
                    <img class="card-img" src="{item['img']}" alt="{item['name']}" />
                    <div class="card-body">
                        <div class="card-name">{item['name']}</div>
                        <div class="card-desc">{item['desc']}</div>
                        <div class="card-footer">
                            <span class="price">{item['price']}</span>
                            {badge_html}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding: 2rem 0 1rem; color: rgba(250,245,238,0.3); font-size:0.8rem; letter-spacing:0.08em;">
    © 2025 Sakura Sushi · All rights reserved
</div>
""", unsafe_allow_html=True)
