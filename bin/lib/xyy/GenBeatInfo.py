import random
import math

spain_name=[]
spain_name.append('Rodrigo Andres')
spain_name.append('Andres Montenegro')
spain_name.append('Hector Marcelo')
spain_name.append('Damian Alejandro')
spain_name.append('Pablo Emanuel')
spain_name.append('Jesus Eduardo')
spain_name.append('Christian Mauricio')
spain_name.append('Juan Martin')
spain_name.append('Jose Luis')
spain_name.append('Paula Alejandra')
spain_name.append('Claudia Nayira')
spain_name.append('Lidia Isabel')
spain_name.append('Luis Sergio')
spain_name.append('Marlon Fabian')
spain_name.append('Jhon Alejandro')
spain_name.append('Victor Arquimides')
spain_name.append('Carlos Manuel')
spain_name.append('Cristian Luis')
spain_name.append('Cesar Alfredo')
spain_name.append('Moises Hugo')
spain_name.append('Carlos Gustavo')
spain_name.append('Diego Mario')
spain_name.append('Luis German')
spain_name.append('Victor Guillermo')
spain_name.append('Miguel Eugenio')
spain_name.append('Hector Francisco')
spain_name.append('Rigoberto Sady')
spain_name.append('Luis Humberto')
spain_name.append('Cristian Eduardo')
spain_name.append('Andres Ariel')
spain_name.append('Luis Atiliano')
spain_name.append('Guillermo Antonio')
spain_name.append('Luis Andres')
spain_name.append('Victor Adan')
spain_name.append('Ronald Alberto')
spain_name.append('Eduardo Felipe')
spain_name.append('Daniel Alejandro')
spain_name.append('Paulina Andrea')
spain_name.append('Sergio Luis')
spain_name.append('Oscar Victor')
spain_name.append('Maria Elena')
spain_name.append('Renato Luiz')
spain_name.append('Ruben Adrian')
spain_name.append('Omar Guillermo')
spain_name.append('Alejandro Alfredo')
spain_name.append('Michael Nicolas')
spain_name.append('Marcio Luiz')
spain_name.append('Ernesto Eugenio')
spain_name.append('Luis Miguel')
spain_name.append('Jose Mauricio')
spain_name.append('Patricio Abraham')
spain_name.append('Fiorella Tereza')
spain_name.append('Rigoberto Sergio')
spain_name.append('Ricardo Joaquin')
spain_name.append('Carlos Antonio')
spain_name.append('Mario Hernan')
spain_name.append('Miguel Alberto')
spain_name.append('Felipe Alejandro')
spain_name.append('Cristian Manuel')
spain_name.append('Ricardo Alejandro')
spain_name.append('Claudia Margarita')
spain_name.append('Julian Patricio')
spain_name.append('David Ricardo')
spain_name.append('Maria Antonieta')
spain_name.append('Maria Irene')
spain_name.append('Manuel Francisco')
spain_name.append('Ramiro Danilo')
spain_name.append('Marcela Alejandra')
spain_name.append('Silvana Teresa')
spain_name.append('Carlos Fabian')
spain_name.append('Rene Fernando')
spain_name.append('Juan Victor')
spain_name.append('Katherine Marisol')
spain_name.append('Boris Romulo')
spain_name.append('Guadalupe Francisca')
spain_name.append('Claudio Alfredo')
spain_name.append('Silvia Lorena')
spain_name.append('Leonardo Isaac')
spain_name.append('Juan Marcos')
spain_name.append('Hugo Benedicto')
spain_name.append('Marcelo Felipe')
spain_name.append('Miguel Claudio')
spain_name.append('Gloria Andrea')
spain_name.append('Omar Leopoldo')
spain_name.append('Fernando Alberto')
spain_name.append('Marcela Cristina')
spain_name.append('Juan Fernando')
spain_name.append('David Bernardo')
spain_name.append('Juan Rolando')
spain_name.append('Rodrigo Benjamin')
spain_name.append('Daniela Andrea')
spain_name.append('Hugo Enrique')
spain_name.append('Mathias Enrique')
spain_name.append('Pablo Martin')
spain_name.append('Sebastian Ruben')
spain_name.append('Eden Ernesto')
spain_name.append('Sebastian Adolfo')
spain_name.append('Maria Felisa')
spain_name.append('Esteban Giuliano')
spain_name.append('Nelson Bernabe')
spain_name.append('Rodrigo Antonio')
spain_name.append('Adolfo Alamiro')
spain_name.append('Ricardo Enrique')
spain_name.append('Sebastian Alexis')
spain_name.append('Carolina Angelica')
spain_name.append('Carol Andrea')
spain_name.append('Gerardo Sebastian')
spain_name.append('Amelia Viviana')
spain_name.append('Ana Mabel')
spain_name.append('Jose Leonel')

