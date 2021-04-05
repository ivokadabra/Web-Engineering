
   <%inherit file="w.tpl"/> 
     
   <table>
      <tr class="customTable">
         <th>Name (1)</th>
         <th>Vorname (1)</th>
         <th>Akademische Grade (1)</th>
         <th>Tätigkeit (1)</th>
     </tr>
      % for key_s in range(length):
      <tr class="customTable">
         <td>${data_o[key_s][0]}</td>
         <td>${data_o[key_s][1]}</td>
         <td>${data_o[key_s][2]}</td>
         <td>${data_o[key_s][3]}</td>
         
         
      </tr>
      % endfor
   </table>
   
    <div>
      <a href="/sort_weiterbildung">zurück</a>
   </div>
