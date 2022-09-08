#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''Searches and displays the amount of files available with IFU in JWST.
Usage:
    Edit the variables in the file and run.
Author:
    Tiago Floriano - 2022-09-08
License:
    GNU GPL v3 License
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>5.
'''

from astroquery.mast import Mast
import smtplib

#notificar por email? 
notifmail = False

service = "Mast.Jwst.Filtered.Nirspec"
multiple_parameters = {"columns": "*",
               "filters": [
                            {"paramName": "exp_type",
                             "values": ['NRS_IFU']
                            },
                            {"paramName": "template",
                             "values": ['NIRSpec IFU Spectroscopy']
                            },
                            {"paramName": "productLevel",
                             "values": ['3']
                            },
                            {"paramName": "datamodl",
                             "values": ['IFUCubeModel']
                            },
                            {"paramName": "grating",
                             "values": ['G395M']
                            }#,
                            #{"paramName": "targname",
                            # "values": ['NGC 6720 OFF']
                            #}
                            ]}
response_multiple_parameters = Mast.service_request_async(service, multiple_parameters)
results_multiple_parameters = response_multiple_parameters[0].json()['data']

print("##############################")
print("### RESULTADOS ENCONTRADOS ###")
print("##############################\n")
contador=0

for result_multiple_parameters in results_multiple_parameters:
    contador+=1

print("Foram encontrados {} arquivos".format(contador))

print("\n##############################")
print("##############################")
print("##############################")

if(notifmail == True):
    ## outlook
    emailservidor = 'emailservidor@outlook.com'
    senhaservidor = 'senhaservidor'
    emaildestinatario = 'emaildestinatario@gmail.com'
    
    mensagem = 'Foram encontrados {} arquivos'.format(contador)
    
    bodymail = "\r\n".join([
        "Subject: JWST atualizado",
        "",
        mensagem
    ])
    try:
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    except Exception as e:
        print(e)
        smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
    #type(smtpObj) 
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(emailservidor, senhaservidor) 
    smtpObj.sendmail(emailservidor, emaildestinatario, bodymail) # Or recipient@outlook

    smtpObj.quit()
    pass