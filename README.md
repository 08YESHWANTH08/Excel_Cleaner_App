# 🧹 Excel Cleaner

The **Excel Cleaner** is a simple data engineering utility built using Python to automate the process of cleaning and merging Excel files. This project was created as a learning experience to understand how data preprocessing works, especially in real-world spreadsheet data.

## 🚀 Project Highlights

- Merge multiple Excel files
- Clean redundant or dirty data
- Export a well-formatted output Excel file
- Lightweight and fast
- Runs locally using a virtual environment

## 📂 Folder Structure

```
Excel_Cleaner_App/
├── excel_cleaner.py         # Logic for data cleaning
├── merger.py                # Code to merge multiple Excel files
├── main.py                  # Entry point to trigger merging and cleaning
├── requirements.txt         # Python dependencies
├── files_to_work.txt        # List of files to clean (input)
├── LICENSE
```

## 🧪 Technologies Used

- **Python 3**
- **Pandas**
- **openpyxl**
- **Virtual Environment (venv)**

## 🛠️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Excel_Cleaner_App.git
   cd Excel_Cleaner_App
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Excel files and update `files_to_work.txt`**

5. **Run the main script:**
   ```bash
   python main.py
   ```

## 📈 Output

- A cleaned Excel file will be saved in your local directory.
- All specified input files from `files_to_work.txt` are processed.

## 🧠 What I Learned

This was my **first data engineering project**, and it gave me practical exposure to:
- Reading and writing Excel files using Python
- Data cleaning techniques
- File handling and modular programming
- Managing Python environments and dependencies

## 🤝 Contributing

Feel free to fork the repo and create pull requests to contribute improvements or new features.

## 📜 License

This project is licensed under the MIT License.