spain_family=[]
spain_family.append('Rodriguez Faundez')
spain_family.append('Vargas Quintana')
spain_family.append('Ruben Tocas Julian')
spain_family.append('Gomez Sanchez')
spain_family.append('Scout Mundial')
spain_family.append('Hoffens Dieguez')
spain_family.append('Gonzalez Manriquez')
spain_family.append('Jimenez Fernandez')
spain_family.append('Osses Molina')
spain_family.append('Fernandez Silva')
spain_family.append('Mendoza Jimenez')
spain_family.append('Juarez Maceda')
spain_family.append('Osses Lucero')
spain_family.append('Ellis Monreal')
spain_family.append('Julio Gonzalez')
spain_family.append('Antonio Munoz Pezoa')
spain_family.append('Lorenzini Villegas')
spain_family.append('Iturrieta Nunez')
spain_family.append('Aguirre Mendoza')
spain_family.append('Mendoza Diaz')
spain_family.append('Figueroa Arriagada')
spain_family.append('Jimenez Venegas')
spain_family.append('Torres Lombardi')
spain_family.append('Soto Sepulveda')
spain_family.append('Aceiton Navarro')
spain_family.append('Sandoval Juan Ruben')
spain_family.append('Maria Sanchez')
spain_family.append('Silva Soler')
spain_family.append('Acevedo Rivera')
spain_family.append('Schilling Vergara')
spain_family.append('Figueroa Garrido')
spain_family.append('Avendano Miranda')
spain_family.append('Ramos Salas')
spain_family.append('Mella Chepo')
spain_family.append('Aroca Oliva')
spain_family.append('Labra Moya')

car_type=[]
car_type.append('Toyota,Corolla 2017')
car_type.append('Renault,Clio 2016')
car_type.append('Peugeot,206 2015')
car_type.append('Volkswagen,Golf 2018')
car_type.append('Volkswagen,Polo 2017')
car_type.append('Mazda,CX-3 2017')
car_type.append('Kia,Morning 2016')
car_type.append('Kia,Rio 2018')
car_type.append('Chevrolet,Sail 2018')
car_type.append('Suzuki,Celerio 2019')
car_type.append('Great Wall,C30 2019')
car_type.append('Kia,Morning 2019')
car_type.append('Kia,Rio 2015')
car_type.append('Renault,Fluence 2015')
car_type.append('LIFAN,LFX50 2015')
car_type.append('Peugeot,207 2009')
car_type.append('Chery,Arrizo 3 2018')
car_type.append('Great Wall,Haval H6 2019')
car_type.append('Chery,Arrizo 5 2018')
car_type.append('Chevrolet,Spark 2016')
car_type.append('Hyundai,Grand i10 2019')
car_type.append('Chevrolet,Onix 2019')
car_type.append('Volkswagen,Vouage Trendline 2019')
car_type.append('Suzuki,Celerio 2019')
car_type.append('SSANGYONG,Korando 2014')
car_type.append('Kia,Rio 2011')
car_type.append('Chery,IQ 2016')
car_type.append('Kia,Cerato 2013')
car_type.append('Toyota,RAV4 2014')
car_type.append('Nissan,Versa 2019')
car_type.append('Kia,Sportage 2018')
car_type.append('Volkswagen,Vouage Power 2018')
car_type.append('Hyundai,i10 2017')
car_type.append('Chevrolet,Aveo 2013')
car_type.append('Baic,X35 2017')
car_type.append('Chevrolet,Prisma 2019')
car_type.append('Fiat,Uno 2019')
car_type.append('Mg,ZS 2019')
car_type.append('Nissan,Qashqai 2012')
car_type.append('Citroen,C-Elysee 2019')
car_type.append('Chevrolet,Sail 2016')
car_type.append('Mitsubishi,MIRAGE GL 2018')
car_type.append('Nissan,March 2013')
car_type.append('Peugeot,301 2019')
car_type.append('Hyundai,Accent 2018')
car_type.append('JAC,S2 2019')
car_type.append('Renault,Symbol 2018')
car_type.append('Chevrolet,Sail Sedan Classic 2011')
car_type.append('Kia,Morning 2013')
car_type.append('Chevrolet,Spark 2013')
car_type.append('Chevrolet,Spark 2013')

