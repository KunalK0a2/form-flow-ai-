import pandas as pd
import math
from datetime import timedelta

# --- 1. SETTINGS & REFINED INVENTORY DATA ---
# In a real win, we don't just use panels; we use a SYSTEM.
COMPONENT_MULTIPLIERS = {
    'Props': 2.5,      # 2.5 props per panel
    'Tie_Rods': 4.0,   # 4 rods per panel
    'Clamps': 12.0     # 12 clamps per panel
}

def load_data():
    try:
        project = pd.read_csv('project_data.csv')
        inventory = pd.read_csv('inventory_types.csv')
        project['PourDate'] = pd.to_datetime(project['PourDate'])
        return project, inventory
    except FileNotFoundError:
        print("Error: Ensure project_data.csv and inventory_types.csv exist.")
        return None, None

# --- 2. ADVANCED KITTING LOGIC (The "Geometric Brain") ---
def generate_kitting_manifest(width, height):
    """Calculates the exact mix of panels and accessories needed."""
    std_width = 600
    num_panels = math.ceil(width / std_width)
    
    # Calculate waste: How much 'filler' timber is needed?
    efficiency_gap = (std_width - (width % std_width)) % std_width
    
    manifest = {
        'Main_Panels': num_panels,
        'Props': math.ceil(num_panels * COMPONENT_MULTIPLIERS['Props']),
        'Accessories': math.ceil(num_panels * (COMPONENT_MULTIPLIERS['Tie_Rods'] + COMPONENT_MULTIPLIERS['Clamps'])),
        'Waste_Gap_mm': efficiency_gap
    }
    return manifest

# --- 3. TEMPORAL PEAK ANALYSIS (The "Logistics Brain") ---
def analyze_peak_demand(df, buffer_days=3):
    """Calculates the actual inventory needed by simulating daily site activity."""
    df['ReleaseDate'] = df['PourDate'] + timedelta(days=buffer_days)
    
    start_date = df['PourDate'].min()
    end_date = df['ReleaseDate'].max()
    
    daily_log = []
    current_date = start_date
    
    while current_date <= end_date:
        # Which walls are 'active' (pouring or curing) on this specific day?
        active_walls = df[(df['PourDate'] <= current_date) & (df['ReleaseDate'] > current_date)]
        
        daily_panels = active_walls['Main_Panels'].sum()
        daily_log.append({'date': current_date, 'panels_in_use': daily_panels})
        current_date += timedelta(days=1)
        
    return pd.DataFrame(daily_log)

# --- 4. EXECUTION ---
def run_optimization():
    project, inventory = load_data()
    if project is None: return

    # Apply Geometric Kitting
    manifests = project.apply(lambda x: generate_kitting_manifest(x['Width_mm'], x['Height_mm']), axis=1)
    project = pd.concat([project, pd.DataFrame(list(manifests))], axis=1)

    # Calculate Peak
    timeline_df = analyze_peak_demand(project)
    peak_inventory = timeline_df['panels_in_use'].max()
    total_theoretical = project['Main_Panels'].sum()

    # Output Results
    print("\n" + "="*50)
    print("      CREATECH FORMWORK OPTIMIZER: CORE ENGINE")
    print("="*50)
    print(f"Total Individual Wall Demand: {total_theoretical} Panels")
    print(f"Optimized Peak Fleet Needed:  {peak_inventory} Panels")
    print(f"Reduction in Capital Outlay:  {((total_theoretical-peak_inventory)/total_theoretical)*100:.1f}%")
    print("-" * 50)
    
    # Highlight Design Inefficiency
    total_waste = project['Waste_Gap_mm'].sum()
    if total_waste > 1000:
        print(f"⚠️ DESIGN ALERT: Total width gaps equal {total_waste/1000}m of custom timber.")
        print("Recommendation: Standardize wall widths to multiples of 600mm.")
    
    print("="*50 + "\n")

if __name__ == "__main__":
    run_optimization()