import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import math
from datetime import timedelta

# --- SETTINGS & THEME ---
st.set_page_config(page_title="FormFlow AI | National Edition", layout="wide")

# --- CSS FIX FOR WHITE BOXES ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    /* This part fixes the 'White Box' visibility issue */
    [data-testid="stMetricValue"] {
        color: #1f77b4 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #31333F !important;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border: 1px solid #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("FormFlow AI: Next-Gen Formwork Optimization")
st.write("National Competition Prototype | Sector: CreaTech & Construction 4.0")

# --- SIDEBAR ---
st.sidebar.header("🕹️ Control Center")
uploaded_file = st.sidebar.file_uploader("Upload BIM Data (CSV)", type="csv")
maint_buffer = st.sidebar.slider("Reconditioning Buffer (Days)", 1, 7, 3)
co2_factor = st.sidebar.number_input("CO2 kg per Panel Mfg", value=25.0)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    # Clean column names in case of hidden spaces
    df.columns = df.columns.str.strip()
    df['PourDate'] = pd.to_datetime(df['PourDate'])
    
    # 1. ENHANCED LOGIC
    df['Main_Panels'] = df['Width_mm'].apply(lambda x: math.ceil(x / 600))
    df['Support_Props'] = df['Main_Panels'] * 2.5
    df['Fasteners'] = df['Main_Panels'] * 8

    # 2. TEMPORAL FLOW ANALYSIS
    df['ReleaseDate'] = df['PourDate'] + pd.to_timedelta(maint_buffer, unit='d')
    all_dates = pd.date_range(df['PourDate'].min(), df['PourDate'].max() + pd.Timedelta(days=10))
    
    daily_stats = []
    for d in all_dates:
        active_batch = df[(df['PourDate'] <= d) & (df['ReleaseDate'] > d)]
        daily_stats.append({
            'Date': d,
            'Panels': active_batch['Main_Panels'].sum()
        })
    
    stats_df = pd.DataFrame(daily_stats)
    peak_demand = stats_df['Panels'].max()
    total_linear_need = df['Main_Panels'].sum()
    savings_pct = ((total_linear_need - peak_demand) / total_linear_need) * 100

    # 3. NATIONAL LEVEL METRICS (The 'White Boxes' now fixed)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Optimized Inventory", f"{peak_demand} Units")
    m2.metric("Procurement Alpha", f"{savings_pct:.1f}%")
    m3.metric("Carbon Offset", f"{(total_linear_need - peak_demand) * co2_factor:.0f} kg")
    m4.metric("Cycle Efficiency", f"{100 - (peak_demand/total_linear_need*100):.1f}%")

    st.markdown("---")

    # 4. DATA VISUALIZATION
    st.subheader("📈 4D Inventory Lifecycle Visualization")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stats_df['Date'], y=stats_df['Panels'], fill='tozeroy', name='Active Panels', line_color='#0068c9'))
    fig.add_hline(y=peak_demand, line_dash="dash", line_color="red", annotation_text="Peak Demand Limit")
    fig.update_layout(hovermode="x unified", plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

    # 5. STANDARDIZATION ANALYTICS
    st.subheader("🎯 Design Standardization Report")
    df['Waste_Score'] = df['Width_mm'] % 600
    bad_designs = df[df['Waste_Score'] > 0]
    
    if not bad_designs.empty:
        st.warning(f"Optimization Alert: {len(bad_designs)} segments require custom timber fillers.")
        st.dataframe(bad_designs[['AreaID', 'Width_mm', 'Waste_Score']].rename(columns={'Waste_Score': 'Gap (mm)'}), use_container_width=True)
    else:
        st.success("Design Perfection: All structural elements match standard modules.")

    # 6. LOGISTICS DISPATCH
    with st.expander("🚚 View Daily Dispatch Manifest"):
        manifest = df[['AreaID', 'PourDate', 'Main_Panels', 'Support_Props', 'Fasteners']].sort_values('PourDate')
        st.dataframe(manifest, use_container_width=True)

else:
    st.info("Awaiting Data Input... Upload your structural CSV to begin optimization.")