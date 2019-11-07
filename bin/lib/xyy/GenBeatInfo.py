import random
import math

spain_name=[]
spain_name.append('Adelaida')
spain_name.append('Adio')
spain_name.append('Aedo')
spain_name.append('Alamillo')
spain_name.append('Arvelo')
spain_name.append('Baca')
spain_name.append('Barreda')
spain_name.append('Barriga')
spain_name.append('Barba')
spain_name.append('Baros')
spain_name.append('Benzo')
spain_name.append('Caccia')
spain_name.append('Canaro')
spain_name.append('Carnio')
spain_name.append('Caligo')
spain_name.append('Calvino')
spain_name.append('De Los Reyes')
spain_name.append('Delano')
spain_name.append('Dusi')
spain_name.append('Diokno')
spain_name.append('Diego')
spain_name.append('Elena')
spain_name.append('Ema')
spain_name.append('Emmanuel')
spain_name.append('Edelmiro')
spain_name.append('Elgueta')
spain_name.append('Fanjul')
spain_name.append('Felipez')
spain_name.append('Feliciano')
spain_name.append('Fazio')
spain_name.append('Frida')
spain_name.append('Gambino')
spain_name.append('Galo')
spain_name.append('Galicia')
spain_name.append('Galano')
spain_name.append('Garza')
spain_name.append('Gestido')
spain_name.append('Hilario')
spain_name.append('Henestrosa')
spain_name.append('Hugo')
spain_name.append('Hierro')
spain_name.append('Hermoso')
spain_name.append('Ignacio')
spain_name.append('Immanuel')
spain_name.append('Inirio')
spain_name.append('Irene')
spain_name.append('Isabel')
spain_name.append('Jaime')
spain_name.append('Jirado')
spain_name.append('Josefa')
spain_name.append('Juardo')
spain_name.append('Jorge')
spain_name.append('Juan')
spain_name.append('Labbe')
spain_name.append('Lama')
spain_name.append('Lara')
spain_name.append('Larrea')
spain_name.append('Laso')
spain_name.append('Latorre')
spain_name.append('Leguía')
spain_name.append('Lyon')
spain_name.append('Malo')
spain_name.append('Mendoza')
spain_name.append('Meza')
spain_name.append('Miquel')
spain_name.append('Musa')
spain_name.append('Moncada')
spain_name.append('Neto')
spain_name.append('Noelio')
spain_name.append('Navarro')
spain_name.append('Noelio')
spain_name.append('Nybia')
spain_name.append('Oderigo')
spain_name.append('Ocampos')
spain_name.append('Obagas')
spain_name.append('Obagas')
spain_name.append('Orfelio')
spain_name.append('Pablo')
spain_name.append('Palmes')
spain_name.append('Parga')
spain_name.append('Pavia')
spain_name.append('Pelaez')
spain_name.append('Pola')
spain_name.append('Quindos')
spain_name.append('Quevara')
spain_name.append('Quijano')
spain_name.append('Quinto')
spain_name.append('Ramasso')
spain_name.append('Rada')
spain_name.append('Rodrigo')
spain_name.append('Sabi')
spain_name.append('Saco')
spain_name.append('Santos')
spain_name.append('Sinisterra')
spain_name.append('Sofía')
spain_name.append('Tugores')
spain_name.append('Umberto')
spain_name.append('Uribe')
spain_name.append('Urraca')
spain_name.append('Valentín')
spain_name.append('Varleta')
spain_name.append('Viarela')
spain_name.append('Viera')
spain_name.append('Villasis')
spain_name.append('Villeda')
spain_name.append('Xavier')
spain_name.append('Yoma')
spain_name.append('Zaviezo')
spain_name.append('Za artu')
spain_name.append('Zubieta')

spain_family=[]
spain_family.append('Castellano')
spain_family.append('Navarro')
spain_family.append('Salazar')
spain_family.append('Balderas')
spain_family.append('Montes')
spain_family.append('Rojo')
spain_family.append('Alvarez')
spain_family.append('Gonzalo')
spain_family.append('Hernando')
spain_family.append('Martín')
spain_family.append('Pere')
spain_family.append('Pedro')
spain_family.append('Alcocer')
spain_family.append('Cahuich')
spain_family.append('Arizmendi')
spain_family.append('La Croix')
spain_family.append('Herrera')
spain_family.append('Moya')
spain_family.append('Castro')
spain_family.append('Vargas')
spain_family.append('Ruiz')
spain_family.append('Serrano')
spain_family.append('Cabrera')
spain_family.append('Parra')
spain_family.append('Figueroa')
spain_family.append('Lozano')
spain_family.append('Sosa')
spain_family.append('Pena')
spain_family.append('Silva')
spain_family.append('Aguilar')
spain_family.append('Contreras')
spain_family.append('Ortiz')
spain_family.append('Moreno')
spain_family.append('Flores')
spain_family.append('Costa')
spain_family.append('Ramos')

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
        middle_name=spain_name[random.randint(0,35)]
        last_name=spain_name[random.randint(0,35)]
        full_name=first_name+' '+middle_name+' '+last_name
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
        interval=random.randint(0,interval)
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