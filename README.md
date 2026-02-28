# FormFlow AI: Next-Gen Formwork Optimization 🏗️⚡

**National Competition Prototype | Sector: CreaTech & Construction 4.0**

FormFlow AI is a data-driven web application engineered to optimize construction formwork logistics, reduce capital outlay, and minimize environmental impact. 

**🔗 [Link to Live Application](https://formflowai.streamlit.app/)**

## 🚀 Key Features

* **BIM Data Ingestion:** Seamlessly process structural CSV data to evaluate site requirements instantly.
* **Dynamic Kitting Logic:** Automatically calculates the exact mix of main panels, support props, and fasteners required for specific wall dimensions.
* **4D Temporal Flow Analysis:** Simulates daily site activity and reconditioning buffers to determine true peak inventory demand, preventing costly over-procurement.
* **Carbon Offset Tracking:** Quantifies environmental savings (in kg of CO2) achieved by reducing the total number of manufactured panels through optimized sharing.
* **Design Standardization Analytics:** Identifies dimensional inefficiencies in architectural designs, flagging structural segments that require custom timber fillers to minimize waste.
* **Logistics Dispatch:** Generates a daily, sortable dispatch manifest for precise on-site deliveries.

## 📖 How to Use the Website

Using the FormFlow AI dashboard is designed to be straightforward for project managers and logistics coordinators.

### Step 1: Upload Your Data
* Navigate to the **🕹️ Control Center** in the left sidebar.
* Click **"Browse files"** under the **Upload BIM Data (CSV)** section and upload your project's structural dataset or you can use the project dataset from this github repository . 
* *(Note: The CSV must contain `PourDate` and `Width_mm` columns for the engine to process the geometry and timeline).*

### Step 2: Configure Constraints
* **Reconditioning Buffer (Days):** Use the slider in the sidebar to define how many days a panel needs for curing, stripping, and cleaning before it can be reused on another wall.
* **CO2 Factor:** Adjust the "CO2 kg per Panel Mfg" input based on the specific manufacturing emissions of your chosen formwork system.

### Step 3: Analyze the Dashboard
Once the data is processed, the main dashboard will populate automatically:
* **National Level Metrics:** Review your top-line ROI, including your Optimized Inventory peak, Procurement Alpha (savings %), and total Carbon Offset.
* **4D Lifecycle Visualization:** Hover over the interactive area chart to see exactly how many panels are active on any given day compared to your peak demand limit.
* **Standardization Report:** Check the alerts below the chart to see if any walls need redesigning to fit standard 600mm modules, complete with exact gap measurements.
* **Daily Dispatch Manifest:** Click the expander at the bottom of the page (`🚚 View Daily Dispatch Manifest`) to view and export the exact components needed for each specific pour date and area.

---
**Author:** Kunal Kapoor | B.Tech Information Technology | Manipal Institute of Technology
