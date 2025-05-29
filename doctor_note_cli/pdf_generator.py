from fpdf import FPDF

def generate_pdf(note, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, f"Patient Name: {note.patient_name}", ln=True)
    pdf.cell(0, 10, f"Diagnosis: {note.diagnosis}", ln=True)
    pdf.cell(0, 10, f"Date: {note.date}", ln=True)
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"Notes:\n{note.notes_text}")

    pdf.output(filename)
    print(f"Saved PDF as {filename}")
