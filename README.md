# 📊 Sales Data Analysis & Visualization

A simple modular Python project that loads sales data from a CSV file, processes it to calculate total sales by category, and generates a bar chart visualization.

---

## 📌 Project Overview

This project demonstrates an end-to-end data analysis workflow:

- Load sales data from a CSV file  
- Calculate total sales (Quantity × UnitPrice)  
- Group sales data by category  
- Generate a bar chart visualization  
- Save the output as an image file  

The final output is a bar chart (`report.png`) showing total sales for each category.

---

## 🛠️ Technologies Used

- Python 3.x  
- Pandas  
- Matplotlib  

---

## 📁 Project Structure

sales-data-analysis/
│
├── data/
│   └── sample_data.csv
│
├── data_loader.py
├── processor.py
├── reporter.py
├── main.py
│
├── report.png
├── requirements.txt
└── README.md

---

## 📂 File Explanation

### data_loader.py
Loads the CSV file using Pandas.

### processor.py
- Creates a new column:
  Total = Quantity × UnitPrice  
- Groups the data by Category  
- Calculates total sales per category  

### reporter.py
- Creates a bar chart using Matplotlib  
- Saves the chart as `report.png`

### main.py
Controls the full workflow:
1. Loads data  
2. Processes data  
3. Generates visualization  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/sales-data-analysis.git  
cd sales-data-analysis

### 2️⃣ (Optional but Recommended) Create Virtual Environment

python -m venv venv

Activate:

Windows:  
venv\Scripts\activate  

Mac/Linux:  
source venv/bin/activate  

### 3️⃣ Install Dependencies

pip install -r requirements.txt

If you don’t have a requirements file:

pip install pandas matplotlib

---

## ▶️ How to Run the Project

Run the main script:

python main.py

---

## 📊 Output

After running:

- Processed sales summary is displayed in the console.
- A bar chart is generated and saved as:

report.png

The visualization shows total sales for categories such as:
- Clothing  
- Electronics  
- Groceries  

---

## 🎯 Key Concepts Demonstrated

- Modular Python programming  
- Data processing using Pandas  
- Data aggregation using groupby  
- Data visualization using Matplotlib  
- Clean project structure  

---

## 🚀 Future Improvements

- Add error handling  
- Add logging functionality  
- Export processed summary to CSV  
- Build interactive dashboard using Streamlit  
- Add unit testing  

---

## 👩‍💻 Author

Sudeepthi Rao  
Aspiring Data Analyst