word=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

class beat_info:
    def dirver_name(self):
        first_name=spain_name[random.randint(0,len(spain_name)-1)]
        last_name=spain_family[random.randint(0,len(spain_family)-1)]
        full_name=first_name+' '+last_name
        return full_name
    def drive_license(self):
        #LJCX981
        first=word[random.randint(0,25)]
        second=word[random.randint(0,25)]
        third=word[random.randint(0,25)]
        forth=word[random.randint(0,25)]
        fifth=str(random.randint(0,9))
        sixth=str(random.randint(0,9))
        seventh=str(random.randint(0,9))
        car_no=first+second+third+forth+fifth+sixth
        return car_no
    def car(self):
        car_type[random.randint(0,49)]
        return car_type[random.randint(0,49)]


class beat_payment:
    def payment_format(self,amount,interval):
        interval=random.randint(0,interval//50)*50
        if random.randint(0,1)==1:
            pay_amt=amount+interval*-1
        else:
            pay_amt=amount+interval
        len_str=len(str(pay_amt))
        pay_amt=math.ceil(pay_amt/10)*10
        if len_str>3:
            pay_amt=str(pay_amt)[:-3]+','+str(pay_amt)[-3:]
        return pay_amt

class beat_pdf:
    def create_html_file(self,come_add,back_add,pay_amt,come_time,dirver_name,car_name,car_no):
        html_content="""<!DOCTYPE html>
        <html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
            <title>mybeat</title>
            <style>
                body {
                    background-color: white;
                }
                * {
                    font-family: Helvetica, Arial, sans-serif;
                    color: #262626;
                }
                main {
                    margin: 20px auto 0;
                    max-width: 400px;
                    padding: 16px 30px 40px;
                    border-radius: 5px;
                    border: 1px #CCC solid;
                    box-sizing: border-box;
                }
                h1 {
                    margin: 0;
                }
                h2 {
                    font-size: 16px;
                    border-bottom: 1px black solid;
                    padding-bottom: 5px;
                }
                hr {
                    border-color: #EEE;
                    margin: 10px 0;
                }
                label {
                    margin: 0;
                    font-weight: lighter;
                }
                label, .details-text, .payment-text {
                    font-size: 12px;
                }
                pre {
                    width: 340px;
                    margin: 20px auto;
                    font-family: Helvetica, Arial, sans-serif;
                    font-size: 7px;
                    color: #262626;
                }
                .logo {
                    max-width: 120px;
                    display: block;
                    margin-bottom: 30px;
                }
                .details {
                    margin-top: 30px;
                }

                .details-text {
                    font-weight: bold;
                }
                .payment-text {
                    float: right;
                    clear: right;
                    text-align: right;
                    font-weight: bold;
                }
                .clearfix:after {
                    content: " ";
                    display: table;
                }
                .clearfix:before {
                    content: " ";
                    display: table;
                }
                @media only screen and (max-width: 420px) {
                    main {
                        margin-top: 0;
                    }
                }
            </style>
        </head>
        <body>
        <main>
            <header>
                <img class="logo" src="../bin/logo.png" alt="Taxibeat">
            </header>
            <section class="payment">
                <header>
                    <h2>Ride Receipt</h2>
                </header>
                <div>
                    <label>Payment</label>
                    <div class="payment-text">
                            Cash
                    </div>
                </div>
                <hr>
                <div class="clearfix">
                    <label>Total Fare</label>
                    <div class="payment-text">$"""+str(pay_amt)+"""</div>
                </div>
            </section>
            <section class="details">
                <header>
                    <h2>Ride Summary</h2>
                </header>
                <label>Date &amp; Time</label>
                <div class="details-text">
                    <time datetime="2019-10-19 13:57:49">"""+str(come_time)+"""</time>
                </div>
                <hr>
                <label>Pickup Address</label>
                <div class="details-text">"""+come_add+"""</div>
                    <hr>
                    <label>Drop-off Address</label>
                    <div class="details-text">"""+back_add+"""</div>
                <hr>
                <label>Driver</label>
                <div class="details-text">"""+dirver_name+"""</div>
                    <hr>
                    <label>Car</label>
                    <div class="details-text">"""+car_name+"""</div>
                    <hr>
                    <label>License Plates</label>
                    <div class="details-text">"""+car_no+"""</div>
            </section>
        </main>
        </body></html>"""
        htm_file=open('../output/temp.html','w')
        htm_file.write(html_content)
        htm_file.close()
        return 1