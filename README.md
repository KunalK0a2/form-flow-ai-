# FormFlow AI: Next-Gen Formwork Optimization 🏗️⚡

**National Competition Prototype | Sector: CreaTech & Construction 4.0**

FormFlow AI is a data-driven web application engineered to optimize construction formwork logistics, reduce capital outlay, and minimize environmental impact. By ingesting BIM (Building Information Modeling) data, the system provides 4D inventory lifecycle visualization, geometric kitting logic, and carbon offset tracking.

## 🚀 Key Features

* **Dynamic Kitting Logic:** Automatically calculates the exact mix of main panels, support props, and fasteners required for specific wall dimensions.
* **4D Temporal Flow Analysis:** Simulates daily site activity and reconditioning buffers to determine true peak inventory demand, preventing over-procurement.
* **Carbon Offset Tracking:** Quantifies environmental savings (in kg of CO2) achieved by reducing the total number of manufactured panels.
* **Design Standardization Analytics:** Identifies dimensional inefficiencies in architectural designs, flagging segments requiring custom timber fillers.
* **Logistics Dispatch:** Generates a daily dispatch manifest for precise on-site deliveries.

## 📂 Repository Structure

Ensure your GitHub repository looks exactly like this before deploying:

my-streamlit-app/
├── app.py                  # Main Streamlit dashboard and UI presentation layer
├── optimizer.py            # Core engine for geometric kitting and peak demand analysis
├── requirements.txt        # Python dependencies (streamlit, pandas, plotly)
├── project_data.csv        # Structural BIM dataset (Required to prevent crash)
├── inventory_types.csv     # Formwork system definitions (Required to prevent crash)
└── README.md               # Project documentation

## 🌐 Zero-Git Deployment Guide (Streamlit Community Cloud)

This project is configured for instant deployment without using the command line. Follow these exact steps to get the app live:

### Step 1: Upload Files to GitHub
1. Log in to GitHub and create a **New repository**.
2. Check the box to **"Add a README file"** and click **Create repository**.
3. On your new repository page, click **Add file** > **Upload files**.
4. Drag and drop `app.py`, `optimizer.py`, `requirements.txt`, `project_data.csv`, and `inventory_types.csv` into the browser.
5. Click the green **Commit changes** button.

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/) and click **Continue with GitHub**.
2. Click the **New app** button.
3. Select the GitHub repository you just created.
4. Set the **Branch** to `main` (or `master`).
5. Set the **Main file path** to `app.py`.
6. Click **Deploy!** Streamlit will automatically read the `requirements.txt` file, install the necessary libraries, and provide you with a live URL to share.

## 🛠️ Local Execution Setup

If you prefer to run this prototype locally on your machine for testing:

1. Clone the repository:
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. Install the required dependencies:
   pip install -r requirements.txt

3. Run the application:
   streamlit run app.py

## 👨‍💻 Author
**Kunal Kapoor** B.Tech Information Technology (Class of 2027)  
Manipal Institute of Technology (MIT), Manipal
