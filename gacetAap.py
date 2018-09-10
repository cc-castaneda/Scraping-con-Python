#! /usr/bin/python
#/**By Camilo Castaneda**/
import urllib2
import csv
from lxml import html
import requests

with open('gacetaAAP2.csv', 'wb') as f:
    writer = csv.writer(f, delimiter='<')
    writer.writerow(['titulo',
    				'fecha',
    				'contenido_link',
    				'link',
    				'contenido_general'
    				])
    itera=range(11,144)
    #itera=[1,2,3,4,5,6,7,8,9]
    for i in itera:
	    sitio = requests.get('http://www.imprenta.gov.co/gacetap/gaceta.indice?v_num='+ str(i) +'&v_anog=2017')
	    gaceta = html.fromstring(sitio.text)
	    app = gaceta.xpath('/html', encoding="UTF-8")
	    for gacetapp in app:
			titulo = gacetapp.xpath('//center/font/strong')
			#esta replicada la ruta por eso tomo la primera
			fecha = gacetapp.xpath('///center/font/p/strong/text()')[:1]
			contenido1 = gacetapp.xpath('//td/a')
			c_link = gacetapp.xpath('//td/a[@target]')
			c_ = gacetapp.xpath('//td/text()')
			for tt in titulo:
				title = tt.xpath('text()')
			ttt = u', '.join(title).encode('utf-8') 
			for ff in fecha:
				date = ff
			fff = (date).encode('utf-8')
			for c1,c_l,c2 in zip(contenido1, c_link,c_):
				content_1= c1.xpath('text()')
				link = c_l.xpath('@href')
				content_2 = c2
				ll = u', '.join(link).encode('utf-8')
				cc = u', '.join(content_1).encode('utf-8')
				cc2 = (content_2).encode('utf-8')
				#print 'Titulo:' , title  , 'fecha: ', date,'contenido: ' , cc , 'link: ',ll, 'contenido 2: ',cc2
				print 'fecha: ', date
				#print 'contenido 2: ',cc2
				writer.writerow([ttt,fff,cc,('http://www.imprenta.gov.co')+ll,cc2])
