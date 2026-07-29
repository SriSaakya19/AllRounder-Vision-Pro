import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from allrounder_model import get_player_stats, get_allrounder_list, get_auction_value, predict_category, generate_swot

st.set_page_config(page_title="AllRounder Vision Pro", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:wght@700&display=swap');
html, body, [class*="st"] { font-family: 'Lora', serif !important; font-weight: 700; color: #1B0000 !important; font-size: 24px !important; background-color: #FAF3E0; }
h1 { font-size: 56px !important; } h2 { font-size: 42px !important; } h3 { font-size: 36px !important; }
.min-card { background: #FFFFFF; border: 3px solid #5D4037; border-radius: 20px; padding: 35px; }
.metric-big { font-size: 60px !important; color: #000; }
</style>
""", unsafe_allow_html=True)

st.title("🏏 All-Rounder Vision Pro - Indian Edition")
st.markdown("### *AI Powered IPL Indian All-Rounder Analysis*")

INDIAN_PLAYERS = get_allrounder_list()
selected_player = st.selectbox("✨ SELECT INDIAN ALL-ROUNDER ✨", INDIAN_PLAYERS)

if selected_player:
    stats = get_player_stats(selected_player)
    auction_val = get_auction_value(selected_player)
    category = predict_category(selected_player)
    swot = generate_swot(selected_player)

    st.markdown(f"""
    <div class="min-card">
        <h2>Featured All-Rounder</h2>
        <h1>🏏 {selected_player}</h1>
        <p><b>Category:</b> {category}</p>
        <p><b>Value:</b> {auction_val}</p>
        <p><b>Batting Avg:</b> {stats['batting_avg']} | <b>SR:</b> {stats['batting_sr']} | <b>Wickets:</b> {stats['wickets']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    
    st.subheader("📊 PERFORMANCE RADAR")
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=[stats['batting_avg']*2, stats['batting_sr']/8, stats['wickets']*15, (10-stats['bowling_econ'])*8, stats['catches']*15],
        theta=['Batting Avg', 'Strike Rate', 'Wickets', 'Economy', 'Fielding'],
        fill='toself', line_color='#5D4037'
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, tickfont_size=22), angularaxis=dict(tickfont_size=24)),
        title=dict(text=f"<b>{selected_player} - Skill Radar</b>", font_size=32),
        font=dict(family="Lora", size=22, color="#000"),
        paper_bgcolor='rgba(0,0,0,0)', height=500
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='min-card'><h3>🏏 Batting</h3><div class='metric-big'>{stats['batting_avg']}</div><div>Avg</div><div class='metric-big'>{stats['batting_sr']}</div><div>SR</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='min-card'><h3>🎯 Bowling</h3><div class='metric-big'>{stats['wickets']}</div><div>Wkts</div><div class='metric-big'>{stats['bowling_econ']}</div><div>Econ</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='min-card'><h3>🛡️ Fielding</h3><div class='metric-big'>{stats['catches']}</div><div>Catches</div><div class='metric-big'>{stats['dots_balls']}</div><div>Dots</div></div>", unsafe_allow_html=True)

    st.subheader("🧠 SWOT ANALYSIS")
    s1, s2, s3, s4 = st.columns(4)
    with s1: 
        st.markdown("<h3>Strengths</h3>", unsafe_allow_html=True)
        for i in swot['Strengths']: st.markdown(f"<p style='font-size:22px'>✅ {i}</p>", unsafe_allow_html=True)
    with s2: 
        st.markdown("<h3>Weaknesses</h3>", unsafe_allow_html=True)
        for i in swot['Weaknesses']: st.markdown(f"<p style='font-size:22px'>❌ {i}</p>", unsafe_allow_html=True) # IKKADA POINTS VASTAI
    with s3: 
        st.markdown("<h3>Opportunities</h3>", unsafe_allow_html=True)
        for i in swot['Opportunities']: st.markdown(f"<p style='font-size:22px'>📈 {i}</p>", unsafe_allow_html=True)
    with s4: 
        st.markdown("<h3>Threats</h3>", unsafe_allow_html=True)
        for i in swot['Threats']: st.markdown(f"<p style='font-size:22px'>⚠️ {i}</p>", unsafe_allow_html=True)