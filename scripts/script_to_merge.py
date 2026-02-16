import os
import nbformat
from nbconvert import PDFExporter

notebooks = [
    'cleaned_data.ipynb',
    'expense_type_breakdown.ipynb',
    'high_value_transactions',
    'monthly_spending_trends',
    'supplier_type_comparison',
    'top_suppliers_analysis',
    'years_comparison_analysis'
    # add other notebooks
]

for nb in notebooks:
    os.system(f'jupyter nbconvert --to pdf {nb}')

# Then manually merge PDFs or use PyPDF2