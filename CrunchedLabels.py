# from fpdf import FPDF
pdf = FPDF()
pdf.set_margins(left=30, right=1, top=15)


prod_code = "M8215"
prod_name = "Crunch Coir"
location = "Koco & Koir Exports Pvt Ltd, #236 Rasipalayam, Coimbatore, India"
order_no = input("please enter order number: ")
date = input("please enter date of production: ")
pcs = "228"
container = input("please enter container number: ")


for i in range(20):
    weight = input("please input weight: ")
    for j in range (2):
    
        pdf.add_page(orientation="L") #Landscape
        pdf.rect(10,10,275,190,"D") #Border
        
        pdf.set_font("Arial", size = 26)
        pdf.rect(15,15,267,30,"D") #Border
        # create a cell
        pdf.cell(0, 15, txt = "PTH SKU                               :" + prod_code, ln = 1, align = 'L')#, border=1
        pdf.cell(0, 15, txt = "PTH SKU DESCRIPTION     :" + prod_name, ln = 2, align = 'L') 
        
        pdf.cell(0, 15, txt = "", ln = 3, align = 'L') #spacer
        pdf.set_font("Arial", size = 20)
        pdf.rect(15,60,267,60,"D") #Border
        pdf.cell(0, 15, txt = "Supplier  : " + location, ln = 4, align = 'L') 
        pdf.cell(0, 15, txt = "PTH Purchase Order Number    :" + order_no, ln = 5, align = 'L') 
        pdf.cell(0, 15, txt = "Production Date                         :" + date, ln = 6, align = 'L') 
        pdf.cell(0, 15, txt = "Production Lot No                      :" + str(i) + "/20", ln = 7, align = 'L') 
        
        pdf.cell(0, 10, txt = "", ln = 8, align = 'L')  #spacer
        pdf.set_font("Arial", size = 20)
        pdf.rect(15,130,267,30,"D") #Border
        pdf.cell(0, 15, txt = "Total Quantity on this Pallet (W/Unit of Measure)               : " + pcs + "pcs", ln = 9, align = 'L') 
        pdf.cell(0, 15, txt = "Pallet Gross Weight (Kgs)                                                   : " + weight + "Kgs", ln = 10, align = 'L') 
        
        pdf.cell(0, 10, txt = "", ln = 11, align = 'L')  #spacer
        pdf.set_font("Arial", size = 26)
        pdf.rect(15,170,267,15,"D") #Border
        pdf.cell(0, 15, txt = "Supplier Info : " + container, ln = 12, align = 'L') 
        
        

# save the pdf with name .pdf
pdf.output("PLTK_Labels.pdf")
