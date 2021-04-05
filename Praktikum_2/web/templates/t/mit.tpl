 <%inherit file="w.tpl"/>

   <table>
      <tr class="customTable">
         <th>Name (1)</th>
         <th>Vorname (1)</th>
         <th>Akademische Grade (1)</th>
         <th>Tätigkeit (1)</th>
         
      </tr>
      % for key_s in data_o:
      <tr class="customTable">
         <td><a href="/w/${key_s}">  ${data_o[key_s][0]} </a></td>
         <td>${data_o[key_s][1]}</td>
         <td>${data_o[key_s][2]}</td>
         <td>${data_o[key_s][3]}</td>
        
      </tr>
      % endfor
   </table>
  
    <div>
      <a href="/index">zurück</a>
   </div>
