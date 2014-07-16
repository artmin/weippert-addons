<html>
<head>
    <style type="text/css">
        ${css}
    </style>
</head>
<body>
  %for o in objects :
  <table style="width:100%; padding-top:1.5cm">
    <tr>
      <td class="from" style="width:11.3cm">
        ${company.partner_id.name} &middot; 
        ${company.partner_id.street} &middot;
        ${company.partner_id.zip} ${company.partner_id.city}
      </td>
      <!-- info box -->
      <td rowspan="2" class="info">
        ${company.partner_id.name}<br/>
        Schraubengro&szlig;handel<br/>
        Webshop<br/>
        ${company.partner_id.street}<br/>
        ${company.partner_id.zip} ${company.partner_id.city}<br/>
        Telefon ${company.partner_id.phone}</br>
        Mail: ${company.partner_id.email}<br/>
        ${company.partner_id.web}
      </td>
    </tr>
    <!-- partner address -->
    <tr>
      <td>
        % if not o.partner_id.is_company:
          ${o.partner_id.parent_id.name or ''}<br/>
        % endif
        ${o.partner_id.name}<br/>
        ${o.partner_id.street or ''}<br/>
        ${o.partner_id.street2 or ''}<br/>
        ${o.partner_id.zip or ''} ${o.partner_id.city or ''}
      </td>
    </tr>
  </table>
  
  <table class="fullwidth" style="margin-top:2cm">
    <tr>
      <td class="title" style="margin-right:0.6cm">
        %if o.state not in ['draft','sent'] or '':
	  Auftragsbest&auml;tigung Nr.
	%endif        
        %if o.state in ['draft','sent'] or '':
	  Angebot Nr.
	%endif
      </td>
      <td class="title" style="margin-right:1.3cm">
        <b>${o.name}</b>
      </td>
      <td style="margin-right:0.6cm">
        vom
      </td>
      <td style="margin-right:1.3cm">
        ${ time.strftime('%d.%m.%Y') }
      </td>
      <td>
        % if o.partner_id.customer:
          Kunden-Nr.
        % elif o.partner_id.supplier:
          Lieferanten-Nr.
        % endif
        ${o.partner_id and o.partner_id.ref or ''}
      </td>
    </tr>
  </table>
  
  <table style="margin-top:1cm">
    <tr><td>Ihre Anfrage</td></tr>
  </table>
  
  <table class="fullwidth"  style="margin-top:1.5cm">
    <tr>
      <td>Pos.</td>
      <td>Artikelnummer</td>
      <td>Artikelbezeichnung</td>
      <td>Menge</td>
      <td>Preis/Einheit</td>
      <td class="right">Gesamtpreis</td>
    </tr>
    % for line in o.order_line:
    <tr>
      <td>${ o.order_line.index(line)+1 }</td>
      <td>${ line.product_id.default_code or '' }</td>
      <td>${ line.name }</td>
      <td>${ formatLang(line.product_uos and line.product_uos_qty or line.product_uom_qty) } ${ line.product_uos and line.product_uos.name or line.product_uom.name }</td>
      <td>${ formatLang(line.price_unit , digits=get_digits(dp='Product Price')) }</td>
      <td class="right">${ formatLang(line.price_subtotal, digits=get_digits(dp='Account'), currency_obj=o.pricelist_id.currency_id) }</td>
    </tr>
    % endfor
  </table>
  
  <table class="right" style="margin-top:0.5cm">
    <tr>
      <td>Gesamt Netto</td>
      <td  class="right">${ formatLang(o.amount_untaxed, dp='Account', currency_obj=o.pricelist_id.currency_id) }</td>
    </tr>
    <tr>
      <td>MwSt. 19 %</td>
      <td class="right">${ formatLang(o.amount_tax, dp='Account', currency_obj=o.pricelist_id.currency_id) }</td>
    </tr>
    <tr>
      <td>Rechnungsendbetrag</td>
      <td class="right">${ formatLang(o.amount_total, dp='Account', currency_obj=o.pricelist_id.currency_id) }</td>
    </tr>
  </table>

  <!-- Versandart, -bedingungen und Zahlungsbedingungen -->
  <table style="margin-top:1.5cm">
    <tr>
      <td>
        <p> ${ o.carrier_id and ('Versandart: ' + o.carrier_id.name) or '' }</p>
        <p> ${o.incoterm and ('Lieferbedingungen: ' + o.incoterm.name) or ''}</p>
        <p> ${o.payment_term and ('Zahlungsbedinungen: ') + o.payment_term.name or ''}</p>
      </td>
    </tr>
    <tr>
      <td> ${o.note and o.note or ''}</td>
      <td>
        %if o.state in ['draft','sent'] or '':
          Wir bedanken und für Ihre Anfrage und bieten freibleibend an.
        %endif
      </td>
    </tr>
  </table>      

  %endfor
</body>
</html>
