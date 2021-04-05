 <%inherit file="w.tpl"/>
   
     
   <table>
      <tr class="customTable">
         <th>Beziechnung (1)</th>
         <th>Von (1)</th>
         <th>Bis (1)</th>
         <th>Beschreibung (1)</th>
         <th>Maximale Anzahl (1)</th>
         <th>Minimale Anzahl (1)</th>
         <th>Status (1)</th>
     </tr>
      % for key_s in range(length):
      <tr class="customTable">
         <td>${data_o[key_s][0]}</td>
         <td>${data_o[key_s][1]}</td>
         <td>${data_o[key_s][2]}</td>
         <td>${data_o[key_s][3]}</td>
         <td>${data_o[key_s][4]}</td>
         <td>${data_o[key_s][5]}</td>
         <td>${data_u[key_s]}</td>
         
      </tr>
      % endfor
       

   </table>
   
    <div>
      <a href="/sort_mitarbeiter">zurück</a>
   </div>
