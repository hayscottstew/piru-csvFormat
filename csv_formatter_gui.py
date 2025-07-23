import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from pathlib import Path

class CSVFormatterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Formatter Tool")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        # Define the columns to keep, based on your macro
        self.keep_cols = [
            "Input_Property_Address", "Input_Property_City", "Input_Property_State", "Input_Property_Zip",
            "Email1", "Email2", "Email3", "OWNER_FIRST_NAME", "OWNER_LAST_NAME",
            "Mailing_Zip", "Mailing_State", "Mailing_City", "Mailing_Address",
            "EQUITY_PERCENT", "EQUITY", "Data_Mailing_Address", "Data_Mailing_City",
            "Data_Mailing_State", "Data_Mailing_Zip"
        ]
        
        # Define the phone number columns to unpivot
        self.phone_cols = [f"Phone{i}_Number" for i in range(1, 11)]
        
        self.input_file_path = None
        self.output_file_path = None
        
        self.setup_ui()
    
    def setup_ui(self):
        # Create main frame with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="CSV Formatter Tool", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Input file selection
        ttk.Label(main_frame, text="Input CSV File:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.input_file_var = tk.StringVar()
        self.input_entry = ttk.Entry(main_frame, textvariable=self.input_file_var, width=50)
        self.input_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(10, 5), pady=5)
        ttk.Button(main_frame, text="Browse", 
                  command=self.select_input_file).grid(row=1, column=2, pady=5)
        
        # Output file selection
        ttk.Label(main_frame, text="Output Location:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.output_file_var = tk.StringVar()
        self.output_entry = ttk.Entry(main_frame, textvariable=self.output_file_var, width=50)
        self.output_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(10, 5), pady=5)
        ttk.Button(main_frame, text="Browse", 
                  command=self.select_output_file).grid(row=2, column=2, pady=5)
        
        # Process button
        self.process_button = ttk.Button(main_frame, text="Format CSV", 
                                       command=self.process_csv, 
                                       style="Accent.TButton")
        self.process_button.grid(row=3, column=0, columnspan=3, pady=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # Status/Log area
        ttk.Label(main_frame, text="Status:").grid(row=5, column=0, sticky=tk.W, pady=(10, 5))
        
        # Create a frame for the text widget and scrollbar
        text_frame = ttk.Frame(main_frame)
        text_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)
        
        self.status_text = tk.Text(text_frame, height=8, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.status_text.yview)
        self.status_text.configure(yscrollcommand=scrollbar.set)
        
        self.status_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Configure main_frame row weights for the text area to expand
        main_frame.rowconfigure(6, weight=1)
        
        # Add initial status message
        self.log_message("Ready to format CSV files. Please select an input file to begin.")
    
    def log_message(self, message):
        """Add a message to the status text area"""
        self.status_text.insert(tk.END, f"{message}\n")
        self.status_text.see(tk.END)
        self.root.update_idletasks()
    
    def select_input_file(self):
        """Open file dialog to select input CSV file"""
        file_path = filedialog.askopenfilename(
            title="Select CSV file to format",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if file_path:
            self.input_file_path = file_path
            self.input_file_var.set(file_path)
            
            # Auto-suggest output filename
            input_dir = os.path.dirname(file_path)
            input_name = Path(file_path).stem
            suggested_output = os.path.join(input_dir, f"Formatted_{input_name}.csv")
            self.output_file_var.set(suggested_output)
            
            self.log_message(f"Selected input file: {os.path.basename(file_path)}")
    
    def select_output_file(self):
        """Open file dialog to select output location"""
        file_path = filedialog.asksaveasfilename(
            title="Save formatted CSV as...",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if file_path:
            self.output_file_path = file_path
            self.output_file_var.set(file_path)
            self.log_message(f"Output will be saved to: {os.path.basename(file_path)}")
    
    def process_csv(self):
        """Process the CSV file with the formatting logic"""
        if not self.input_file_path:
            messagebox.showerror("Error", "Please select an input CSV file first.")
            return
        
        if not self.output_file_var.get():
            messagebox.showerror("Error", "Please specify an output location.")
            return
        
        try:
            # Start progress indicator
            self.progress.start()
            self.process_button.config(state='disabled')
            
            self.log_message("Starting CSV formatting process...")
            
            # Load the data
            self.log_message(f"Loading data from {os.path.basename(self.input_file_path)}...")
            df = pd.read_csv(self.input_file_path)
            self.log_message(f"Loaded {len(df)} rows of data.")
            
            # Check if required columns exist
            missing_cols = [col for col in self.keep_cols if col not in df.columns]
            missing_phone_cols = [col for col in self.phone_cols if col not in df.columns]
            
            if missing_cols:
                self.log_message(f"Warning: Missing expected columns: {missing_cols}")
            
            if missing_phone_cols:
                self.log_message(f"Warning: Missing phone columns: {missing_phone_cols}")
            
            # Use only the columns that actually exist
            available_keep_cols = [col for col in self.keep_cols if col in df.columns]
            available_phone_cols = [col for col in self.phone_cols if col in df.columns]
            
            self.log_message(f"Using {len(available_keep_cols)} main columns and {len(available_phone_cols)} phone columns.")
            
            # Melt the DataFrame to unpivot the phone numbers
            self.log_message("Unpivoting phone number columns...")
            unpivoted_df = df.melt(
                id_vars=available_keep_cols,
                value_vars=available_phone_cols,
                var_name='Phone_Source',
                value_name='Phone_Number'
            )
            
            # Drop rows where the phone number is missing
            rows_before = len(unpivoted_df)
            unpivoted_df.dropna(subset=['Phone_Number'], inplace=True)
            rows_after = len(unpivoted_df)
            self.log_message(f"Removed {rows_before - rows_after} rows with missing phone numbers.")
            
            # Convert phone numbers to integers to remove decimal points
            self.log_message("Converting phone numbers to integers...")
            unpivoted_df['Phone_Number'] = unpivoted_df['Phone_Number'].astype(int)
            
            # Clean up the 'Phone_Source' column
            unpivoted_df.drop(columns=['Phone_Source'], inplace=True)
            
            # Save the formatted data
            output_path = self.output_file_var.get()
            self.log_message(f"Saving formatted data to {os.path.basename(output_path)}...")
            unpivoted_df.to_csv(output_path, index=False)
            
            self.log_message(f"✅ SUCCESS! Formatted data saved with {len(unpivoted_df)} rows.")
            messagebox.showinfo("Success", f"CSV formatting completed successfully!\n\nOutput saved to:\n{output_path}")
            
        except Exception as e:
            error_msg = f"Error processing CSV: {str(e)}"
            self.log_message(f"❌ ERROR: {error_msg}")
            messagebox.showerror("Error", error_msg)
        
        finally:
            # Stop progress indicator and re-enable button
            self.progress.stop()
            self.process_button.config(state='normal')

def main():
    root = tk.Tk()
    app = CSVFormatterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 