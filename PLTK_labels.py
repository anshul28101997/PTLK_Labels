from fpdf import FPDF
pdf = FPDF()
pdf.set_margins(left=30, right=1, top=15)


prod_name = "Biofilter 4.5Kg Bales"
prod_class = "Biofilter CBM 105"
order_no = input("please enter order number: ")
date = input("please enter date of production: ")
container = input("please enter container number: ")
location = "Koco & Koir Exports Pvt Ltd"
country = "India"

for i in range(20):
	weight = input("please input weight: ")
	for j in range (2):
	
		pdf.add_page(orientation="L") #Landscape
		pdf.rect(10,10,275,190,"D") #Border
		pdf.set_font("Arial", size = 32)
		# create a cell
		pdf.cell(0, 19, txt = "Product Name      :"+prod_name, ln = 1, align = 'L') #, border=1
		pdf.cell(0, 19, txt = "Product Class       :"+prod_class, ln = 2, align = 'L')
		pdf.cell(0, 19, txt = "Order Number      :"+order_no, ln = 3, align = 'L')
		pdf.cell(0, 19, txt = "Pallet Number      :"+str(i+1)+" of 20", ln = 4, align = 'L')
		pdf.cell(0, 19, txt = "Quantity               :"+str(weight)+"Kg", ln = 5, align = 'L')
		pdf.cell(0, 19, txt = "Production Date   :"+date, ln = 6, align = 'L')
		pdf.cell(0, 19, txt = "Container No.      :"+container, ln = 7, align = 'L')
		pdf.cell(0, 19, txt = "Location               :"+location, ln = 8, align = 'L')
		pdf.cell(0, 19, txt = "Country of Origin  :"+country, ln = 9, align = 'L')

# save the pdf with name .pdf
pdf.output("PLTK_Labels.pdf")
