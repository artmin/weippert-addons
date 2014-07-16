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
    <!-- Lieferadressen --> 
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
        Rechnung
      </td>
      <td class="title" style="margin-right:1.3cm">
        <b>${o.number and o.number or 'Entwurf'}</b>
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
        ${ o.partner_id.ref and o.partner_id.ref or ''}
      </td>
    </tr>
  </table>
  
  <table style="margin-top:1cm">
    <tr><td>Ihre Bestellung</td></tr>
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
    % for line in o.invoice_line:
    <tr>
      <td>${ o.invoice_line.index(line)+1 }</td>
      <td>${ line.product_id.default_code or '' }</td>
      <td>${ line.name }</td>
      <td>${ formatLang(line.quantity) }</td>
      <td>${ formatLang(line.price_unit) + company.currency_id.symbol }</td>
      <td class="right">${ formatLang(line.price_subtotal) +
        company.currency_id.symbol }</td>
    </tr>
    % endfor
  </table>
  
  <table class="right" style="margin-top:0.5cm">
    <tr>
      <td>Gesamt Netto</td>
      <td  class="right">
        ${ formatLang(o.amount_untaxed) + company.currency_id.symbol }</td>
    </tr>
    <tr>
      <td>MwSt. 19 %</td>
      <td class="right">
        ${ formatLang(o.amount_tax) + company.currency_id.symbol }</td>
    </tr>
    <tr>
      <td>Rechnungsendbetrag</td>
      <td class="right">
        ${ formatLang(o.amount_total) + company.currency_id.symbol }
      </td>
    </tr>
  </table>

  <!-- Anmerkungen zu Steuern -->

  <table style="margin-top:3cm">
    <tr>
      <td>
        ${ o.fiscal_position.note and o.fiscal_position.note or ''}
        % if o.fiscal_position.name == 'Kunde EU Unternehmen (mit USt-ID)'
          ${o.partner_id.vat}
        % endif
      </td>
    </tr>
  </table>

  <!-- Versandart, -bedingungen und Zahlungsbedingungen -->
  <table style="margin-top:1.5cm">
    <tr>
      <td>
        <p>${ o.carrier_id and ('Versandart: ' + o.carrier_id.name) or '' }</p>
        <p>${o.incoterm and ('Lieferbedingungen: ' + o.incoterm.name) or ''}</p>
        <p>${o.payment_term and ('Zahlungsbedingungen: ' + o.payment_term.name) or ''}</p>
      </td>
    </tr>
  </table>

  <table style="margin-top:1.5cm">
    <tr>
      <td>
        ${o.comment and o.comment or ''}
      </td>
    </tr>
  </table>

  %endfor
</body>
</html>
