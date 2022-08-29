from importlib.resources import open_text
from escpos.printer import Serial

def print_invoice(seller,ccode, customer, item_list, total, total_itbis, evento):
      
    a = '/dev/ttyACM0'
    
    p = Serial(devfile   = a,
                baudrate = 9600,
                bytesize = 8,
                parity   = 'N',
                stopbits = 1,
                timeout  = 1.00,
                dsrdtr   = True)

    p.image('branx_sources/logo_negocio.jpg')

    # Adress and contact
    p.set(align       = 'left',
          font        = 'b', 
          bold        = False, 
          width       = 2, 
          height      = 1, 
          smooth      = True, 
          custom_size = True)

    p.text("Dirección: C/Eusebio Puello #65, Mercado Municipal,\nSan Juan de la Maguana.\n")
    p.text("Teléfono: (809) 557-5259 \n \n")
    
    p.text(f'Atendido por {seller} \n \n')

    p.text(f'Vendido a {customer} \n {ccode} \n \n')

    # Legend of the text
    p.set(align       = 'left',
          font        = 'a', 
          bold        = True, 
          width       = 1, 
          height      = 2, 
          smooth      = True, 
          custom_size = True)


    p.text('------------------------------------------------\n')
    p.text('* Articulo \nPrecio       ITBIS        Cantidad      Subtotal\n')
    p.text('------------------------------------------------\n')

    # Description uses 24 chars and a break
    # Price uses 8 chars, qty uses 6 chars and total uses 10 chars

    p.set(align       = 'left',
          font        = 'a', 
          bold        = False, 
          width       = 1, 
          height      = 2, 
          smooth      = True, 
          custom_size = True)
    
    try:
        for item in item_list:
            p.text(f'{item[1]:<30} \n{item[2]:<12}{item[3]:<12}{item[4]:<10}{item[5]:<16}\n')
           
    except:
        a = item_list
        p.text(f'{a[1]:<24} \n{a[2]:<8}{a[3]:<8}{a[3]:<6}{a[4]:<10}\n')

    p.set(align       = 'right',
          font        = 'a', 
          bold        = False, 
          width       = 2, 
          height      = 1, 
          smooth      = True, 
          custom_size = True)

    p.text('------------------------\n')
    p.text(f'Total ITBIS = {total_itbis} \n')    
    p.text('------------------------\n')

    p.text('------------------------\n')
    p.text(f'Total a pagar = {total} \n')    
    p.text('------------------------\n')

    p.set(align       = 'center',
          font        = 'a', 
          bold        = False, 
          width       = 2, 
          height      = 1, 
          smooth      = True, 
          custom_size = True)
    
    p1 = evento[0:11]
    p2 = evento[11:22]
    p3 = evento[22:32]
    p.barcode('{B'+f'{p1}', 'CODE128', function_type='B')
    p.barcode('{B'+f'{p2}', 'CODE128', function_type='B')
    p.barcode('{B'+f'{p3}', 'CODE128', function_type='B')   
    p.cut()

if __name__ == '__main__':
    print_invoice('Randhal', '40211821331', 'Moreno', ['','Descripcion', 'Precio', 'Cantidad', 'Subtotal'], '451', '11', '21806e2a1d9211edbf75a8a7956a446a')
    #pass
    pass