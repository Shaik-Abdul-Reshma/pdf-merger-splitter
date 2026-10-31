# PDF Merger & Splitter - Codtech Task 4
# Intern ID: CITS9867 | Name: Shaik Abdul Reshma

import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

def merge_pdfs():
    print("\n--- PDF MERGER ---")
    print("Put all PDFs to merge in same folder as this script")
    pdfs = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    
    if len(pdfs) < 2:
        print(f"Found {len(pdfs)} PDF(s). Need at least 2 PDFs to merge.")
        print("Found files:", pdfs)
        return

    print("\nFound PDFs:")
    for i, pdf in enumerate(pdfs, 1):
        print(f"{i}. {pdf}")

    merger = PdfMerger()
    for pdf in pdfs:
        try:
            merger.append(pdf)
            print(f"Added: {pdf}")
        except Exception as e:
            print(f"Error adding {pdf}: {e}")

    output = input("\nEnter output merged file name (default: merged.pdf): ").strip()
    if not output:
        output = "merged.pdf"
    if not output.lower().endswith('.pdf'):
        output += ".pdf"

    merger.write(output)
    merger.close()
    print(f"\nSUCCESS! Merged PDF saved as: {output}")

def split_pdf():
    print("\n--- PDF SPLITTER ---")
    pdfs = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    if not pdfs:
        print("No PDF found in current folder!")
        return

    print("\nAvailable PDFs:")
    for i, pdf in enumerate(pdfs, 1):
        print(f"{i}. {pdf}")

    try:
        choice = int(input("\nEnter PDF number to split: "))
        input_pdf = pdfs[choice-1]
    except:
        print("Invalid choice!")
        return

    try:
        reader = PdfReader(input_pdf)
        total = len(reader.pages)
        print(f"\n{input_pdf} has {total} pages.")

        print("\n1. Split into single pages")
        print("2. Split by page range")
        mode = input("Choose mode (1/2): ").strip()

        if mode == "1":
            for i in range(total):
                writer = PdfWriter()
                writer.add_page(reader.pages[i])
                out_name = f"{input_pdf[:-4]}_page_{i+1}.pdf"
                with open(out_name, "wb") as f:
                    writer.write(f)
                print(f"Created: {out_name}")
            print("\nSUCCESS! Split into single pages done.")

        elif mode == "2":
            start = int(input(f"Enter start page (1-{total}): ")) - 1
            end = int(input(f"Enter end page (1-{total}): ")) - 1
            if start < 0 or end >= total or start > end:
                print("Invalid page range!")
                return
            writer = PdfWriter()
            for i in range(start, end+1):
                writer.add_page(reader.pages[i])
            out_name = f"{input_pdf[:-4]}_pages_{start+1}-{end+1}.pdf"
            with open(out_name, "wb") as f:
                writer.write(f)
            print(f"\nSUCCESS! Created: {out_name}")
        else:
            print("Invalid mode!")

    except Exception as e:
        print(f"Error: {e}")

def main():
    print("="*50)
    print("PDF MERGER & SPLITTER - Reshma CITS9867")
    print("="*50)
    print("Make sure PyPDF2 is installed: pip install PyPDF2")
    
    while True:
        print("\n1. Merge PDFs")
        print("2. Split PDF")
        print("3. Exit")
        ch = input("Enter choice (1/2/3): ").strip()
        
        if ch == "1":
            merge_pdfs()
        elif ch == "2":
            split_pdf()
        elif ch == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
