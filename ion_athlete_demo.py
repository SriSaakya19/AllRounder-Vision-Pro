import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ION AMS 2.0 - OBSIDIAN & ROSE GOLD ELITE THEME
st.set_page_config(page_title="ION AMS 2.0", layout="wide", page_icon="⚡")

st.markdown("""
<style>
 .stApp { background-color: #0F0F12; color: #FFFFFF; } /* Pitch Obsidian */
    div[data-testid="metric-container"] {
        background-color: #1B1B20; /* Deep Slate */
        border: 1px solid #2A2A30;
        padding: 18px;
        border-radius: 12px;
    }
    div[data-testid="metric-container"] label { color: #FFFFFF!important; font-size: 14px; } /* Metric Title White */
    div[data-testid="metric-container"] div { color: #FFFFFF!important; } /* Metric Value White */
 .stTabs [data-baseweb="tab-list"] { background-color: #1B1B20; border-radius: 8px; }
 .stTabs [data-baseweb="tab"] { color: #FFFFFF; }
    h1, h2, h3, p, label { color: #FFFFFF!important; font-weight: 600; } /* All labels white */
 .stSelectbox label { color: #FFFFFF!important; }
 .stSelectbox [data-baseweb="select"] { background-color: #1B1B20; color: #FFFFFF; }
</style>
""", unsafe_allow_html=True)

st.title("ION TOTAL ATHLETE MONITORING SYSTEM 2.0")
st.markdown("**Official Fitness Partner: ION x APL** | *Bhimavaram Bulls Performance Hub*")
st.divider()

# REAL BHIMAVARAM BULLS SQUAD + NITISH KUMAR REDDY AS CAPTAIN
athletes = [
    'NITISH KUMAR REDDY (C)', # Added as Captain
    'M HEMANTH REDDY',
    'THOTA SRAVAN',
    'REVANTH REDDY (WK)',
    'MOPADA RAVIKIRAN',
    'BENDALAM SATVIK',
    'M DHEERAJ KUMAR',
    'B MUNISH VARMA',
    'BAILAPUDI YESWANTH',
    'SATYANARAYANA RAJU',
    'CHENNUPATI RAVI TEJA',
    'DHEERAJ LAXMAN'
]

weeks = ['W1', 'W2', 'W3', 'W4']
data = []
np.random.seed(42) # For consistent demo data
for ath in athletes:
    for i, w in enumerate(weeks):
        data.append({
            'Week': w,
            'Athlete': ath,
            'CMJ_Height': np.random.randint(50, 60) + i*0.3,
            'Sprint_Speed': np.random.uniform(9.0, 10.8) - i*0.05,
            'Squat_Power': np.random.randint(1200, 1600),
            'ACWR': np.random.uniform(0.7, 1.9),
            'Fatigue_Index': np.random.randint(25, 75)
        })
df = pd.DataFrame(data)

# KPI METRIC CARDS - ALL WHITE
st.subheader("📊 Squad Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Avg CMJ", "55.8 cm", "+1.9cm vs Baseline")
with col2:
    st.metric("High Risk Athletes", "2", "-1 from last week")
with col3:
    st.metric("Team Readiness", "89%", "+7%")
with col4:
    st.metric("Total Workload", "3,120 AU", "+15%")

tab1, tab2, tab3 = st.tabs(["📈 Trends", "📊 Comparison", "⚡ Risk Analysis"])

# TAB 1: DYNAMIC LINE CHART
with tab1:
    st.header("CMJ Fatigue Trend & Sprint Performance")
    athlete_select = st.selectbox("Select Athlete", df['Athlete'].unique())
    df_ath = df[df['Athlete'] == athlete_select]

    fig_line = px.line(df_ath, x='Week', y=['CMJ_Height', 'Sprint_Speed'],
                       title='Performance Trend Over 4 Weeks',
                       markers=True, labels={'value':'Score', 'variable':'Metric'})
    fig_line.update_layout(
        paper_bgcolor='#1B1B20', plot_bgcolor='#0F0F12',
        font=dict(color='#FFFFFF', size=13),
        title_font_color='#FFFFFF',
        xaxis=dict(gridcolor='#2A2A30', tickfont=dict(color='#FFFFFF')),
        yaxis=dict(gridcolor='#2A2A30', tickfont=dict(color='#FFFFFF')),
        legend=dict(bgcolor='#1B1B20', font=dict(color='#FFFFFF'))
    )
    fig_line.update_traces(line_width=3)
    fig_line.data[0].line.color = '#E0A899' # Rose Gold - CMJ
    fig_line.data[1].line.color = '#00E5FF' # Electric Cyan - Sprint
    st.plotly_chart(fig_line, use_container_width=True)

# TAB 2: HORIZONTAL BAR CHART
with tab2:
    st.header("Squad Comparison - Testing Scores")
    latest_data = df[df['Week'] == 'W4'].sort_values('Squat_Power', ascending=True)

    fig_bar = px.bar(latest_data, x='Squat_Power', y='Athlete',
                     orientation='h', title='Squat Power Ranking - Week 4',
                     color='Squat_Power', color_continuous_scale=['#E0A899', '#C86D51'])
    fig_bar.update_layout(
        paper_bgcolor='#1B1B20', plot_bgcolor='#0F0F12',
        font=dict(color='#FFFFFF'),
        title_font_color='#FFFFFF',
        xaxis=dict(gridcolor='#2A2A30', tickfont=dict(color='#FFFFFF')),
        yaxis=dict(gridcolor='#2A2A30', tickfont=dict(color='#FFFFFF'))
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# TAB 3: ACWR SCATTER PLOT
with tab3:
    st.header("Acute-to-Chronic Workload Ratio - Injury Risk")

    fig_scatter = px.scatter(df, x='Week', y='ACWR', size='Fatigue_Index',
                             color='Athlete', hover_data=['CMJ_Height'],
                             title="ACWR Across Squad")
    fig_scatter.add_hline(y=0.8, line_dash="dash", line_color="#00E5FF", annotation_text="Under-trained", annotation_font_color="white")
    fig_scatter.add_hline(y=1.3, line_dash="dash", line_color="#E0A899", annotation_text="Sweet Spot", annotation_font_color="white")
    fig_scatter.add_hline(y=1.5, line_dash="dash", line_color="#C86D51", annotation_text="High Risk", annotation_font_color="white")

    fig_scatter.update_layout(
        paper_bgcolor='#1B1B20', plot_bgcolor='#0F0F12',
        font=dict(color='#FFFFFF'),
        title_font_color='#FFFFFF',
        xaxis=dict(gridcolor='#2A2A30', tickfont=dict(color='#FFFFFF')),
        yaxis=dict(gridcolor='#2A2A30', tickfont=dict(color='#FFFFFF')),
        legend=dict(font=dict(color='#FFFFFF'), bgcolor='#1B1B20')
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.caption("🔵 <0.8 Under-trained | 🟡 0.8-1.3 Optimal | 🔴 >1.5 High Injury Risk")

st.divider()
st.markdown("Built for ION Athlete Performance Studio x Bhimavaram Bulls | Telemetry v2.0")