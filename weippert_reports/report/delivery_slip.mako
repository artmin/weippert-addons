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
        Telefon: ${company.partner_id.phone}</br>
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
        Lieferschein
      </td>
      <td class="title" style="margin-right:1.3cm">
        <b>${o.name and o.name or 'Entwurf'}</b>
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
    </tr>
    % for line in o.move_lines:
    <tr>
      <td>${ o.move_lines.index(line)+1 }</td>
      <td>${ line.product_id.default_code or '' }</td>
      <td>${ line.product_id.name }</td>
      <td>${ formatLang(line.product_qty) }</td>
    </tr>
    % endfor
  </table>

  <table style="margin-top:1cm">
    <tr><td>Die gelieferte Ware bleibt bis zur vollst&auml;ndigen Bezahlung Eigentum
        des Lieferanten.</td></tr>
  </table>
  
  %endfor
</body>
</html>
